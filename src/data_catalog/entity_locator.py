from __future__ import annotations

# Standard library imports
import os

# Third-party imports
from asyncpg.pool import Pool

# Project-specific imports
from src.data_catalog.epam_interface import search_data

class EntityLocator:
    """Service to locate and retrieve entity information."""

    def __init__(self, kafka_topic: str) -> None:
        self.kafka_topic: str = kafka_topic

    async def locate_entity(self, db_pool: Pool) -> dict:
        """Locate and retrieve entity information based on Kafka topic.

        Args:
            db_pool: AsyncPG connection pool for database interactions.

        Returns:
            A dictionary containing the entity information.

        Raises:
            ValueError: If no entity information is found.
        """
        search_query = {
            "topic": self.kafka_topic
        }

        try:
            result = await search_data(search_query)
        except Exception as error:
            raise RuntimeError("Failed to fetch entity information.") from error

        if not result:
            raise ValueError(f"No entity found for topic: {self.kafka_topic}")

        return result
