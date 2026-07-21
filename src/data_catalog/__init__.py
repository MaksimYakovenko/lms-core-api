from __future__ import annotations

import os
from typing import List, Dict, Any
import httpx

class DataCatalogClient:
    """Client to interact with the EPAM Data Catalog MCP API."""

    def __init__(self, base_url: str) -> None:
        """Initialize the DataCatalogClient.

        Args:
            base_url: The base URL of the EPAM Data Catalog MCP API.
        """
        self.base_url = base_url

    async def request_mcp(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        """Performs an asynchronous request to the MCP API.

        Args:
            endpoint: The MCP API endpoint to interact with.
            params: The parameters to include in the request.

        Returns:
            A dictionary containing the JSON response from the server.
        """
        async with httpx.AsyncClient() as client:
            headers = {"Authorization": f"Bearer {os.environ['MCP_API_KEY']}"}
            response = await client.get(f"{self.base_url}/{endpoint}", params=params, headers=headers)
            if response.status_code == 200:
                return response.json()
            raise httpx.HTTPError(f"MCP API request failed: {response.text}")

    async def search_data(self, query: str) -> List[str]:
        """Search the data catalog with the provided query.

        Args:
            query: The query string to search for.

        Returns:
            List of resulting data identifiers matching the query.
        """
        endpoint = "search"
        params = {"query": query}
        data = await self.request_mcp(endpoint, params)
        return [item["id"] for item in data.get("results", [])]

    async def get_data_details(self, identifier: str) -> Dict[str, str]:
        """Get details for the data by its identifier.

        Args:
            identifier: The identifier of the data item.

        Returns:
            A dictionary containing details of the specified data item.
        """
        endpoint = f"details/{identifier}"
        params = {}
        data = await self.request_mcp(endpoint, params)
        return data
