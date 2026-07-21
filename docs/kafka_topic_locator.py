from __future__ import annotations

import os
import asyncio
from mcp_tools import search_data, get_data_details

class KafkaTopicLocator:
    """
    A utility class to locate and retrieve information about Kafka topics using MCP Tools.
    """

    def __init__(self) -> None:
        self.target_topic = os.getenv("KAFKA_TARGET_TOPIC", "epm-skls-ai.courses-to-take")

    async def locate_and_retrieve_topic_info(self) -> dict[str, str]:
        """
        Locate the Kafka topic using MCP tools and retrieve its relevant information.

        Returns:
            A dictionary with details of the located topic.

        Raises:
            ValueError: If no matching topics are found.
        """
        search_results = await search_data(self.target_topic)

        if not search_results:
            raise ValueError(f"Topic '{self.target_topic}' not found using MCP search.")

        for result in search_results:
            if result.get("name") == self.target_topic:
                return await get_data_details(result.get("id"))

        raise ValueError(f"Matching topic details for '{self.target_topic}' could not be determined.")

if __name__ == "__main__":
    async def main() -> None:
        locator = KafkaTopicLocator()
        try:
            topic_info = await locator.locate_and_retrieve_topic_info()
            print("Retrieved topic information:")
            print(topic_info)
        except ValueError as e:
            print(f"Error: {e}")

    asyncio.run(main())
