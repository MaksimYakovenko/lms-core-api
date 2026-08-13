"""Shared fixtures for OpenAPI-driven E2E tests."""

from __future__ import annotations

import os

import pytest

_OPENAPI_BASE_URL = ""


@pytest.fixture(scope="session")
def base_url() -> str:
    url = (os.getenv("INTEGRATION_BASE_URL") or "").rstrip("/")
    if not url:
        pytest.skip(
            "INTEGRATION_BASE_URL is not set - E2E suite is packaged with the "
            "MR but not executed without a staging target"
            + (f" (OpenAPI default was {_OPENAPI_BASE_URL!r})" if _OPENAPI_BASE_URL else "")
        )
    return url
