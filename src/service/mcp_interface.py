from __future__ import annotations

import os
from typing import Iterator, Sequence, Dict

import asyncio
from asyncpg import create_pool, Pool
from kafka import KafkaConsumer

class McpService:
    """
    Service to handle MCP system communications, specifically to search for data related to Kafka topic entities.
    """

    def __init__(self, kafka_topic: str, db_url: str):
        """
        Initialize the service with Kafka topic and database URL.
        
        Args:
            kafka_topic: The Kafka topic to monitor.
            db_url: Database URL for connections.
        """
        self.kafka_topic: str = kafka_topic
        self.db_url: str = db_url
        self.db_pool: Pool | None = None

    async def initialize(self) -> None:
        """
        Initialize the database connection pool.
        """
        self.db_pool = await create_pool(self.db_url)

    async def terminate(self) -> None:
        """
        Close the database connection pool.
        """
        if self.db_pool is not None:
            await self.db_pool.close()

    async def search_data(self, identifier: str) -> list[Dict[str, str]]:
        """
        Search records in the database by identifier.
        
        Args:
            identifier: Identifier of the record to search.
        
        Returns:
            A list of dictionaries containing the matching record data.
        """
        assert self.db_pool is not None, "DB pool must be initialized before querying."  # nosec
        async with self.db_pool.acquire() as connection:
            query:str = """
                SELECT data
                FROM records
                WHERE identifier = $1
            """
            result: Sequence[Dict[str, str]] = await connection.fetch(query, identifier)
            return [dict(row) for row in result]

    def subscribe_to_topic(self) -> Iterator[str]:
        """
        Subscribe to the Kafka topic.
        
        Returns:
            Iterator of identifiers sent to the Kafka topic.
        """
        consumer = KafkaConsumer(
            self.kafka_topic,
            bootstrap_servers=os.getenv("KAFKA_SERVERS"),
        )
        try:
            for message in consumer:
                yield message.key.decode("utf-8")  # assuming message.key contains identifiers
        finally:
            consumer.close()

    async def process_topic_entities(self) -> None:
        """
        Process incoming entities from the Kafka topic.
        """
        async for identifier in self.subscribe_to_topic():
            matching_entities = await self.search_data(identifier)

            if not matching_entities:
                print(f"No matching entity for identifier {identifier}")
                continue

            print(f"Matching entity found: {matching_entities[0]}")

# Please note that the changes made include creation of db pool and using async generator to limit
# redundant processing.
