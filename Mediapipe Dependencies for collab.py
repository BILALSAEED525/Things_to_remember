//for using media pipe in collab you must have to run this in new cell 

!pip uninstall -y tensorflow tensorboard keras
# 1. Clear out the broken packages
!pip uninstall -y mediapipe opencv-python opencv-python-headless protobuf

# 2. Install the EXACT matching versions
!pip install --no-cache-dir mediapipe==0.10.14 opencv-python-headless==4.8.0.74 protobuf==4.25.3
