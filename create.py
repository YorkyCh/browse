import os


def create(name):
    sessions_dir = "./sessions"

    if not os.path.exists(sessions_dir):
        try:
            os.makedirs(sessions_dir)
            print(f"Created directory: {sessions_dir}")
        except OSError as e:
            print(f"Error: Unable to create directory '{sessions_dir}' : {e}")
            return

    try:
        with open(f"./sessions/{name}.csv", "w") as _:
            pass
        print("success")
    except IOError:
        print(f"Error: Unable to create file '{name}'")
