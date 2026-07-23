from __future__ import annotations

import os

class CatalogLocator:
    """Utility class to locate catalog entities based on provided Kafka topics."""

    def __init__(self, mcp_client: MCPClient, kafka_topic: str):
        """Initialize the CatalogLocator with an MCP client and Kafka topic."""
        self.mcp_client = mcp_client
        self.kafka_topic = kafka_topic

    def locate(self) -> dict:
        """Locate the catalog entity using MCP for the Kafka topic."""
        entity = self.mcp_client.search_data(self.kafka_topic)
        if not entity:
            raise ValueError(f"No entity found for topic: {self.kafka_topic}")
        details = self.mcp_client.get_data_details(entity['id'])
        return details


class MCPClient:
    """Mock representation of an MCP client with methods for searching and retrieving data."""

    def search_data(self, query: str) -> dict | None:
        """Mock search data method returning a catalog entity."""
        if query == 'epm-skls-ai.courses-to-take':
            return {"id": "1234", "name": query}
        return None

    def get_data_details(self, entity_id: str) -> dict:
        """Mock get data details method returning details for an entity."""
        return {"id": entity_id, "name": "Entity Details"}
