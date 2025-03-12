def read_and_write_file():
    """Reads a file and writes a modified version to a new file with error handling."""
    try:
        # Ask the user for a filename
        input_filename = input("Enter the filename to read: ")
        
        # Open and read the file
        with open(input_filename, "r") as file:
            content = file.readlines()

        # Modify the content (e.g., convert text to uppercase)
        modified_content = [line.upper() for line in content]

        # Ask for output filename and write the modified content
        output_filename = "modified_" + input_filename
        with open(output_filename, "w") as file:
            file.writelines(modified_content)

        print(f"File has been successfully modified and saved as '{output_filename}'")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_write_file()
