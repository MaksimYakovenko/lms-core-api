from __future__ import annotations

import os
import logging
import httpx

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def fetch_data_entity(topic: str) -> dict[str, object]:
    """Fetches the data entity for the specified Kafka topic using the Data Catalog MCP API."""
    api_url = os.getenv("DATA_CATALOG_API_URL")
    if not api_url:
        raise ValueError("The environment variable 'DATA_CATALOG_API_URL' is not set.")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{api_url}/entities", params={"topic": topic})
            response.raise_for_status()
            data = response.json()
            return {
                "basic": data.get("basic"),
                "governance": data.get("governance"),
                "links": data.get("links"),
            }
    except (httpx.RequestError, httpx.HTTPStatusError) as err:
        logger.error("Request to Data Catalog MCP API failed.", exc_info=True)
        raise RuntimeError(f"Failed to retrieve data entity: {err}") from err
