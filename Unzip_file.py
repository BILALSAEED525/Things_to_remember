# This recreates the folder
!mkdir -p /content/dataset

# This unzips the exact file from your Google Drive into the Colab temporary storage
!unzip -q "/content/drive/MyDrive/psl_full_site_videos.zip" -d "/content/dataset/"
