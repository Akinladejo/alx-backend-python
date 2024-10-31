#!/usr/bin/env python3
"""Test suite for the client module"""
from typing import Dict
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class"""

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org: str, expected: Dict, mock_get_json: Mock):
        """Test that GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = expected
        client = GithubOrgClient(org)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )

    def test_public_repos_url(self):
        """Test that _public_repos_url property works correctly"""
        expected_url = "https://api.github.com/orgs/testorg/repos"
        payload = {"repos_url": expected_url}
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("testorg")
            self.assertEqual(client._public_repos_url, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Mock):
        """Test the public_repos method"""
        test_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = test_payload

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/testorg/repos"
            )
            client = GithubOrgClient("testorg")

            self.assertEqual(
                client.public_repos(),
                ['repo1', 'repo2', 'repo3']
            )
            self.assertEqual(client.public_repos("mit"), ['repo1'])
            self.assertEqual(client.public_repos("apache-2.0"), ['repo2'])
            self.assertEqual(client.public_repos("nonexistent"), [])

            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/testorg/repos"
            )
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, license_key: str, expected: bool):
        """Test the has_license static method"""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected
        )


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the integration tests"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down after the integration tests"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Integration test for public_repos method"""
        client = GithubOrgClient("testorg")
        self.assertEqual(client.org, self.org_payload)
        self.assertEqual(client.repos_payload, self.repos_payload)
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(
            client.public_repos("apache-2.0"),
            self.apache2_repos
        )
        self.mock_get.assert_called()

    def test_public_repos_with_license(self):
        """Integration test for public_repos method with license filter"""
        client = GithubOrgClient("testorg")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(
            client.public_repos("apache-2.0"),
            self.apache2_repos
        )
        self.mock_get.assert_called()
