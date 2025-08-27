def process_file():
    # Get input filename from user
    input_filename = input("Enter the input filename: ")
    output_filename = "output_" + input_filename

    try:
        # Attempt to open and read the input file
        with open(input_filename, 'r') as input_file:
            # Read all content
            content = input_file.read()

        # Modify content (converting to uppercase as an example)
        modified_content = content.upper()

        # Write modified content to new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"Success! File processed and saved as {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {str(e)}")
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    process_file()
