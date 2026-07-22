import pydicom
import numpy as np
import cv2
import matplotlib.pyplot as plt

# 1) path of the test file
file_path = pydicom.data.get_testdata_file("CT_small.dcm")

# 2) read the file, returns a dataset object
ds = pydicom.dcmread(file_path)

# 3) print patient and image info
print("Patient ID:", ds.PatientID)
print("Modality: ", ds.Modality)
print("Image Dimensions:", ds.Rows, "x", ds.Columns)


# 1) convert pixel data to numpy array
pixel_array = ds.pixel_array

# 2) check shape
print("Matrix shape:", pixel_array.shape)
print("Data type:", pixel_array.dtype)

# 3) find min-max pixel values
min_val = pixel_array.min()
max_val = pixel_array.max()
print("Min pixel value:", min_val)
print("Max pixel value:", max_val)

# 4) min-max normalization (scale to 0-255)
normalized = (pixel_array - min_val) / (max_val - min_val) * 255

# 5) convert to uint8
normalized_img = normalized.astype(np.uint8)

print("Normalized min:", normalized_img.min())
print("Normalized max:", normalized_img.max())


# apply histogram equalization to normalized image
equalized_img = cv2.equalizeHist(normalized_img)

print("Equalized min:", equalized_img.min())
print("Equalized max:", equalized_img.max())


# 1) create 2 subplots side by side
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# 2) left side - original (normalized) image
axes[0].imshow(normalized_img, cmap="gray")
axes[0].set_title("Original CT")
axes[0].axis("off")

# 3) right side - equalized image
axes[1].imshow(equalized_img, cmap="gray")
axes[1].set_title("Processed CT (Equalized)")
axes[1].axis("off")

# 4) save as png
plt.savefig("ct_comparison.png")
plt.show()