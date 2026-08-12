from __future__ import annotations

import os
from mcp import search_data, get_data_details

def locate_kafka_topic_details(topic_name: str) -> dict[str, object] | None:
    """Locate Kafka topic details using MCP tools."""
    search_criteria: dict[str, object] = {"name": topic_name}
    search_results: list[dict[str, object]] = search_data(search_criteria)
    if search_results:
        topic_result = search_results[0]  # Assuming the first result is the desired one
        topic_details = get_data_details(topic_result["id"])
        return topic_details
    return None

def main() -> None:
    """Execute the function to locate Kafka topic details."""
    topic_name = os.getenv("KAFKA_TOPIC", "")
    if not topic_name:
        raise ValueError("Environment variable 'KAFKA_TOPIC' is not defined")
    topic_details = locate_kafka_topic_details(topic_name)
    if topic_details:
        print("Topic Details:")
        print(topic_details)
    else:
        print("Topic details not found.")

if __name__ == "__main__":
    main()
