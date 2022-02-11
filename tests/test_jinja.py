import pytest

import fastapi_jinja
from fastapi_jinja.exceptions import FastAPIJinjaException


def test_missing_request_arg():
    with pytest.raises(FastAPIJinjaException):
        @fastapi_jinja.template("open/index.html")
        def view_root():
            return {}
