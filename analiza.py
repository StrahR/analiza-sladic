import json
import sys

import nose2

from common import const, tools
from common.tools import fmt
from parsing import parse
from scraper import scrape


def get_commands():
    return [
        'test',
        'scrape',
        'parse',
    ]


def get_help(argv) -> str:
    return (
        f"\nUsage\n  python {argv[0]} [options] <command>"
        f"\nOptions:"
        f"\n  -h, --help\t\tPrint help and exit"
        f"\nCommands:\n  "
        + "\n  ".join(get_commands())
    )


def run_scrape_catalogues():
    scrape.catalogue(
        const.allrecipes_url_base,
        const.allrecipes_filename_base
    )
    scrape.catalogue(
        const.jamie_oliver_url_base,
        const.jamie_oliver_filename_base,
        end=1
    )


def run_parse_catalogues():
    ar_recipes = parse.catalogues(
            const.allrecipes_filename_base,
        const.allrecipes_recipe_link_selector, end=764
        )
    jo_recipes = parse.catalogues(
        const.jamie_oliver_filename_base,
        const.jamie_oliver_recipe_link_selector,
        prefix="https://www.jamieoliver.com"
    )
    tools.save(json.dumps(list(ar_recipes), indent=4, ensure_ascii=False),
               const.data_directory, const.allrecipes_recipe_links_json)
    tools.save(json.dumps(list(jo_recipes), indent=4, ensure_ascii=False),
               const.data_directory, const.jamie_oliver_recipe_links_json)




if __name__ == "__main__":
    program_name = sys.argv[0]
    if len(sys.argv) == 1:
        print(f"{program_name}: missing operand")
        print(f"Try 'python {program_name} --help' for more information")
    elif '--help' == sys.argv[1] or '-h' == sys.argv[1]:
        print(get_help(sys.argv))
    elif 'test' == sys.argv[1]:
        nose2.discover(argv=[sys.argv[0]] + sys.argv[2:])
    elif 'scrape' == sys.argv[1]:
        print("Running scrape...")
        run_scrape_catalogue()
        print("Done!")
    elif 'parse' == sys.argv[1]:
        run_parse_catalogues()
    else:
        print(
            f"""{program_name}: unrecognised option '{" ".join(sys.argv[1:])}'.\n"""
            f"""Try 'python {program_name} --help' for more information.""")
