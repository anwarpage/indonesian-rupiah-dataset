# Contributing to Rupiah Banknotes Dataset

Thank you for your interest in contributing to this open-source dataset community! Every contribution — big or small — helps make Indonesian currency computer vision research more accessible.

## Ways to Contribute

### 1. Submit a Model Benchmark
Have you trained a classifier (MobileNetV3, EfficientNet, ResNet, ViT) or detector (YOLOv8/v11, RT-DETR) on this dataset?
1. Fork this repository and add your notebook/script under `examples/` (or link your public Kaggle/Colab notebook).
2. Add a row to the **Community Benchmarks** table in `README.md` with your split, metric (Top-1 Accuracy / mAP), model size, and GitHub handle.
3. Open a Pull Request — we will review and merge it promptly!

### 2. Contribute Annotations (e.g., YOLO Bounding Boxes)
- We welcome bounding-box or segmentation labels, especially for the `idr_mix/` folder.
- Keep label files lightweight (`.txt` / `.json` / `data.yaml`) and place them under an `annotations/` folder in your PR, referencing the exact filenames from Kaggle.

### 3. Contribute New Photos
- **Do not commit large raw image files directly to GitHub** (this repo stays lightweight).
- Open a **[Data Contribution Issue](https://github.com/anwarpage/indonesian-rupiah-dataset/issues/new?template=data_contribution.md)** describing the new images (denomination, emission year, lighting/environment, count) and link a temporary archive (Google Drive / Kaggle). Maintainers will verify quality and publish them in the next Kaggle dataset version with full credit!
- Ensure all contributed photos are **your own original photographs** and contain **no personal/identifying information** (faces, IDs, addresses).

### 4. Improve Scripts & Documentation
- Bug fixes, PyTorch/TensorFlow/ONNX examples, or documentation improvements can be submitted directly via Pull Request.

## Pull Request Guidelines
- Keep PRs focused on a single improvement.
- Run `python -m py_compile scripts/*.py` before submitting changes to Python scripts.
- Be respectful and follow our [Code of Conduct](CODE_OF_CONDUCT.md).
