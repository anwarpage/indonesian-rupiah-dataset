"""Compute per-class image counts, disk size, and resolution stats."""

import argparse
from pathlib import Path

from PIL import Image, ImageOps

IMAGE_EXTS = {".jpg", ".jpeg", ".png"}
CLASS_ORDER = [
    "idr_1000",
    "idr_2000",
    "idr_5000",
    "idr_10000",
    "idr_20000",
    "idr_50000",
    "idr_100000",
    "idr_mix",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute Rupiah Banknotes Dataset statistics.")
    parser.add_argument("--source", type=Path, required=True, help="Path to dataset root folder.")
    parser.add_argument(
        "--check-res",
        action="store_true",
        help="Also read image headers to compute average resolution (slightly slower).",
    )
    args = parser.parse_args()

    total_imgs = 0
    total_bytes = 0

    header = f"{'Class':12s} | {'Images':>7s} | {'Size (MB)':>10s}"
    if args.check_res:
        header += f" | {'Avg Resolution':>15s}"
    print(header)
    print("-" * len(header))

    for cls in CLASS_ORDER:
        cls_dir = args.source / cls
        if not cls_dir.is_dir():
            continue
        imgs = [p for p in cls_dir.iterdir() if p.suffix.lower() in IMAGE_EXTS]
        size_bytes = sum(p.stat().st_size for p in imgs)
        total_imgs += len(imgs)
        total_bytes += size_bytes

        row = f"{cls:12s} | {len(imgs):7d} | {size_bytes / (1024**2):10.2f}"
        if args.check_res and imgs:
            widths, heights = [], []
            for p in imgs:
                with Image.open(p) as im:
                    w, h = ImageOps.exif_transpose(im).size
                    widths.append(w)
                    heights.append(h)
            avg_w = int(sum(widths) / len(widths))
            avg_h = int(sum(heights) / len(heights))
            row += f" | {avg_w}x{avg_h:>6}"
        print(row)

    print("-" * len(header))
    print(f"{'TOTAL':12s} | {total_imgs:7d} | {total_bytes / (1024**2):10.2f} MB ({total_bytes / (1024**3):.2f} GB)")


if __name__ == "__main__":
    main()
