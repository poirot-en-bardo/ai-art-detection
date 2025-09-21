# Detecting AI-Generated Art with Deep Learning and Frequency Analysis

This repository contains the code and experiments for our Deep Learning course project during the Erasmus Mundus Master of Science in Computer Science.  
We combine **state-of-the-art deep neural networks** with **Fourier-domain analysis** to detect and understand differences between authentic and AI-generated artworks.

---

## 🔍 Overview

Generative AI (diffusion models, GANs) produces increasingly realistic art that is hard to distinguish from human-made works.  
Our project builds on existing literature but extends it by:

- Implementing and benchmarking **deep learning classifiers** (VGG-19, ResNet-50, Vision Transformer).  
- Incorporating **Fourier-domain features** to analyze hidden frequency patterns.  
- Improving model interpretability with **Grad-CAM and spectral visualizations**.  

This hybrid approach allows both **high accuracy** in classification and **insights** into how AI art differs from authentic art.

---

## 🧰 Key Components

### 1. Deep Learning Models
- **VGG-19**, **ResNet-50**, and **ViT** implemented.  
- Fine-tuned on a balanced dataset of authentic vs AI-generated artworks.  
- Optimized with Adam, early stopping, and learning-rate scheduling.  
- Metrics: Accuracy, Precision, Recall, F1.

### 2. Frequency / Fourier Analysis
- Compute **2D FFT** on artworks.  
- Extract **spectral fingerprints** (radial profiles, peaks, high/low-frequency energy ratios).  
- Optionally **fuse** Fourier features with spatial features for classification.  
- Provides interpretability and a complementary view beyond RGB.

### 3. Explainability
- **Grad-CAM** heatmaps show which regions influence model predictions.  
- Spectral plots illustrate periodic artifacts or color inconsistencies indicative of generative models.

---

## 📦 Data

- Authentic artworks sampled from **𝒜𝑟𝑡𝒢𝑟𝑎𝑝ℎ** dataset.  
- AI-generated artworks sampled from **ArtiFact** and other diffusion/GAN models.  
- All images standardized to fixed resolution, split 80/10/10 (train/val/test).

---
