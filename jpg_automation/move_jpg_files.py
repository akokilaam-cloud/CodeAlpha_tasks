import os
import shutil

# Step 1: Define source and destination folders
source_folder = "source_images"
destination_folder = "jpg_files"

# Step 2: Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Step 3: Loop through all files in source folder
for file_name in os.listdir(source_folder):

    # Step 4: Check if file is a .jpg image
    if file_name.lower().endswith(".jpeg"):

        # Step 5: Build full file paths
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        # Step 6: Move the file
        shutil.move(source_path, destination_path)

# Step 7: Completion message
print("All .jpg files have been moved successfully.")
