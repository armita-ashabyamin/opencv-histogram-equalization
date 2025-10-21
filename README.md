# opencv-histogram-equalization
This PDF is focused on histogram normalization techniques, including manual histogram equalization, OpenCV’s built-in equalizeHist, and CLAHE . Through Python code and visual comparisons, the project demonstrates how each method enhances image contrast and improves visibility, especially in low-light or unevenly illuminated images.

# Histogram Normalization Project

This project explores various histogram normalization techniques in image processing using Python and OpenCV. It demonstrates how contrast enhancement can be achieved through manual histogram equalization, OpenCV’s built-in `equalizeHist`, and CLAHE (Contrast Limited Adaptive Histogram Equalization).

## 📂 Contents

- Manual Histogram Equalization
- OpenCV `equalizeHist` Comparison
- CLAHE Algorithm Explanation
- Visual Comparisons of Input vs. Normalized Images
- Histogram Plots for Each Method

## 🛠 Technologies Used

- Python
- OpenCV (`cv2`)
- NumPy
- Matplotlib
- Google Colab

## 📈 Key Features

- Converts input images to grayscale
- Computes and visualizes histograms before and after normalization
- Implements manual histogram equalization using CDF
- Applies OpenCV’s `equalizeHist` and CLAHE for contrast enhancement
- Compares results visually and statistically

## 📚 CLAHE Overview

CLAHE improves upon traditional histogram equalization by:
- Enhancing contrast locally (per tile)
- Limiting contrast amplification to reduce noise
- Using bilinear interpolation to merge tiles seamlessly

## 👨‍🏫 Supervised By

Dr. Khosravi  
University of Birjand

## 👥 Contributors

- Mohsen Shayeghi  
- Armita As'hab Yamin

## 📎 How to Run

1. Mount your Google Drive in Colab.
2. Upload your input image to the specified path.
3. Run the notebook to view normalized images and histograms.

## 📌 Notes

This project is especially useful for improving image quality in fields like medical imaging, satellite imagery, and low-light photography.

