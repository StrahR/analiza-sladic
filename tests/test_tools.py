import os
import unittest
from unittest.mock import mock_open, patch

import requests

from common.tools import page_content, save


class TestTools(unittest.TestCase):

    def setUp(self):
        self.url = "https://example.com/"
        self.directory = "dir"
        self.filename = "file.html"
        self.text = requests.get(self.url).text

    def test_page_content(self):
        self.assertEqual(page_content(self.url), self.text)

    @patch('os.path.exists')
    @patch('os.makedirs')
    def test_save(self, mock_make_dirs, mock_exists):
        mock_exists.return_value = True

        open_mock = mock_open()
        with patch("common.tools.open", open_mock, create=True):
            save(self.text, self.directory, self.filename)

        # test create dir
        mock_make_dirs.assert_called_with(self.directory, exist_ok=True)
        # test open file for writing
        open_mock.assert_called_with(os.path.join(
            self.directory, self.filename), "w", encoding='utf-8')
        # test writing text to file
        open_mock.return_value.write.assert_called_once_with(self.text)


if __name__ == '__main__':
    unittest.main()
