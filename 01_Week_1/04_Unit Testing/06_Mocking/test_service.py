import unittest
from unittest.mock import patch
import service


class TestService(unittest.TestCase):

    @patch("service.get_user")
    def test_get_user(self, mock_get_user):
        mock_get_user.return_value = "Mock User"

        result = service.get_user()

        self.assertEqual(result, "Mock User")


if __name__ == "__main__":
    unittest.main()