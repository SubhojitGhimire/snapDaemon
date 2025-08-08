import sys
import time
import logging
import argparse
import pyautogui
from typing import Dict
from pathlib import Path

TIME_UNITS: Dict[str, int] = {"s": 1, "m": 60, "h": 3600}
DEFAULT_SAVE_PATH = Path("..\Screenshots") # Change Path to any absolute/relative path you want. Example: C:\Users\SubhojitGhimire\OneDrive\Pictures\Screenshots
DEFAULT_TIME_UNIT = "m"
DEFAULT_FREQUENCY = 1

def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

def calculate_interval(frequency: int, unit: str) -> float:
    if frequency <= 0:
        logging.error("Frequency must be a positive number. Exiting.")
        sys.exit(1)

    seconds_per_unit = TIME_UNITS[unit]
    interval = seconds_per_unit / frequency

    # Enforce a minimum 1-second interval to prevent system overload.
    if interval < 1.0:
        logging.warning(
            f"Calculated interval is {interval:.2f}s. Enforcing a minimum of 1.0s."
        )
        return 1.0

    return interval

def take_screenshot(save_path: Path) -> None:
    try:
        save_path.mkdir(parents=True, exist_ok=True) # Ensure the save directory exists.

        # Create a unique filename.
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        file_name = f"screenshot_{timestamp}.png"
        full_path = save_path / file_name

        # Capture and save the screenshot.
        pyautogui.screenshot(full_path)
        logging.info(f"Screenshot saved to: {full_path}")

    except Exception as e:
        logging.error(f"Failed to take or save screenshot: {e}")


def main() -> None:
    setup_logging()

    parser = argparse.ArgumentParser(
        description="A tool to automatically take screenshots at a set interval.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=(
            "Usage Examples:\n"
            "  # Take 1 screenshot every 5 minutes and save to './screenshots'\n"
            "  python %(prog)s -t m -f 1\n\n"
            "  # Take 4 screenshots per hour and save to 'D:/Captures'\n"
            "  python %(prog)s -p 'D:/Captures' -t h -f 4\n\n"
            "  # Take 2 screenshots every second\n"
            "  python %(prog)s -t s -f 2"
        ),
    )

    parser.add_argument(
        "-p", "--path",
        type=Path,
        default=DEFAULT_SAVE_PATH,
        help=f"Path to store screenshots.\n(default: {DEFAULT_SAVE_PATH})",
    )
    parser.add_argument(
        "-t", "--type",
        type=str,
        default=DEFAULT_TIME_UNIT,
        choices=TIME_UNITS.keys(),
        help=f"Time unit: 'h' (hours), 'm' (minutes), or 's' (seconds).\n(default: {DEFAULT_TIME_UNIT})",
    )
    parser.add_argument(
        "-f", "--frequency",
        type=int,
        default=DEFAULT_FREQUENCY,
        help=f"Number of screenshots per time unit.\n(default: {DEFAULT_FREQUENCY})",
    )

    args = parser.parse_args()
    interval = calculate_interval(args.frequency, args.type)

    logging.info(
        f"Starting screenshot utility.\n"
        f"  - Save Path: {args.path.resolve()}\n"
        f"  - Frequency: {args.frequency} screenshot(s) per '{args.type}'\n"
        f"  - Interval:  Every {interval:.2f} seconds"
    )
    logging.info("Press Ctrl+C to stop the script.")

    try:
        while True:
            take_screenshot(args.path)
            time.sleep(interval)
    except KeyboardInterrupt:
        logging.info("\nScript terminated successfully!")
        sys.exit(0)
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()