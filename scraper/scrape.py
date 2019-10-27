# import time
import os
from typing import List

from common import const, tools
from common.tools import fmt


def catalogue(url_base: str, filename_base: str, start=1, end=None):
    i = start-1
    while True:
        i += 1
        if end and i > end:
            break
        text = tools.page_content(fmt(url_base, page=i))
        if text is None:
            break
        tools.save(text, const.catalogue_directory, fmt(filename_base, i))


def recipe(recipe_url: str, recipe_filename_base: str, i: int, force=False):
    subfolder = 1000 * (i // 1000)
    directory = os.path.join(
        const.recipe_directory,
        f'{subfolder:05d}-{subfolder+999:05d}'
    )

    if force or not os.path.isfile(os.path.join(directory, fmt(recipe_filename_base, i))):
        # time.sleep(2)
        text = tools.page_content(recipe_url)
        if text is not None:
            # print(f'Fetched {i}')
            tools.save(text, directory, fmt(recipe_filename_base, i))
        # else:
            # print(f'Failed {i}')


def recipes(recipe_url_list: List[str], recipe_filename_base: str, start=0):
    for i, url in enumerate(recipe_url_list[start:], start=start):
        recipe(url, recipe_filename_base, i)
