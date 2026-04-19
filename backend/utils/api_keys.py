import logging
from typing import List, Optional
from config import settings

log = logging.getLogger(__name__)

class KeyManager:
    def __init__(self):
        self._keys: List[str] = []
        self._current_index = 0
        self._load_keys()

    def _load_keys(self):
        # Prefer the list if available, otherwise use the single key
        if settings.GOOGLE_API_KEYS:
            self._keys = [k.strip() for k in settings.GOOGLE_API_KEYS.split(",") if k.strip()]
        
        if not self._keys and settings.GOOGLE_API_KEY and settings.GOOGLE_API_KEY != "dummy":
            self._keys = [settings.GOOGLE_API_KEY]
        
        if not self._keys:
            log.warning("No Gemini API keys found in configuration")
        else:
            log.info(f"Loaded {len(self._keys)} Gemini API keys for rotation")

    def get_key(self) -> Optional[str]:
        if not self._keys:
            return None
        return self._keys[self._current_index]

    def get_next_key(self) -> Optional[str]:
        if not self._keys:
            return None
        self._current_index = (self._current_index + 1) % len(self._keys)
        key = self._keys[self._current_index]
        masked_key = f"{key[:6]}...{key[-4:]}" if len(key) > 10 else "***"
        log.info(f"Rotated to API key index {self._current_index} ({masked_key})")
        return key

    @property
    def has_keys(self) -> bool:
        return len(self._keys) > 0

key_manager = KeyManager()
