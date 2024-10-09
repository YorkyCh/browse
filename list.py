import os


def list(folder_path):
    try:
        files = os.listdir(folder_path)

        if not files:
            print(f"The folder '{folder_path}' is empty.")

        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Error: The folder '{folder_path}' does not exist.")

    except PermissionError:
        print(f"Error: Permission denied to access '{folder_path}'.")
