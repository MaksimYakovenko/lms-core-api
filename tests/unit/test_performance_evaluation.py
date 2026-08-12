# Import necessary libraries and modules
import pytest
from unittest.mock import Mock
from src.data_catalog.performance_evaluation import evaluate_mcp_performance

def test_evaluate_mcp_performance_valid_inputs():
    """
    Test the `evaluate_mcp_performance` function with valid inputs.
    """
    # Mock the search_data function to simulate delays
    search_data_mock = Mock()
    search_data_mock.side_effect = lambda x: "found"

    # Example test cases with unique inputs
    test_cases = ["search_item_one", "search_item_two", "search_item_three"]

    # Call the function under test
    result = evaluate_mcp_performance(search_data_mock, test_cases)

    # Validate the function results
    assert isinstance(result, dict)
    assert all(isinstance(v, float) for v in result.values())
    for test_case in test_cases:
        assert test_case in result

    # Ensure the mock was called the correct number of times
    assert search_data_mock.call_count == len(test_cases)
    for idx, tc in enumerate(test_cases):
        assert search_data_mock.call_args_list[idx][0][0] == tc

def test_evaluate_mcp_performance_empty_test_cases():
    """
    Test the `evaluate_mcp_performance` function with an empty test case list.
    """
    # Mock the search_data function
    search_data_mock = Mock()

    # Define empty test cases
    test_cases = []

    # Call the function under test
    result = evaluate_mcp_performance(search_data_mock, test_cases)

    # Validate the function results
    assert result == {}

    # Ensure the mock was not called
    search_data_mock.assert_not_called()

def test_evaluate_mcp_performance_response_times():
    """
    Test that the response times recorded by `evaluate_mcp_performance` are reasonable.
    """
    import time
    search_data_mock = Mock()
    search_data_mock.side_effect = lambda query: time.sleep(0.1) and "found"

    test_cases = ["test1", "test2"]
    result = evaluate_mcp_performance(search_data_mock, test_cases)

    for v in result.values():
        assert 0.1 <= v < 1.0