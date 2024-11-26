def modify_file_content(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, "r") as infile:
            content = infile.read()  # Read the content of the file
        
        # Modify the content (convert to uppercase in this example)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)
        
        print(f"File has been successfully modified and saved to '{output_file}'!")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for the input file name and the output file name
input_file = input("Enter the name of the file to read: ")
output_file = input("Enter the name of the file to save the modified content: ")

# Call the function
modify_file_content(input_file, output_file)
