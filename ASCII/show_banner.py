from pathlib import Path
import random
import argparse

BANNER_DIR = Path("banners")
DEFAULT_BANNER = Path("assets/banner.txt")


def list_banners():
    banners = sorted(BANNER_DIR.glob("*.txt"))

    if not banners:
        print("No banners found in banners/")
        return

    print("Available banners:")
    for banner in banners:
        print(f"- {banner.stem}")


def show_banner(name=None, random_mode=False):
    banners = sorted(BANNER_DIR.glob("*.txt"))

    if random_mode:
        if not banners:
            print("No banners found in banners/")
            return
        banner_path = random.choice(banners)

    elif name:
        banner_path = BANNER_DIR / f"{name}.txt"
        if not banner_path.exists():
            print(f"Banner not found: {banner_path}")
            print("Use --list to see available banners.")
            return

    else:
        banner_path = DEFAULT_BANNER
        if not banner_path.exists():
            print("Default banner not found: assets/banner.txt")
            print("Use a banner name or add a default banner.")
            return

    print(banner_path.read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description="Display ASCII banners.")
    parser.add_argument("name", nargs="?", help="Banner name without .txt")
    parser.add_argument("--random", action="store_true", help="Display a random banner")
    parser.add_argument("--list", action="store_true", help="List available banners")

    args = parser.parse_args()

    if args.list:
        list_banners()
    else:
        show_banner(name=args.name, random_mode=args.random)


if __name__ == "__main__":
    main()