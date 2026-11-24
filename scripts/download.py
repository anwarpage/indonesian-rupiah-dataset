"""Download the Rupiah Banknotes Dataset from Kaggle using kagglehub."""

import argparse
import shutil
from pathlib import Path

import kagglehub

DATASET_HANDLE = "mkaspulanwar/rupiah-banknotes-dataset"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download the Rupiah Banknotes Dataset from Kaggle."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional local directory to copy the downloaded dataset into (e.g., ./data).",
    )
    args = parser.parse_args()

    print(f"Downloading '{DATASET_HANDLE}' from Kaggle...")
    cache_path = Path(kagglehub.dataset_download(DATASET_HANDLE))
    print(f"Downloaded to KaggleHub cache: {cache_path}")

    if args.output is not None:
        args.output.mkdir(parents=True, exist_ok=True)
        for item in cache_path.iterdir():
            if item.is_dir() and item.name.startswith("idr_"):
                target = args.output / item.name
                if target.exists():
                    shutil.rmtree(target)
                shutil.copytree(item, target)
        print(f"Copied class folders to: {args.output.resolve()}")


if __name__ == "__main__":
    main()
