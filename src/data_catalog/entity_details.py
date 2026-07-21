from __future__ import annotations

from typing import Any

class EntityDetailsFetcher:
    """A class for fetching entity details from the MCP."""

    def __init__(self, mcp_client: Any) -> None:
        """Initialize the fetcher with a configured MCP client instance.

        Args:
            mcp_client: The MCP client used to perform the requests.
        """
        self.mcp_client = mcp_client

    def get_details(self, entity_id: str) -> dict[str, Any]:
        """Fetch 'basic', 'governance', and 'links' details of a specific entity.

        Args:
            entity_id: The identifier of the entity to fetch details for.

        Returns:
            A dictionary containing the fetched details.
        """
        details = self.mcp_client.get_data_details(entity_id, sections=['basic', 'governance', 'links'])
        return details
