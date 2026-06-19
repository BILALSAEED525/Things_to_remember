import cv2
import numpy as np
import os
from IPython.display import HTML
from base64 import b64encode

# 1. Point this to your NEW 154-feature .npy file
npy_path = "/content/drive/MyDrive/PSL_Landmarks_Numpy/15-beauty/631-bald_bald_1619523827_17575.npy.npy"
out_path = "/content/skeleton_verification.mp4"

# Load the data matrix
try:
    data = np.load(npy_path)
    print(f"Loaded data shape: {data.shape} (Features should be 154 now!)")
except Exception as e:
    print(f"Error loading file. Check the path! {e}")
    data = None

if data is not None:
    height, width = 480, 640

    # Setup the Video Writer (Playing at normal 30 FPS speed)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_path, fourcc, 30.0, (width, height))

    print("Generating 7-Point clean skeleton video... please wait.")

    # 2. Loop through every single frame in the numpy array
    for frame_data in data:
        # Create a blank black canvas
        blank_image = np.zeros((height, width, 3), dtype=np.uint8)

        # DRAW POSE (Green dots) - 7 points (x, y, z, visibility) = 28 values
        # We stop at index 28 instead of 132 because the legs are gone!
        for i in range(0, 28, 4):
            x, y = int(frame_data[i] * width), int(frame_data[i+1] * height)
            if x > 0 and y > 0: # Ignore zeroed-out coordinates
                cv2.circle(blank_image, (x, y), 4, (0, 255, 0), -1)

        # DRAW LEFT HAND (Blue dots) - 21 points (x, y, z) = 63 values
        # Starts right after the pose (index 28) and goes to 91
        for i in range(28, 91, 3):
            x, y = int(frame_data[i] * width), int(frame_data[i+1] * height)
            if x > 0 and y > 0:
                cv2.circle(blank_image, (x, y), 3, (255, 0, 0), -1)

        # DRAW RIGHT HAND (Red dots) - 21 points (x, y, z) = 63 values
        # Starts right after the left hand (index 91) and goes to 154
        for i in range(91, 154, 3):
            x, y = int(frame_data[i] * width), int(frame_data[i+1] * height)
            if x > 0 and y > 0:
                cv2.circle(blank_image, (x, y), 3, (0, 0, 255), -1)

        # Add the drawn frame to the video
        out.write(blank_image)

    out.release()
    print("Video generated successfully!")

    # 3. Compress and display the video right here in Colab
    os.system(f"ffmpeg -i {out_path} -vcodec libx264 -y /content/compressed_skeleton.mp4")

    try:
        mp4 = open('/content/compressed_skeleton.mp4','rb').read()
        data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
        display(HTML(f"""
        <video width=640 controls autoplay loop>
              <source src="{data_url}" type="video/mp4">
        </video>
        """))
    except Exception as e:
        print("Could not display video in browser. Click the folder icon on the left to download 'skeleton_verification.mp4'.")
