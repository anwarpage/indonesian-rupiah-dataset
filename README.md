<div align="center">

# Rupiah Banknotes Dataset

**An open-source, community-driven Computer Vision dataset of Indonesian Rupiah banknotes (Rp1,000 – Rp100,000).**

<p>
  <a href="https://www.kaggle.com/datasets/mkaspulanwar/rupiah-banknotes-dataset">
    <img src="https://img.shields.io/badge/Kaggle-Download%20Dataset-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" alt="Download on Kaggle">
  </a>
  <a href="https://www.kaggle.com/code/mkaspulanwar/rupiah-banknotes-eda-pytorch-resnet18-starter">
    <img src="https://img.shields.io/badge/Notebook-Starter%20EDA-20BEFF?style=for-the-badge&logo=jupyter&logoColor=white" alt="Starter Notebook">
  </a>
  <a href="CONTRIBUTING.md">
    <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge" alt="PRs Welcome">
  </a>
  <a href="https://github.com/anwarpage/rupiah-banknotes-dataset/stargazers">
    <img src="https://img.shields.io/github/stars/anwarpage/rupiah-banknotes-dataset?style=for-the-badge&color=gold" alt="GitHub Stars">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="MIT License">
  </a>
</p>

<p>
  <a href="#overview">Overview</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#community-benchmarks">Benchmarks</a> •
  <a href="#roadmap">Roadmap</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#citation">Citation</a>
</p>

<br>

<img src="assets/cover_collage.jpg" alt="Rupiah Banknotes Dataset Preview" width="100%">

</div>

---

## Overview

**Rupiah Banknotes Dataset** is an open dataset of **1,392 real-world JPG photographs** (~3.74 GB) of Indonesian Rupiah banknotes across all 7 active paper denominations plus multi-note scenes.

Unlike scraped web collections or synthetic renders, every image was **photographed directly** under varied angles, lighting conditions, folds, and backgrounds — built to support:

- **Assistive Technology:** Mobile & edge currency readers for visually impaired users.
- **Academic Research & Theses:** Reproducible classification and object detection benchmarks.
- **Computer Vision Education:** Clean end-to-end pipelines from raw images to deployed models.

> **Lightweight GitHub Repository:** Full image files (**3.74 GB**) are hosted on **[Kaggle Datasets](https://www.kaggle.com/datasets/mkaspulanwar/rupiah-banknotes-dataset)** for fast downloads and free GPU notebooks. This repository hosts the documentation, download/split scripts, starter notebooks, and community benchmarks.

### Class Distribution

| Folder | Denomination | Images | Size | Task Focus |
| :--- | :--- | ---: | ---: | :--- |
| `idr_1000/` | Rp1,000 | 166 | 460.3 MB | Classification |
| `idr_2000/` | Rp2,000 | 178 | 398.4 MB | Classification |
| `idr_5000/` | Rp5,000 | 167 | 384.0 MB | Classification |
| `idr_10000/` | Rp10,000 | 156 | 430.5 MB | Classification |
| `idr_20000/` | Rp20,000 | 189 | 492.4 MB | Classification |
| `idr_50000/` | Rp50,000 | 202 | 612.0 MB | Classification |
| `idr_100000/` | Rp100,000 | 191 | 574.2 MB | Classification |
| `idr_mix/` | Mixed / multiple notes | 143 | 476.4 MB | Object Detection |
| **Total** | **8 folders** | **1,392** | **3.74 GB** | |

---

## Quick Start

### 1. Download in 1 Line (`kagglehub`)

```python
import kagglehub

path = kagglehub.dataset_download("mkaspulanwar/rupiah-banknotes-dataset")
print("Dataset path:", path)
```

### 2. Clone Companion Tools & Prepare Splits

```bash
git clone https://github.com/anwarpage/rupiah-banknotes-dataset.git
cd rupiah-banknotes-dataset
pip install -r requirements.txt

# Download dataset into ./data
python scripts/download.py --output ./data

# Inspect per-class counts and sizes
python scripts/stats.py --source ./data

# Create stratified 70% train / 15% val / 15% test splits
python scripts/split_dataset.py --source ./data --output ./splits
```

### 3. Train with PyTorch or TensorFlow

```python
# PyTorch ImageFolder
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

tf = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])
train_loader = DataLoader(datasets.ImageFolder("splits/train", transform=tf), batch_size=32, shuffle=True)
```

For a complete EDA + PyTorch walkthrough, open [`examples/rupiah_banknotes_starter.ipynb`](examples/rupiah_banknotes_starter.ipynb) or run it directly on **[Kaggle](https://www.kaggle.com/code/mkaspulanwar/rupiah-banknotes-eda-pytorch-resnet18-starter)**.

---

## Community Benchmarks

Trained a model on this dataset? **Submit your results via a Pull Request** (or open a [Benchmark Submission](https://github.com/anwarpage/rupiah-banknotes-dataset/issues/new?template=benchmark_submission.md)) to be featured on the leaderboard!

| Model | Task | Split (70/15/15) | Metric | Params | Code / Notebook | Contributor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ResNet18 *(Starter)* | 7-Class Classification | 80/20 | *Baseline Pipeline* | 11.7M | [Kaggle Notebook](https://www.kaggle.com/code/mkaspulanwar/rupiah-banknotes-eda-pytorch-resnet18-starter) | [@anwarpage](https://github.com/anwarpage) |
| *Your Model Here!* | Classification / YOLO | — | — | — | [Submit PR](CONTRIBUTING.md) | *Open for contributions* |

---

## Roadmap

We are actively growing this dataset with the community:

- [x] **v1.0** — Release 1,392 curated JPG images on Kaggle + lightweight companion repo & starter notebook.
- [ ] **v1.1** — Community YOLO bounding-box annotations for `idr_mix/` ([#1](https://github.com/anwarpage/rupiah-banknotes-dataset/issues/1)).
- [ ] **v1.2** — Reproducible classification benchmarks: MobileNetV3, EfficientNet, ViT ([#2](https://github.com/anwarpage/rupiah-banknotes-dataset/issues/2)).
- [ ] **v2.0** — Expanded 2022 Rupiah emission series, low-light/occluded samples, and Indonesian coin classes.

Have an idea or want to collaborate? Join **[GitHub Discussions](https://github.com/anwarpage/rupiah-banknotes-dataset/discussions)**!

---

## Contributing

Contributions of all kinds are warmly welcomed — whether you're adding new photos, labeling bounding boxes, sharing a Kaggle/Colab notebook, or improving scripts.

Please read **[CONTRIBUTING.md](CONTRIBUTING.md)** and our **[Code of Conduct](CODE_OF_CONDUCT.md)** to get started.

### Maintainers & Original Photographers

- **M. Kaspul Anwar** ([@anwarpage](https://github.com/anwarpage))
- **Muhammad Lutfan**
- **Andri Rahmadani**

---

## Citation

If this dataset helps your research, thesis, or project, please consider starring the repo and citing:

```bibtex
@misc{rupiah-banknotes-dataset,
  author       = {M. Kaspul Anwar and Muhammad Lutfan and Andri Rahmadani},
  title        = {Rupiah Banknotes Dataset (Indonesian Currency)},
  year         = {2025},
  howpublished = {\url{https://www.kaggle.com/datasets/mkaspulanwar/rupiah-banknotes-dataset}},
  note         = {GitHub: \url{https://github.com/anwarpage/rupiah-banknotes-dataset}}
}
```

---

## Responsible Use & License

This dataset is released under the **[MIT License](LICENSE)** for academic research, education, and legitimate computer vision applications. It **must not** be used for counterfeiting, fraud, or any illegal financial activity.

<div align="center">
  <br>
  <a href="https://blockstream.info/address/bc1q9jc7wnggqhuq7lqx29u49t3pv5ftk5lmwpl6k4" target="_blank">
    <img src="https://img.shields.io/badge/Support%20This%20Open%20Dataset-Bitcoin-ff9900?style=for-the-badge&logo=bitcoin&logoColor=white&labelColor=333333" alt="Support with Bitcoin">
  </a>
</div>
