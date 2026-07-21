"""
Module `kafka_topic_locator` provides functionality to locate Kafka topics in the EPAM Data Catalog.
"""

from __future__ import annotations

import os
from typing import Awaitable, Callable, TypeAlias

data_search_fn: TypeAlias = Callable[[str], Awaitable[list[dict[str, str]]]]
data_details_fn: TypeAlias = Callable[[str], Awaitable[dict[str, str]]]

def locate_topic(
    topic_name: str, search_data: data_search_fn, get_data_details: data_details_fn
) -> dict[str, str | None]:
    """
    Locate the Kafka topic in the EPAM Data Catalog and retrieve its details.

    Args:
        topic_name: Name of the Kafka topic to locate.
        search_data: Function to search the data catalog for potential matches.
        get_data_details: Function to fetch detailed information of a specific entity.

    Returns:
        A dictionary with topic information, or a message indicating the topic was not found.
    """

    try:
        results = await search_data(topic_name)
    except Exception as err:
        raise RuntimeError("Failed to search the data catalog") from err

    for result in results:
        if result.get("name") == topic_name:
            entity_id = result.get("entity_id")

            if entity_id:
                try:
                    details = await get_data_details(entity_id)
                    return {"status": "found", "details": details}
                except Exception as err:
                    raise RuntimeError("Failed to fetch entity details") from err

    return {"status": "not_found", "details": None}


# Environment variables
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

if KAFKA_TOPIC:
    # Mock functions for implementation demonstration
    async def mock_search_data(query: str) -> list[dict[str, str]]:
        return [{"entity_id": "123", "name": "epm-skls-ai.courses-to-take"}]

    async def mock_get_data_details(entity_id: str) -> dict[str, str]:
        return {"entity_id": entity_id, "name": "epm-skls-ai.courses-to-take", "info": "Example details"}

    result = locate_topic(KAFKA_TOPIC, mock_search_data, mock_get_data_details)
    print(result)
else:
    print("Environment variable KAFKA_TOPIC not set.")
