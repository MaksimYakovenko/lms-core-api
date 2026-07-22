from __future__ import annotations

import os
from typing import cast
import asyncpg
import asyncio

class EntityLocator:
    """A class to locate Kafka topics via the MCP tool."""

    def __init__(self, kafka_topic: str) -> None:
        self.kafka_topic = kafka_topic

    async def locate_entity(self) -> dict[str, object]:
        """Locate the Kafka topic entity and retrieve its details."""
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            raise ValueError("DATABASE_URL environment variable is not set.")
        
        details: dict[str, object] = {}
        async with asyncpg.create_pool(database_url) as pool:
            async with pool.acquire() as connection:
                try:
                    query = """
                    SELECT attributes, governance_information, links
                    FROM kafka_topics
                    WHERE topic_name = $1;
                    """
                    result = await connection.fetchrow(query, self.kafka_topic)
                    if result:
                        details = {
                            "attributes": result["attributes"],
                            "governance_information": result["governance_information"],
                            "links": result["links"],
                        }
                    else:
                        raise ValueError("Topic not found.")
                except asyncpg.PostgresError as err:
                    raise RuntimeError("Database query failed.") from err
        return details

if __name__ == "__main__":
    topic_name = os.getenv("KAFKA_TOPIC", "default-topic")
    locator = EntityLocator(topic_name)
    result = asyncio.run(locator.locate_entity())
    print(result)
