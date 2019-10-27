from typing import Set

from bs4 import BeautifulSoup


def get_recipe_links(page: str, selector: str, prefix: str = '') -> Set[str]:
    soup = BeautifulSoup(page, 'lxml')
    recipe_anchors = soup.select(selector)
    return {prefix + a.get('href') for a in recipe_anchors}
