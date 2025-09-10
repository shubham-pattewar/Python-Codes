def update_file(filepath, new_lines, position):
    """Insert new_lines into file after 'position' lines."""
    with open(filepath, 'r') as f:
        content = f.readlines()
    updated_content = content[:position] + new_lines + content[position:]
    with open(filepath, 'w') as f:
        f.writelines(updated_content)