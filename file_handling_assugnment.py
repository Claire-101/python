def write_to_file(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with text and numbers: 9876\n")
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
    except PermissionError:
        print(f"Error: Permission denied to write to {file_name}.")
    else:
        print(f"{file_name} created and written successfully.")

def read_and_display(file_name):
    try:
        with open(file_name, 'r') as file:
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
    except PermissionError:
        print(f"Error: Permission denied to read {file_name}.")

def append_to_file(file_name):
    try:
        with open(file_name, 'a') as file:
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
    except PermissionError:
        print(f"Error: Permission denied to append to {file_name}.")
    else:
        print("Content appended successfully.")

if __name__ == "__main__":
    file_name = "my_file.txt"
    write_to_file(file_name)
    read_and_display(file_name)
    append_to_file(file_name)
    read_and_display(file_name)
