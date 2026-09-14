import json
import os


CONFIG_FILE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "config.json")
)


def load_config():
    """Load NEXUS configuration from config.json."""
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def get_config(section, key, default=None):
    """Get a configuration value safely."""
    config = load_config()

    section_data = config.get(section, {})

    if not isinstance(section_data, dict):
        return default

    return section_data.get(key, default)