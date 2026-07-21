from __future__ import annotations

import pytest
from src.data_catalog.performance_evaluation import evaluate_mcp_performance

def mock_search_data(query: str) -> str:
    return query[::-1]

def test_evaluate_mcp_performance() -> None:
    test_cases = ["test1", "importance", "scale"]
    performance = evaluate_mcp_performance(mock_search_data, test_cases)
    assert all(isinstance(time, float) for time in performance.values())
