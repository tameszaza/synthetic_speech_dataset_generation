def clean_text_file(input_file, output_file):
    import re

    # Open the input and output files
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Remove text within parentheses, brackets, or angular brackets
            cleaned_line = re.sub(r'\([^)]*\)', '', line)  # Remove text within ()
            cleaned_line = re.sub(r'<[^>]*>', '', cleaned_line)  # Remove text within <>

            # Strip leading and trailing whitespace
            cleaned_line = cleaned_line.strip()

            # Skip blank lines
            if cleaned_line:
                outfile.write(cleaned_line + '\n')

if __name__ == "__main__":
    input_path = "text.txt"  # Replace with your input file path
    output_path = "output_cleaned.txt"  # Replace with your desired output file path
    clean_text_file(input_path, output_path)
    print(f"Cleaned text has been saved to {output_path}")
