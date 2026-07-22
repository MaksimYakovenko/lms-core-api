from __future__ import annotations

from collections.abc import Callable
from typing import Any

class MCP:
    """
    Mock MCP tool class to simulate 'search_data' and 'get_data_details'.
    These represent the exclusive tools allowed for data retrieval.
    """

    def search_data(self, query: str) -> list[dict[str, Any]]:
        """Simulates the 'search_data' functionality of MCP."""
        # Implementation here
        pass

    def get_data_details(self, identifier: str) -> dict[str, Any]:
        """Simulates the 'get_data_details' functionality of MCP."""
        # Implementation here
        pass

class DataRetrievalVerifier:
    """Class to validate MCP data retrieval usage."""

    def __init__(self, mcp: MCP) -> None:
        """
        Initialize the verifier with an MCP instance.
        
        :param mcp: The MCP tool instance.
        """
        self.mcp = mcp

    def retrieve_data(self, query: str) -> list[dict[str, Any]] | None:
        """
        Retrieves data using only allowed MCP functions.
        
        :param query: The search query to execute.
        :return: The search results or None if an error occurred.
        """
        try:
            results = self.mcp.search_data(query)
            return [self.mcp.get_data_details(result['id']) for result in results]
        except Exception as err:
            raise RuntimeError("Data retrieval failed.") from err
