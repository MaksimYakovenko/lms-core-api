from __future__ import annotations

import os
from collections.abc import Callable
import asyncpg

class KafkaTopicLocator:
    """
    A class to locate Kafka topics in the EPAM Data Catalog using MCP tools.
    """

    def __init__(self, db_url: str, kafka_target_topic: str):
        """
        Initialize the locator with a database connection and target topic.

        Args:
            db_url (str): The database URL for connection.
            kafka_target_topic (str): The Kafka topic name to find.
        """
        self.db_url = db_url
        self.kafka_target_topic = kafka_target_topic

    async def locate_topic(self) -> dict[str, str | int | None]:
        """
        Locate the Kafka topic in the EPAM Data Catalog.

        Returns:
            dict[str, str | int | None]: Details of the located Kafka topic.
        """
        async with asyncpg.create_pool(self.db_url) as pool:
            async with pool.acquire() as connection:
                query_primary = "SELECT * FROM catalog WHERE topic_name = $1"
                result_primary = await connection.fetchrow(query_primary, self.kafka_target_topic)
                if result_primary:
                    return dict(result_primary)
                query_fallback = "SELECT * FROM catalog WHERE topic_name LIKE $1 LIMIT 1"
                result_fallback = await connection.fetchrow(query_fallback, "%" + self.kafka_target_topic + "%")
                if result_fallback:
                    return dict(result_fallback)
                return {"error": "Topic not found"}

if __name__ == "__main__":
    db_url = os.getenv("DATABASE_URL")
    kafka_target_topic = os.getenv("KAFKA_TARGET_TOPIC")
    if db_url and kafka_target_topic:
        locator = KafkaTopicLocator(db_url, kafka_target_topic)
        details = locator.locate_topic()
        print("Located Kafka Topic details:", details)
    else:
        print("Environment variables not set correctly.")
