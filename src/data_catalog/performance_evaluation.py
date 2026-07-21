from __future__ import annotations

import time
from collections.abc import Callable

def evaluate_mcp_performance(search_data: Callable[[str], str], test_cases: list[str]) -> dict[str, float]:
    """
    Evaluates the performance of the MCP search_data function.

    Args:
        search_data: A callable that performs the search.
        test_cases: A list of test input strings.

    Returns:
        A dictionary containing performance metrics.
    """
    performance_metrics = {}
    for test_case in test_cases:
        start_time = time.time()
        _ = search_data(test_case)
        end_time = time.time()
        performance_metrics[test_case] = end_time - start_time
    return performance_metrics
