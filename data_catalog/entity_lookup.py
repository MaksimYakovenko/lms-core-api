from __future__ import annotations

import os

def search_data(filters: dict[str, str]) -> list[dict]:
    """Mock function to search for data entities."""
    return [{"id": "entity123", "name": "Test Entity"}] if filters else []

def get_data_details(entity_id: str, sections: list[str]) -> dict:
    """Mock function to return data entity details."""
    return {"id": entity_id, "details": {section: "Details for " + section for section in sections}}

class DataCatalogLookup:
    """Class to look up details for Kafka topics in the data catalog."""

    def __init__(self, topic_name: str) -> None:
        self.topic_name = topic_name

    def fetch_entity_details(self) -> dict:
        """Find and retrieve the details of the data entity for the given Kafka topic."""
        filters = {"type": "kafka_topic", "name": self.topic_name}
        search_results = search_data(filters)
        if not search_results:
            raise ValueError("No entity found for the provided topic name.")
        entity_id = search_results[0]["id"]
        return get_data_details(entity_id, ["schema", "metadata"])
