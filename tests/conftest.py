import logging
from logging.config import dictConfig
from pathlib import Path

import yaml

LOGGING_CONFIG_PATH = Path("config", "logging.yaml")

logging_config_dict = yaml.safe_load(open(LOGGING_CONFIG_PATH))

# Create log file folder if needed
log_file_path = Path(logging_config_dict["handlers"]["File"]["filename"])
log_file_path.parent.mkdir(parents=True, exist_ok=True)

dictConfig(logging_config_dict)
logger = logging.getLogger(__name__)
logger.info(f"Logging config loaded from: {LOGGING_CONFIG_PATH}")
