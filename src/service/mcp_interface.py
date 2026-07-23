from __future__ import annotations

import os

from asyncpg import create_pool
from kafka import KafkaConsumer

class McpService:
    def __init__(self, kafka_topic: str, db_url: str):
        self.kafka_topic = kafka_topic
        self.db_url = db_url

    async def search_data(self, identifier: str):
        async with create_pool(self.db_url) as pool:
            async with pool.acquire() as connection:
                result = await connection.fetch("""
                    SELECT data
                    FROM records
                    WHERE identifier = $1
                """, identifier)
        return result

    async def process_topic_entities(self):
        consumer = KafkaConsumer(
            self.kafka_topic,
            bootstrap_servers=os.getenv("KAFKA_SERVERS"),
        )
        for message in consumer:
            identifier = message.key.decode('utf-8')
            matching_entities = await self.search_data(identifier)

            if not matching_entities:
                print(f"No matching entity for identifier {identifier}")
                continue
            print(f"Matching entity found: {matching_entities[0]}" )
