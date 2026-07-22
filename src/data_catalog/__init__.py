from __future__ import annotations

import aiohttp
import json
from typing import Any

class DataEntityRetriever:
    """Class to retrieve data entities via EPAM Data Catalog MCP tools."""

    BASE_URL = "https://datacatalog.epam.com"

    def __init__(self) -> None:
        self.session = aiohttp.ClientSession()

    async def fetch_entity(self, catalog_id: int) -> dict[str, Any] | None:
        """Fetch data entity from catalog.

        Args:
            catalog_id (int): The ID of the entity to retrieve.

        Returns:
            dict[str, Any] | None: The entity data or None if not found.
        """
        url = f"{self.BASE_URL}/data/data-details/{catalog_id}/summary?utm_source=onehub-assistant&utm_medium=widget"
        async with self.session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None

    async def close(self) -> None:
        """Close the session."""
        await self.session.close()

# Fallback mechanism for entity retrieval:
def fallback_mechanism(catalog_id: int) -> dict[str, Any] | None:
    """Documented fallback for retrieving a data entity.

    Args:
        catalog_id (int): The ID of the entity to retrieve.

    Returns:
        dict[str, Any] | None: Fallback entity data or None if not found.
    """
    print(f"Entity {catalog_id} could not be retrieved using MCP tools.")
    print("Refer to Data Steward or Data Governance team for assistance.")
    return None

# Example Usage:
async def main() -> None:
    retriever = DataEntityRetriever()
    entity_data = await retriever.fetch_entity(255703)
    if entity_data is None:
        entity_data = fallback_mechanism(255703)
    await retriever.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
