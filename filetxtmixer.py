import os
import re

# Folder where your TXT files are stored (set to your directory)
folder_path = "/storage/emulated/0/Pydroid3/"  # Change if needed

# Get all TXT files in the folder
txt_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".txt")]

# Set to store unique words
unique_words = set()

# Regular expressions
remove_numbers = re.compile(r'\d+')  # Remove numbers
valid_word_pattern = re.compile(r'^[a-zA-Z]+(-[a-zA-Z]+)?$')  # Only letters, allow single hyphen in between

# Read each file and process words
for file in txt_files[:4]:  # Open only the first 4 files
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            # Remove numbers first
            clean_line = remove_numbers.sub('', line)

            # Split into words
            words = clean_line.strip().split()

            for word in words:
                word = word.lower()  # Convert to lowercase

                # Remove if word starts/ends with '-'
                if word.startswith('-') or word.endswith('-'):
                    continue

                # Allow only words with letters or a single hyphen between letters
                if not valid_word_pattern.fullmatch(word):
                    continue

                # Remove words with spaces (e.g., "Water fall")
                if " " in word:
                    continue

                # Add to set (removes duplicates automatically)
                unique_words.add(word)

# Merge words into one file
output_file = os.path.join(folder_path, "merged_output.txt")

with open(output_file, "w", encoding="utf-8") as out:
    for word in sorted(unique_words):  # Sort for better readability
        out.write(word + "\n")

print(f"Process completed. Merged file saved as: {output_file}")