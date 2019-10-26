import sys

from common import const
from scraper.scraper import scrape


def get_commands():
    return [
        'scrape',
    ]


def get_help(argv) -> str:
    return (
        f"\nUsage\n  python {argv[0]} [options] <command>"
        f"\nOptions:"
        f"\n  -h, --help\t\tPrint help and exit"
        f"\nCommands:\n  "
        + "\n  ".join(get_commands())
    )


def run_scrape():
    scrape(const.allrecipes_url_base, const.allrecipes_filename_base)
    scrape(const.jamie_oliver_url_base,
           const.jamie_oliver_filename_base, end=24)


if __name__ == "__main__":
    program_name = sys.argv[0]
    if len(sys.argv) == 1:
        print(f"{program_name}: missing operand")
        print(f"Try 'python {program_name} --help' for more information")
    elif '--help' == sys.argv[1] or '-h' == sys.argv[1]:
        print(get_help(sys.argv))
    elif "scrape" == sys.argv[1]:
        print("Running scrape...")
        run_scrape()
        print("Done!")
    else:
        print(
            f"""{program_name}: unrecognised option '{" ".join(sys.argv[1:])}'.\n"""
            f"""Try 'python {program_name} --help' for more information.""")
