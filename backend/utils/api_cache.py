import sqlite3
import json
import hashlib
import functools
import logging
from datetime import datetime, timedelta
import os

log = logging.getLogger(__name__)

DB_PATH = "./data/gtm_intelligence.db"

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS external_api_cache (
                endpoint TEXT,
                payload_hash TEXT,
                response_json TEXT,
                created_at TIMESTAMP,
                PRIMARY KEY (endpoint, payload_hash)
            )
        ''')
        conn.commit()

init_db()

def _get_hash(*args, **kwargs):
    """Deterministically hash the arguments and kwargs for caching."""
    # Convert args and kwargs to a canonical JSON string
    return hashlib.sha256(json.dumps({"args": args, "kwargs": kwargs}, sort_keys=True).encode()).hexdigest()

def get_cached_response(endpoint: str, payload_hash: str, ttl_days: int) -> dict | list | None:
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT response_json, created_at FROM external_api_cache
                WHERE endpoint = ? AND payload_hash = ?
            ''', (endpoint, payload_hash))
            row = cursor.fetchone()
            if row:
                response_str, created_at_str = row
                created_at = datetime.fromisoformat(created_at_str)
                if datetime.utcnow() - created_at < timedelta(days=ttl_days):
                    log.info(f"💾 [CACHE HIT] {endpoint} ({payload_hash[:8]})")
                    return json.loads(response_str)
                else:
                    log.info(f"🗑️ [CACHE EXPIRED] {endpoint} ({payload_hash[:8]})")
    except Exception as e:
        log.error(f"Cache read error: {e}")
    return None

def set_cached_response(endpoint: str, payload_hash: str, data: dict | list):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO external_api_cache
                (endpoint, payload_hash, response_json, created_at)
                VALUES (?, ?, ?, ?)
            ''', (endpoint, payload_hash, json.dumps(data), datetime.utcnow().isoformat()))
            conn.commit()
            log.info(f"✍️ [CACHE SAVE] {endpoint} ({payload_hash[:8]})")
    except Exception as e:
        log.error(f"Cache write error: {e}")


def with_persistent_cache(ttl_days=30):
    """
    Decorator to cache external API functional calls into SQLite.
    The function name is used as the endpoint/key, and args/kwargs are hashed.
    """
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            endpoint = fn.__name__
            payload_hash = _get_hash(*args, **kwargs)
            
            cached = get_cached_response(endpoint, payload_hash, ttl_days)
            if cached is not None:
                return cached
            
            # Not cached, perform actual function
            result = fn(*args, **kwargs)
            
            # Don't cache empty lists or dicts — these are often transient API gaps
            # (e.g., events not yet indexed, or filtered results temporarily empty).
            # Caching empty results causes stale data that persists for days.
            is_empty = result is None or result == [] or result == {}
            if not is_empty:
                set_cached_response(endpoint, payload_hash, result)
            elif result is not None:
                log.warning(f"⚠️ [CACHE SKIP] {endpoint} ({payload_hash[:8]}) - empty result, not caching")
            
            return result
        return wrapper
    return decorator


def clear_cache_for_endpoint(endpoint: str):
    """Delete all cached entries for a specific endpoint. Use after schema changes."""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM external_api_cache WHERE endpoint = ?', (endpoint,))
            deleted = cursor.rowcount
            conn.commit()
            log.info(f"🗑️ [CACHE CLEAR] Deleted {deleted} rows for endpoint '{endpoint}'")
            return deleted
    except Exception as e:
        log.error(f"Cache clear error: {e}")
        return 0


def clear_all_cache():
    """Nuke the entire cache. Use when Explorium schema or taxonomy changes."""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM external_api_cache')
            deleted = cursor.rowcount
            conn.commit()
            log.info(f"🗑️ [CACHE CLEAR ALL] Deleted {deleted} total rows")
            return deleted
    except Exception as e:
        log.error(f"Cache clear-all error: {e}")
        return 0
