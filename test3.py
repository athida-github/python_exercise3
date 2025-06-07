import os

def get_file_statistics(file_content):
    """Analyze the content of the file and return statistics."""
    lines = file_content.splitlines()
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_characters = len(file_content)
    return {
        "Number of lines": num_lines,
        "Number of words": num_words,
        "Number of characters": num_characters,
    }

def save_statistics_to_file(statistics, output_file):
    """Save statistics to an output file."""
    with open(output_file, "w") as file:
        for key, value in statistics.items():
            file.write(f"{key}: {value}\n")
    print(f"Statistics saved to {output_file}")

def main():
    # Ask user for the file name
    input_file = input("Enter the name of the text file to analyze: ")
    
    # Check if the file exists
    if not os.path.exists(input_file):
        print("The specified file does not exist. Please try again.")
        return

    # Read the file content
    with open(input_file, "r") as file:
        file_content = file.read()

    # Analyze the file content
    statistics = get_file_statistics(file_content)

    # Display the statistics
    print("\nFile Statistics:")
    for key, value in statistics.items():
        print(f"{key}: {value}")

    # Generate output file name
    base_name, ext = os.path.splitext(input_file)
    output_file = f"{base_name}-statistics{ext}"

    # Save statistics to the output file
    save_statistics_to_file(statistics, output_file)

if __name__ == "__main__":
    main()
