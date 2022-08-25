from pathlib import Path

from yaml import safe_load

from pipeliner import readers, utils


def main():
    utils.find_all_addons()

    config_dir = Path(__file__).parent
    config = safe_load((config_dir / 'config.yaml').read_text())

    for _, reader in config['readers'].items():
        print("***")
        print(reader)
        func = getattr(readers, reader['func'])
        print(f"- calling  {reader['func']}")
        func()


if __name__ == "__main__":
    main()
