#!/usr/bin/env python3
"""Unit tests for utils.access_nested_map"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test case for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns correct value."""
        self.assertEqual(access_nested_map(nested_map, path), expected)


    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("b",)),
        ({"a": {"b": 2}}, ("a", "c")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map raises KeyError for missing keys."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test case for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json returns expected JSON response from a URL."""
        with patch("utils.requests.get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)

if __name__ == "__main__":
    unittest.main()
