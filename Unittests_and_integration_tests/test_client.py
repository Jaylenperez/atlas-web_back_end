#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org method with parameterized org names"""
        mock_payload = {"org_name": org_name, "info": "sample data"}
        mock_get_json.return_value = mock_payload

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, mock_payload)


    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test GithubOrgClient._public_repos_url property"""
        mock_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        mock_org.return_value = mock_payload

        client = GithubOrgClient("google")
        result = client._public_repos_url

        self.assertEqual(result, mock_payload["repos_url"])
        mock_org.assert_called_once()


if __name__ == "__main__":
    unittest.main()
