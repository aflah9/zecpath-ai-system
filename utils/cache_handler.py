import os
import json

CACHE_DIR = "cache"

def ensure_cache_dir():
    # If 'cache' exists but is a file → remove it
    if os.path.exists(CACHE_DIR) and not os.path.isdir(CACHE_DIR):
        os.remove(CACHE_DIR)

    os.makedirs(CACHE_DIR, exist_ok=True)


def load_from_cache(file_name):
    try:
        ensure_cache_dir()

        cache_file = os.path.join(CACHE_DIR, f"{file_name}.json")

        if os.path.exists(cache_file):
            with open(cache_file, "r") as f:
                return json.load(f)

    except Exception as e:
        print(f"[Cache Load Error]: {e}")

    return None


def save_to_cache(file_name, data):
    try:
        ensure_cache_dir()

        cache_file = os.path.join(CACHE_DIR, f"{file_name}.json")

        with open(cache_file, "w") as f:
            json.dump(data, f, indent=4)

    except Exception as e:
        print(f"[Cache Save Error]: {e}")