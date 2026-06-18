import numpy as np

# Load one sample file from your drive
sample_file_path = "/content/drive/MyDrive/PSL_Landmarks_Numpy/28-computer/6559-router_router_1665481637_65148.npy"

try:
    data = np.load(sample_file_path)
    print("=== DATA STRUCTURAL VERIFICATION ===")
    print(f"File Shape: {data.shape}")
    print(f"Total Frames Sampled: {data.shape[0]} (Should match SEQUENCE_LENGTH)")
    print(f"Features Per Frame: {data.shape[1]} (Should be exactly 258)")
    print(f"Data Type: {data.dtype}")
    print(f"Contains NaNs/Missing values: {np.isnan(data).any()}")
except Exception as e:
    print(f"Error loading file: {e}")
