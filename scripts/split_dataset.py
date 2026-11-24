"""Create stratified train/val/test splits for the Rupiah Banknotes Dataset."""

import argparse
import random
import shutil
from pathlib import Path

IMAGE_EXTS = {".jpg", ".jpeg", ".png"}
SINGLE_CLASSES = [
    "idr_1000",
    "idr_2000",
    "idr_5000",
    "idr_10000",
    "idr_20000",
    "idr_50000",
    "idr_100000",
]


def split_dataset(
    source_dir: Path,
    output_dir: Path,
    train_ratio: float = 0.70,
    val_ratio: float = 0.15,
    seed: int = 42,
    include_mix: bool = False,
) -> None:
    if not (0 < train_ratio < 1 and 0 <= val_ratio < 1 and train_ratio + val_ratio < 1):
        raise ValueError("train_ratio + val_ratio must be strictly between 0 and 1.")

    classes = list(SINGLE_CLASSES) + (["idr_mix"] if include_mix else [])
    rng = random.Random(seed)

    totals = {"train": 0, "val": 0, "test": 0}
    for cls in classes:
        cls_dir = source_dir / cls
        if not cls_dir.is_dir():
            print(f"[skip] Missing folder: {cls_dir}")
            continue

        images = sorted(p for p in cls_dir.iterdir() if p.suffix.lower() in IMAGE_EXTS)
        rng.shuffle(images)

        n = len(images)
        n_train = int(n * train_ratio)
        n_val = int(n * val_ratio)

        buckets = {
            "train": images[:n_train],
            "val": images[n_train : n_train + n_val],
            "test": images[n_train + n_val :],
        }

        for split_name, files in buckets.items():
            dest_dir = output_dir / split_name / cls
            dest_dir.mkdir(parents=True, exist_ok=True)
            for src in files:
                shutil.copy2(src, dest_dir / src.name)
            totals[split_name] += len(files)

        print(
            f"{cls:12s} | total={n:4d} -> train={len(buckets['train']):3d}, "
            f"val={len(buckets['val']):3d}, test={len(buckets['test']):3d}"
        )

    print(
        f"\nDone! Splits saved to '{output_dir.resolve()}' "
        f"(train={totals['train']}, val={totals['val']}, test={totals['test']})."
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Split Rupiah Banknotes Dataset into train/val/test folders."
    )
    parser.add_argument("--source", type=Path, required=True, help="Path to dataset root folder.")
    parser.add_argument("--output", type=Path, default=Path("splits"), help="Output directory.")
    parser.add_argument("--train", type=float, default=0.70, help="Train split ratio (default: 0.70).")
    parser.add_argument("--val", type=float, default=0.15, help="Val split ratio (default: 0.15).")
    parser.add_argument("--seed", type=int, default=42, help="Random seed (default: 42).")
    parser.add_argument(
        "--include-mix",
        action="store_true",
        help="Include 'idr_mix' folder in the classification split.",
    )
    args = parser.parse_args()

    split_dataset(
        source_dir=args.source,
        output_dir=args.output,
        train_ratio=args.train,
        val_ratio=args.val,
        seed=args.seed,
        include_mix=args.include_mix,
    )


if __name__ == "__main__":
    main()
