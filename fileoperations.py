import os
import sys

def count_search_text_in_file(file_path, search_text):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content.lower().count(search_text.lower())
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

def search_text_in_files(directory, search_text):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            count = count_search_text_in_file(file_path, search_text)
            if count > 0:
                print(f"File: {file_path} | Search text '{search_text}' found {count} times.")

def file_operations():
    new_file = 'sample_output.txt'
    content = "This is a sample file for demonstrating file write and read operations."
    
    try:
        with open(new_file, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Content written to {new_file}")
    except Exception as e:
        print(f"Error writing to {new_file}: {e}")
    
    try:
        with open(new_file, 'r', encoding='utf-8') as file:
            print(f"Content of {new_file}:")
            print(file.read())
    except Exception as e:
        print(f"Error reading {new_file}: {e}")
    
    if os.path.exists(new_file):
        print(f"{new_file} exists.")
    else:
        print(f"{new_file} does not exist.")

    renamed_file = 'renamed_sample_output.txt'
    try:
        os.rename(new_file, renamed_file)
        print(f"File renamed to {renamed_file}")
    except Exception as e:
        print(f"Error renaming file: {e}")



if len(sys.argv) != 3:
    print("Usage: python script.py <directory_path> <search_text>")
    sys.exit(1)

directory = sys.argv[1]
search_text = sys.argv[2]

print(f"\nSearching for '{search_text}' in all files within '{directory}'...\n")
search_text_in_files(directory, search_text)

print("\nDemonstrating additional file operations...")
file_operations()
