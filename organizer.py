import os
import shutil

def organize_files(folder_path="messy_folder"):
    """
    Organizes files in the specified folder based on their extension:
      - .jpg -> Images/
      - .pdf -> Documents/
      - .txt -> TextFiles/
    """
    # Mapping file extensions to destination folder names
    destination_map = {
        ".jpg": "Images",
        ".pdf": "Documents",
        ".txt": "TextFiles",
    }

    if not os.path.exists(folder_path):
        print(f"Directory '{folder_path}' does not exist.")
        return

    # Scan through all entries in the target directory
    for item in os.listdir(folder_path):
        src_path = os.path.join(folder_path, item)

        # Process only files (ignore subdirectories)
        if os.path.isfile(src_path):
            _, ext = os.path.splitext(item)
            ext = ext.lower()

            if ext in destination_map:
                dest_folder_name = destination_map[ext]
                dest_dir = os.path.join(folder_path, dest_folder_name)

                # Create the target category folder if it doesn't already exist
                os.makedirs(dest_dir, exist_ok=True)

                # Destination path inside the category folder
                dest_path = os.path.join(dest_dir, item)

                # Move the file
                shutil.move(src_path, dest_path)
                print(f"Moved: '{item}' -> '{dest_folder_name}/'")

if __name__ == "__main__":
    organize_files()

