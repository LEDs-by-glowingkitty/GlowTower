import os
import glob

# Define the directory to start from
start_dir = './elec/src/'

# Open the output markdown file
with open('pcbs_code.md', 'w') as md_file:
    # Walk through the directory
    for dirpath, dirnames, filenames in os.walk(start_dir):
        # Find all .ato files in the current directory
        for filename in glob.glob(os.path.join(dirpath, '*.ato')):
            # Write the relative file path to the markdown file
            md_file.write(f'## File: {os.path.relpath(filename, start_dir)}\n\n')
            # Open the .ato file
            with open(filename, 'r') as ato_file:
                # Write the content of the .ato file to the markdown file
                md_file.write(ato_file.read())
                md_file.write('\n\n')