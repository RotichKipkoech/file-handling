def create_and_write_file():
    """Create a new file and write initial content."""
    try:
        # Open the file in write mode ('w')
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is the first line.\n")
            file.write("This is line 2 with a number: 12345\n")
            file.write("This is line 3 with some more text.\n")
        print("Initial content written to my_file.txt.")
    
    except PermissionError:
        print("Error: You do not have permission to write to the file.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        print("File creation and writing process complete.")

def read_and_display_file():
    """Read the contents of the file and display them."""
    try:
        # Open the file in read mode ('r')
        with open("my_file.txt", "r") as file:
            content = file.read()  # Read the entire file content
            print("\nFile contents:")
            print(content)
    
    except FileNotFoundError:
        print("Error: The file my_file.txt was not found.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        print("File reading process complete.")

def append_to_file():
    """Append new lines to the existing file."""
    try:
        # Open the file in append mode ('a')
        with open("my_file.txt", "a") as file:
            file.write("Appended line 1: Adding new content.\n")
            file.write("Appended line 2: More new text!\n")
            file.write("Appended line 3: Even more added.\n")
        print("New content appended to my_file.txt.")
    
    except PermissionError:
        print("Error: You do not have permission to append to the file.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        print("File appending process complete.")

def main():
    """Main function to control the script's workflow."""
    # Step 1: Create file and write initial content
    create_and_write_file()

    # Step 2: Read the file and display its contents
    read_and_display_file()

    # Step 3: Append new content to the file
    append_to_file()

    # Step 4: Read and display the updated file contents
    read_and_display_file()

if __name__ == "__main__":
    main()
