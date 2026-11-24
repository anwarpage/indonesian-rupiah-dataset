<div align="center">

# Indonesian Rupiah Banknotes Dataset

<p>An open-source Computer Vision dataset of <b>1,392 real-world Indonesian Rupiah banknote images</b> (Rp1,000 – Rp100,000).</p>

<p>
  <a href="https://www.kaggle.com/datasets/mkaspulanwar/rupiah-banknotes-dataset">
    <img src="https://img.shields.io/badge/Kaggle-Download%20Dataset%20(3.74%20GB)-0284c7?style=flat&logo=kaggle&logoColor=white&labelColor=0f172a" alt="Download on Kaggle">
  </a>
  <a href="https://www.kaggle.com/code/mkaspulanwar/rupiah-banknotes-eda-pytorch-resnet18-starter">
    <img src="https://img.shields.io/badge/Notebook-Starter%20EDA-0f766e?style=flat&logo=jupyter&logoColor=white&labelColor=0f172a" alt="Starter Notebook">
  </a>
  <a href="https://github.com/anwarpage/indonesian-rupiah-dataset/stargazers">
    <img src="https://img.shields.io/github/stars/anwarpage/indonesian-rupiah-dataset?style=flat&logo=github&label=Stars&labelColor=0f172a&color=334155" alt="GitHub Stars">
  </a>
  <a href="CONTRIBUTING.md">
    <img src="https://img.shields.io/badge/PRs-Welcome-334155?style=flat&labelColor=0f172a" alt="PRs Welcome">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT%20%2F%20CC%20BY--NC--SA%204.0-334155?style=flat&labelColor=0f172a" alt="License">
  </a>
</p>

<p>
  <a href="#overview">Overview</a> &nbsp;·&nbsp;
  <a href="#quick-start">Quick Start</a> &nbsp;·&nbsp;
  <a href="#community-benchmarks">Benchmarks</a> &nbsp;·&nbsp;
  <a href="#contributing">Contributing</a> &nbsp;·&nbsp;
  <a href="#citation">Citation</a>
</p>

<br>

<img src="assets/cover_collage.jpg" alt="Indonesian Rupiah Banknotes Dataset Preview" width="100%">

</div>

---

## Overview

**Rupiah Banknotes Dataset** is an open dataset of **1,392 real-world JPG photographs** (~3.74 GB) of Indonesian Rupiah banknotes across all 7 active paper denominations plus multi-note scenes.

Every image was **photographed directly** under varied angles, lighting conditions, folds, and backgrounds (no synthetic or AI-generated images) — shared freely to support:

- **Assistive Technology:** Mobile & edge currency readers for visually impaired users.
- **Academic Research & Theses:** Reproducible classification and object detection experiments.
- **Computer Vision Education:** Clean end-to-end pipelines from raw images to deployed models.

> **Where are the image files?**
> Full image files (**3.74 GB**) are hosted on **[Kaggle Datasets](https://www.kaggle.com/datasets/mkaspulanwar/rupiah-banknotes-dataset)** for fast downloads and free GPU notebooks. This GitHub repository hosts `metadata.csv`, download/split scripts, starter notebooks, and community benchmarks.

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

### Metadata Index (`metadata.csv`)

[`metadata.csv`](metadata.csv) provides a structured index of all **1,392 images** with columns:
`filepath`, `filename`, `label`, `denomination_idr`, `width`, `height`, and `file_size_kb`.

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
git clone https://github.com/anwarpage/indonesian-rupiah-dataset.git
cd indonesian-rupiah-dataset
pip install -r requirements.txt

# Download dataset into ./data
python scripts/download.py --output ./data

# Inspect per-class counts and sizes
python scripts/stats.py --source ./data

# Create stratified 70% train / 15% val / 15% test splits
python scripts/split_dataset.py --source ./data --output ./splits
```

### 3. Train with PyTorch

```python
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

tf = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])
train_loader = DataLoader(datasets.ImageFolder("splits/train", transform=tf), batch_size=32, shuffle=True)
```

For a complete EDA + PyTorch walkthrough, open [`examples/rupiah_banknotes_starter.ipynb`](examples/rupiah_banknotes_starter.ipynb) or run it directly on **[Kaggle](https://www.kaggle.com/code/mkaspulanwar/rupiah-banknotes-eda-pytorch-resnet18-starter)**.

---

## Community Benchmarks

Trained a model on this dataset? **Submit your results via a Pull Request** (or open a [Benchmark Submission](https://github.com/anwarpage/indonesian-rupiah-dataset/issues/new?template=benchmark_submission.md)) to be featured below!

| Model | Task | Split | Metric | Params | Code / Notebook | Contributor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ResNet18 *(Starter)* | 7-Class Classification | 80/20 | *Baseline Pipeline* | 11.7M | [Kaggle Notebook](https://www.kaggle.com/code/mkaspulanwar/rupiah-banknotes-eda-pytorch-resnet18-starter) | [@anwarpage](https://github.com/anwarpage) |
| *Your Model Here!* | Classification / YOLO | — | — | — | [Submit PR](CONTRIBUTING.md) | *Open for contributions* |

---

## Contributing

Contributions are welcome — whether you want to share a benchmark notebook, add YOLO bounding-box annotations, or improve the helper scripts.

Please see **[CONTRIBUTING.md](CONTRIBUTING.md)** and **[Code of Conduct](CODE_OF_CONDUCT.md)**, or join **[GitHub Discussions](https://github.com/anwarpage/indonesian-rupiah-dataset/discussions)**.

### Dataset Authors

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
  note         = {GitHub: \url{https://github.com/anwarpage/indonesian-rupiah-dataset}}
}
```

---

## Responsible Use & License

This dataset is shared for academic research, education, and legitimate computer vision applications. It **must not** be used for counterfeiting, fraud, or any illegal financial activity.

Code & scripts in this repository are released under the **[MIT License](LICENSE)**; see the Kaggle Dataset page for dataset licensing details.
