import json
import os
from pathlib import Path

from dotenv import load_dotenv

# Environment
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or None
GEMINI_MODEL = os.getenv("GEMINI_MODEL") or "gemini-3.5-flash"

# Paths, anchored to the repo root so they don't depend on the working directory
BASE_DIR = Path(__file__).resolve().parent.parent
CORPUS_DIR = BASE_DIR / "corpus"
DATA_DIR = BASE_DIR / "data"
CHROMA_DIR = DATA_DIR / "chroma"
SETTINGS_FILE = DATA_DIR / "settings.json"
INDEX_STATE_FILE = DATA_DIR / "index_state.json"

# [DECISION D10] Default settings. chunk_size and chunk_overlap are in characters.
DEFAULT_SETTINGS = {"chunk_size": 1000, "chunk_overlap": 200, "top_k": 5}


def validate_settings(settings):
    """Return a clean settings dict, or raise ValueError naming the rule that failed."""
    if not isinstance(settings, dict):
        raise ValueError("Settings must be a JSON object with chunk_size, chunk_overlap and top_k.")

    values = {}
    for key in DEFAULT_SETTINGS:
        value = settings.get(key)
        # bool is a subclass of int in Python, so reject it explicitly
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValueError(f"{key} must be an integer.")
        values[key] = value

    if not 100 <= values["chunk_size"] <= 4000:
        raise ValueError("chunk_size must be between 100 and 4000.")
    if not 0 <= values["chunk_overlap"] < values["chunk_size"]:
        raise ValueError("chunk_overlap must be at least 0 and smaller than chunk_size.")
    if not 1 <= values["top_k"] <= 20:
        raise ValueError("top_k must be between 1 and 20.")
    return values


def load_settings():
    # If the file is missing, use the defaults
    if not SETTINGS_FILE.exists():
        return dict(DEFAULT_SETTINGS)
    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        return validate_settings(json.load(f))


def save_settings(settings):
    settings = validate_settings(settings)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2)
    return settings