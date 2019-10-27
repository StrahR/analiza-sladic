from common import const, tools
from common.tools import fmt


def scrape_catalogue(url_base, filename_base, start=1, end=None):
    i = start-1
    while True:
        i += 1
        if end and i > end:
            break
        text = tools.page_content(fmt(url_base, page=i))
        if text is None:
            break
        tools.save(text, const.catalogue_directory, fmt(filename_base, i))
