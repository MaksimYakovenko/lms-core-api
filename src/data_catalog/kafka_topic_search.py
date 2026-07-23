from __future__ import annotations

import os
from typing import Any, Dict

from external.mcp_tools import search_data, get_data_details

def search_kafka_topics(query: str) -> Dict[str, Any]:
    """
    Searches for Kafka topics matching the given query using the MCP tools.

    Args:
        query (str): The query string to search for.

    Returns:
        Dict[str, Any]: Details of the matched Kafka topic, if found.
    """
    
    # Perform the search using `search_data`
    search_filter = {"type": "kafka_topic"}  # Example filter to customize
    search_results = search_data(query=query, search_filter=search_filter)
    
    if search_results:
        matched_topic = search_results[0]  # Assume taking the first matching topic
        topic_details = get_data_details(matched_topic)
    else:
        topic_details = {}
    
    return topic_details
