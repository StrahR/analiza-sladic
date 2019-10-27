from typing import Set

from bs4 import BeautifulSoup

from common import const, tools
from common.tools import fmt


def get_recipe_links(page: str, selector: str, prefix: str = '') -> Set[str]:
    soup = BeautifulSoup(page, 'lxml')
    recipe_anchors = soup.select(selector)
    return {prefix + a.get('href') for a in recipe_anchors}


def catalogues(filename_base: str, link_selector: str, start=1, end=1, prefix: str = ''):
    links = set()
    for i in range(start, end+1):
        links.update(
            get_recipe_links(
                tools.load(const.catalogue_directory, fmt(filename_base, i)),
                link_selector,
                prefix=prefix)
        )
    return links
