import json
import logging
import requests
from requests import Response
from typing import Dict

from pathlib import Path

TEST_DATA_PATH = Path("test_data")

logger = logging.getLogger(__name__)

CACHE = {}

def load_test_data(filename: str) -> Dict:
    if filename in CACHE.keys():
        logger.debug(f"Using data from cached filename: {filename}")
        return CACHE[filename]

    # Check filename includes extension
    assert Path(filename).suffix, "Need to include filename's extension"
    logger.debug(f"Loading test data from filename: {filename}")
    
    # Check file is exist
    full_filepath = Path(TEST_DATA_PATH, filename)
    assert Path(filename).is_file, f"{filename} is not under {TEST_DATA_PATH}"
    logger.debug(f"Full filepath: {full_filepath}")

    with open(full_filepath, 'r') as test_data_file:
        json_data = json.loads(test_data_file.read())
        CACHE[filename] = json_data
        return json_data


def send_request(method: str, url: str, params: Dict = None, payload: Dict = None) -> Response:
    assert method.upper() in ("GET", "POST", "DELETE", "PUT"), f"Unsupported http method: {method}"
    logger.debug("Sending requests to...") 
    logger.debug(f"{url=}")
    logger.debug(f"{method=}")
    logger.debug(f"{params=}")
    logger.debug(f"{payload=}")
    response = requests.request(
        method.upper(),
        url,
        params=params,
        data=payload
    )
    logger.debug("Response")
    logger.debug(f"{response.status_code=}")
    logger.debug(f"{response.content=}")
    return response
