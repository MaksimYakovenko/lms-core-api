"""Shared fixtures for OpenAPI-driven integration tests."""

from __future__ import annotations

import os

import pytest

# OpenAPI servers.url captured at generation time (informational only).
_OPENAPI_BASE_URL = ""


@pytest.fixture(scope="session")
def base_url() -> str:
    """Base URL for the API under test.

    Requires ``INTEGRATION_BASE_URL`` so suites packaged in the MR do not
    accidentally hit a production host from the OpenAPI servers entry.
    """
    url = (os.getenv("INTEGRATION_BASE_URL") or "").rstrip("/")
    if not url:
        pytest.skip(
            "INTEGRATION_BASE_URL is not set - integration suite is packaged "
            "with the MR but not executed without a staging target"
            + (f" (OpenAPI default was {_OPENAPI_BASE_URL!r})" if _OPENAPI_BASE_URL else "")
        )
    return url
