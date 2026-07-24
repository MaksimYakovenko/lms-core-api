from __future__ import annotations

import os
from typing import Any
import json
import aiohttp

class MCPInteraction:
    """A class to interact with EPAM Data Catalog MCP service."""

    def __init__(self, base_url: str) -> None:
        """Initialize the MCPInteraction instance.

        Args:
            base_url (str): The base URL of the MCP service.
        """
        self.base_url = base_url

    async def search_data(self, filters: dict[str, Any]) -> dict[str, Any]:
        """Search for data entities matching the provided filters.

        Args:
            filters (dict[str, Any]): The filters for the search query.

        Returns:
            dict[str, Any]: The search results as a dictionary.
        """
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/search", json=filters) as response:
                return await response.json()

    async def get_data_details(self, entity_id: str) -> dict[str, Any]:
        """Get details of a specific data entity by its ID.

        Args:
            entity_id (str): The ID of the entity.

        Returns:
            dict[str, Any]: The entity details as a dictionary.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/details/{entity_id}") as response:
                return await response.json()

async def main() -> None:
    """Main function demonstrating the interaction with MCP service."""

    mcp_service = MCPInteraction(base_url=os.getenv("MCP_SERVICE_URL", "http://localhost:8000"))

    search_filters = {"type": "KafkaTopic", "name": "example-topic"}
    search_results = await mcp_service.search_data(filters=search_filters)

    if search_results.get("results"):
        entity_id = search_results["results"][0]["id"]
        details = await mcp_service.get_data_details(entity_id=entity_id)
        print(json.dumps(details, indent=2))

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
