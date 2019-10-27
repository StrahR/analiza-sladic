import unittest
from unittest.mock import Mock, patch

from common import const
from scraper import scrape

# https://stackoverflow.com/a/54838760/11285128


def assert_not_called_with(self, *args, **kwargs):
    try:
        self.assert_any_call(*args, **kwargs)
    except AssertionError:
        return
    raise AssertionError('Expected %s to not have been called.' %
                         self._format_mock_call_signature(args, kwargs))


Mock.assert_not_called_with = assert_not_called_with


class TestScraper(unittest.TestCase):

    def setUp(self):
        self.url_base = "http://www.{page:02d}.com/"
        self.filename_base = "{:02d}.html"

    @patch('common.tools.save')
    @patch('common.tools.page_content')
    def test_scrape_catalogues_range(self, mock_page_content, mock_save):
        mock_page_content.return_value = "asd"

        scrape.catalogue(self.url_base, self.filename_base, start=7, end=10)

        mock_page_content.assert_any_call("http://www.07.com/")
        mock_page_content.assert_any_call("http://www.08.com/")
        mock_page_content.assert_any_call("http://www.09.com/")
        mock_page_content.assert_any_call("http://www.10.com/")

        mock_save.assert_any_call("asd", const.catalogue_directory, "07.html")
        mock_save.assert_any_call("asd", const.catalogue_directory, "08.html")
        mock_save.assert_any_call("asd", const.catalogue_directory, "09.html")
        mock_save.assert_any_call("asd", const.catalogue_directory, "10.html")

    @patch('common.tools.save')
    @patch('common.tools.page_content')
    def test_scrape_catalogues_full(self, mock_page_content, mock_save):
        mock_page_content.side_effect = ["asd", "asd", "asd", None]

        scrape.catalogue(self.url_base, self.filename_base)

        mock_page_content.assert_any_call("http://www.01.com/")
        mock_page_content.assert_any_call("http://www.02.com/")
        mock_page_content.assert_any_call("http://www.03.com/")
        mock_page_content.assert_any_call("http://www.04.com/")

        mock_save.assert_any_call("asd", const.catalogue_directory, "01.html")
        mock_save.assert_any_call("asd", const.catalogue_directory, "02.html")
        mock_save.assert_any_call("asd", const.catalogue_directory, "03.html")
        mock_save.assert_not_called_with(
            "asd", const.catalogue_directory, "04.html")
