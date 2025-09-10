def write_file(filepath, lines):
    with open(filepath, 'w') as f:
        f.writelines(lines)