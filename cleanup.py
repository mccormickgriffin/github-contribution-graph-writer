import os
import shutil

def delete_folders_starting_with(prefix):
    # Get the list of items in the current directory
    items = os.listdir()

    # Filter folders that start with the specified prefix
    folders_to_delete = [item for item in items if os.path.isdir(item) and item.startswith(prefix)]

    # Delete each folder
    for folder in folders_to_delete:
        full_path = os.path.join(os.getcwd(), folder)
        try:
            shutil.rmtree(full_path)  # Use shutil.rmtree to delete a non-empty directory
            print(f"Deleted folder: {folder}")
        except Exception as e:
            print(f"Error deleting folder {folder}: {e}")

if __name__ == "__main__":
    prefix_to_delete = "gcgw"
    delete_folders_starting_with(prefix_to_delete)