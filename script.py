import os

def concatenate_python_files(directory_path, output_file):
    # Open the output file in append mode
    with open(output_file, 'a', encoding='utf-8') as outfile:
        # Walk through the directory
        for root, dirs, files in os.walk(directory_path):
            # Filter for .py files
            python_files = [f for f in files if f.endswith('.py')]
            
            # Process each Python file
            for file_name in python_files:
                full_path = os.path.join(root, file_name)
                
                try:
                    # Read the content of the Python file
                    with open(full_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        
                    # Write the file information and content to the output file
                    outfile.write(f"\nDirectory: {root}\n")
                    outfile.write(f"Filename: {file_name}\n")
                    outfile.write("::START::\n")
                    outfile.write(content)
                    outfile.write("\n::END OF FILE::\n")
                    outfile.write("\n" + "="*50 + "\n")  # Separator between files
                except Exception as e:
                    print(f"Error processing {full_path}: {str(e)}")

# Example usage
if __name__ == "__main__":
    directory_to_scan = r"/Users/maxmahlke/Documents/your-dir"  # Current directory, change this to your target directory
    output_file_path = "combined_python_files.txt"
    concatenate_python_files(directory_to_scan, output_file_path)