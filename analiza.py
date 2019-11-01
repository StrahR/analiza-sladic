import json
import sys

import nose2

from common import const, tools
from parsing import parse
from scraper import scrape


def get_help(argv) -> str:
    return (
        f"Usage\n  python {argv[0]} [options] <command>"
        f"\nOptions:"

        f"\n  -h, --help\t\t\tPrint help and exit"
        f"\nCommands:"
        f"\n  test"
        f"\n  scrape <mode>\t\t\tSave pages locally"
        f"\n  parse <mode>\t\t\tExtract relevant data from local pages"
        f"\nModes:"
        f"\n  catalogues"
        f"\n  recipes"
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


def run_scrape_recipes():
    ar_recipe_urls = json.loads(tools.load(
        const.data_directory,
        const.allrecipes_recipe_links_json
    ))
    jo_recipe_urls = json.loads(tools.load(
        const.data_directory,
        const.jamie_oliver_recipe_links_json
    ))
    scrape.recipes(ar_recipe_urls, const.allrecipes_recipe_filename_base)
    scrape.recipes(jo_recipe_urls, const.jamie_oliver_recipe_filename_base)


def run_parse_recipes():
    jo_recipes = parse.recipes(
        const.jamie_oliver_recipe_filename_base,
        const.jamie_oliver_selectors, start=0, end=284
    )
    tools.save(json.dumps(list(jo_recipes), indent=4, ensure_ascii=False),
               const.data_directory, const.jamie_oliver_recipe_raw_data_json)

    # for i in range(0, 13292+1, 1000):
    ar_recipes = parse.recipes(
        const.allrecipes_recipe_filename_base,
        const.allrecipes_selectors, start=0, end=13292
    )
    tools.save(json.dumps(list(ar_recipes), indent=4, ensure_ascii=False),
               const.data_directory, const.allrecipes_recipe_raw_data_json)
    # const.data_directory, fmt(const.allrecipes_recipe_raw_data_json_base, i//1000))
    # print(f'Parsed {i+1000} recipes')


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
        if len(sys.argv) < 3:
            print(f"{program_name}: usage error: Mode required.")
        elif "catalogues" == sys.argv[2]:
            print("Scraping catalogues...")
            run_scrape_catalogues()
            print("Done!")
        elif "recipes" == sys.argv[2]:
            print("Scraping recipes...")
            run_scrape_recipes()
            print("Done!")
        else:
            print(
                f"""{program_name}: unrecognised mode '{" ".join(sys.argv[2])}'.\n"""
                f"""Try 'python {program_name} --help' for more information.""")
    elif 'parse' == sys.argv[1]:
        if len(sys.argv) < 3:
            print(f"{program_name}: usage error: Mode required.")
        elif "catalogues" == sys.argv[2]:
            print("Parsing catalogues...")
            run_parse_catalogues()
            print("Done!")
        elif "recipes" == sys.argv[2]:
            print("Parsing recipes...")
            run_parse_recipes()
            print("Done!")
        else:
            print(
                f"""{program_name}: unrecognised mode '{" ".join(sys.argv[2])}'.\n"""
                f"""Try 'python {program_name} --help' for more information.""")
    else:
        print(
            f"""{program_name}: unrecognised option '{" ".join(sys.argv[1:])}'.\n"""
            f"""Try 'python {program_name} --help' for more information.""")
