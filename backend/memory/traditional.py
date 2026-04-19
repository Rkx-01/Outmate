import sqlite3
import json
import os
from datetime import datetime
from typing import Optional, Dict, Any

class TraditionalCache:
    def __init__(self, db_path: str = None):
        # Use env var or default to the data directory for persistence
        self.db_path = db_path or os.getenv("DATABASE_URL", "sqlite:///./data/gtm_intelligence.db").replace("sqlite:///", "")
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS run_history (
                    run_id TEXT PRIMARY KEY,
                    query TEXT,
                    timestamp TEXT,
                    confidence REAL,
                    result_count INTEGER,
                    retry_count INTEGER,
                    degraded BOOLEAN,
                    results TEXT
                )
            """)
            conn.commit()

    def save_run(self, run_id: str, query: str, confidence: float, result_count: int, retry_count: int, degraded: bool, results: Any):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO run_history VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (run_id, query, datetime.now().isoformat(), confidence, result_count, retry_count, degraded, json.dumps(results))
            )
            conn.commit()

    def get_history(self) -> list:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT run_id, query, timestamp, confidence, result_count, retry_count, degraded FROM run_history ORDER BY timestamp DESC")
            return [
                {
                    "run_id": r[0],
                    "query": r[1],
                    "timestamp": r[2],
                    "confidence": r[3],
                    "result_count": r[4],
                    "retry_count": r[5],
                    "degraded": r[6]
                }
                for r in cursor.fetchall()
            ]

    def get_run(self, run_id: str) -> Optional[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT * FROM run_history WHERE run_id = ?", (run_id,))
            row = cursor.fetchone()
            if row:
                return {
                    "run_id": row[0],
                    "query": row[1],
                    "timestamp": row[2],
                    "confidence": row[3],
                    "result_count": row[4],
                    "retry_count": row[5],
                    "degraded": row[6],
                    "results": json.loads(row[7])
                }
        return None
