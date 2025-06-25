import requests
import pytest
import logging
from jsonschema import validate
from typing import List, Dict

from util.helpers import load_test_data, send_request

logger = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "response,expected", [
        (
            lambda data=load_test_data("reports_basic.json"): (
                send_request(
                    data["method"],
                    data["url"]
                ).status_code,
                data["response_code"]
            )
        )(),
        (
            lambda data=load_test_data("reports_with_query_params.json"): (
                send_request(
                    data["method"],
                    data["url"],
                    data["query_params"],
                ).status_code,
                data["response_code"]
            )
        )(),
        (
            lambda data=load_test_data("reports_unsupported_category.json"): (
                send_request(
                    data["method"],
                    data["url"],
                    data["query_params"],
                ).status_code,
                data["response_code"]
            )
        )(),
        (
            lambda data=load_test_data("reports_unsupported_category.json"): (
                send_request(
                    data["method"],
                    data["url"],
                    data["query_params"],
                ).json()["message"],
                data["response_body"]["message"]
            )
        )(),
                (
            lambda data=load_test_data("reports_rating_big.json"): (
                send_request(
                    data["method"],
                    data["url"],
                    data["query_params"],
                ).status_code,
                data["response_code"]
            )
        )(),
        (
            lambda data=load_test_data("reports_rating_big.json"): (
                send_request(
                    data["method"],
                    data["url"],
                    data["query_params"],
                ).json()["message"],
                data["response_body"]["message"]
            )
        )(),

    ]
)
def test_response_code(response, expected):
    assert response == expected

@pytest.mark.parametrize(
    "response,expected",
    [
        (
            lambda data=load_test_data("reports_basic.json"): (
                send_request(
                    data["method"],
                    data["url"]
                ).json(),
                data["schema"]
            )
        )(),
        (
            lambda data=load_test_data("reports_with_query_params.json") : (
                send_request(
                    data["method"],
                    data["url"],
                    data["query_params"],
                ).json(),
                data["schema"]
            )
        )(),
                (
            lambda data=load_test_data("reports_unsupported_category.json") : (
                send_request(
                    data["method"],
                    data["url"],
                    data["query_params"],
                ).json(),
                data["schema"]
            )
        )()
    ]
)
def test_validate_schema(response, expected):
    validate(response, schema=expected)
