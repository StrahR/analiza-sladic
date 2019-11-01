import os
from typing import Callable, Dict, List, Set, Tuple, Union

from bs4 import BeautifulSoup

from common import const, tools
from common.tools import fmt

RecipeData = Union[str, Dict[str, Union[str, List[str]]], List[str]]
Recipe = Dict[str, RecipeData]
Selector = Tuple[str, str, Callable[[List[BeautifulSoup]], RecipeData]]


def get_recipe_links(page: str, selector: str, prefix: str = '') -> Set[str]:
    soup = BeautifulSoup(page, 'lxml')
    recipe_anchors = soup.select(selector)
    return {prefix + a.get('href') for a in recipe_anchors}


def catalogues(filename_base: str, link_selector: str, start=1, end=1, prefix: str = '') -> Set[str]:
    links = set()
    for i in range(start, end+1):
        links.update(
            get_recipe_links(
                tools.load(const.catalogue_directory, fmt(filename_base, i)),
                link_selector,
                prefix=prefix)
        )
    return links


def recipe(page: str, selectors: List[Selector]) -> Recipe:
    r = dict()
    soup = BeautifulSoup(page, 'lxml')
    for key, selector, f in selectors:
        r[key] = f(soup.select(selector))
    return r


def recipes(filename_base: str, selectors: List[Selector], start=0, end=0) -> List[Recipe]:
    rs = list()
    for i in range(start, end+1):
        subfolder = 1000 * (i // 1000)
        directory = os.path.join(
            const.recipe_directory,
            f'{subfolder:05d}-{subfolder+999:05d}'
        )
        rs.append(recipe(
            tools.load(directory, fmt(filename_base, i)),
            selectors
        ))
    return rs
