import os
import shutil

source_folder = r"D:\TEJA SREE\codealpha_tasks\TaskAutomation\images"
destination_folder = r"D:\TEJA SREE\codealpha_tasks\TaskAutomation\moved_images"

# Make sure destination exists
os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    source_path = os.path.join(source_folder, filename)
    destination_path = os.path.join(destination_folder, filename)

    # Only move files (not subfolders)
    if os.path.isfile(source_path):
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")
