def change_file_handle(old_path, new_path):
    import os
    os.rename(old_path, new_path)