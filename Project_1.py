import cv2 as cv
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')

input_image = cv.imread('/content/drive/My Drive/input_image6.jpg')

gray_image = input_image.mean(axis=2)

cv_gray_image = cv.cvtColor(input_image, cv.COLOR_BGR2GRAY)

cv2_normalized = cv.equalizeHist(cv_gray_image)

CLAHE = cv.createCLAHE()
cv2_CLAHE_normalized = CLAHE.apply(cv_gray_image)

hist_CLAHE = [0] * 256
for row in cv2_CLAHE_normalized:
    for pixel in row:
        hist_CLAHE[int(pixel)] += 1

hist_cv2 = [0] * 256
for row in cv2_normalized:
    for pixel in row:
        hist_cv2[int(pixel)] += 1

hist_original = [0] * 256
for row in gray_image:
    for pixel in row:
        hist_original[int(pixel)] += 1

sum_Pr = [0] * 256
n,m = gray_image.shape
for i in range(256):
  if i == 0:
    sum_Pr[i] = hist_original[i]/(m*n)
  else:
    sum_Pr[i] = (hist_original[i]/(m*n))+sum_Pr[i-1]

cdf_original = [0] * 256

for i in range(256):
  cdf_original[i] = int(255 * sum_Pr[i])

cdf_max = max(cdf_original)
cdf_min = min(cdf_original)

normalized_image = [[int((cdf_original[int(pixel)] - cdf_min) / (cdf_max-cdf_min) * 255) for pixel in row] for row in gray_image]


hist_normalized = [0] * 256
for row in normalized_image:
    for pixel in row:
        hist_normalized[pixel] += 1


plt.figure(figsize=(12,6))
#plt.subplot(2,2,1)
#plt.imshow(input_image)
#plt.title('Original Image')

#plt.subplot(2,2,2)
#plt.plot(hist_original,color='r')
#plt.title('Original Image Histogram')

#plt.subplot(2,2,2)
#plt.imshow(normalized_image,cmap='gray')
#plt.title('Normalized Image')

#plt.subplot(2,2,4)
#plt.plot(hist_normalized , color='b')
#plt.title('Normalized Image Histogram')

plt.subplot(2,2,1)
plt.imshow(cv2_normalized , cmap='gray')
plt.title('cv2 Normalized Image')

plt.subplot(2,2,2)
plt.plot(hist_cv2 , color='r')
plt.title('cv2 Normalized Image Histogram')

plt.subplot(2,2,3)
plt.imshow(cv2_CLAHE_normalized , cmap='gray')
plt.title('cv2 CLAHE Normalized Image')

plt.subplot(2,2,4)
plt.plot(hist_CLAHE , color='b')
plt.title('cv2 CLAHE Normalized Image Histogram')

plt.tight_layout()
plt.show()