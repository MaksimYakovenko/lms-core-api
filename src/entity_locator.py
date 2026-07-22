from __future__ import annotations

import os
from typing import cast
import asyncpg
import asyncio

class EntityLocator:
    """A class to locate Kafka topics via the MCP tool."""

    def __init__(self, kafka_topic: str) -> None:
        self.kafka_topic = kafka_topic

    async def locate_entity(self) -> dict[str, object] | None:
        """Locate the Kafka topic entity and retrieve its details."""
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            raise ValueError("DATABASE_URL environment variable is not set.")
        
        async with asyncpg.create_pool(database_url) as pool:
            async with pool.acquire() as connection:
                query = """
                SELECT attributes, governance_information, links
                FROM kafka_topics
                WHERE topic_name = $1;
                """
                try:
                    result = await connection.fetchrow(query, self.kafka_topic)
                    if result:
                        return {
                            "attributes": result["attributes"],
                            "governance_information": result["governance_information"],
                            "links": result["links"],
                        }
                    else:
                        return None
                except asyncpg.PostgresError as err:
                    raise RuntimeError("Database query failed.") from err

if __name__ == "__main__":
    topic_name = os.getenv("KAFKA_TOPIC", "default-topic")
    locator = EntityLocator(topic_name)
    try:
        result = asyncio.run(locator.locate_entity())
        if result is None:
            print("Topic not found.")
        else:
            print(result)
    except Exception as e:
        print(f"Error: {e}")
