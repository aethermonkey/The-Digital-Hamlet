import os

# Directory where the cheat sheets are located
directory = os.path.dirname(os.path.realpath(__file__))

# Name of the consolidated cheat sheet
cheat_sheet = "cheat_sheets.md"

# Open the consolidated cheat sheet in write mode
with open(os.path.join(directory, cheat_sheet), 'w') as outfile:
    # Loop over all files in the directory
    for filename in os.listdir(directory):
        # If the file is a markdown file and it's not the consolidated cheat sheet
        if filename.endswith(".md") and filename != cheat_sheet:
            # Open the file in read mode
            with open(os.path.join(directory, filename), 'r') as infile:
                # Write the contents of the file to the consolidated cheat sheet
                outfile.write(infile.read())
                # Add a newline to separate the contents of the different cheat sheets
                outfile.write("\n")
