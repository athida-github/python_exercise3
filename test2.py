import os
from collections import Counter

def get_file_statistics(file_content):
    """Analyze the content of the file and return statistics."""
    lines = file_content.splitlines()
    words = [word.strip(".,!?;:").lower() for line in lines for word in line.split()]  # Clean and normalize words

    num_lines = len(lines)
    num_words = len(words)
    num_characters = len(file_content)
    unique_words = len(set(words))

    # Find the longest word
    longest_word = max(words, key=len) if words else ""

    # Find the most frequent word
    word_frequencies = Counter(words)
    most_frequent_word, most_frequent_count = word_frequencies.most_common(1)[0] if word_frequencies else ("", 0)

    # Top 5 most frequent words
    top_5_words = word_frequencies.most_common(5)

    return {
        "Number of lines": num_lines,
        "Number of words": num_words,
        "Number of unique words": unique_words,
        "Number of characters": num_characters,
        "Longest word": longest_word,
        "Most frequent word": f"{most_frequent_word} (appears {most_frequent_count} times)",
        "Top 5 most frequent words": top_5_words,
    }

def save_statistics_to_file(statistics, output_file):
    """Save statistics to an output file."""
    with open(output_file, "w") as file:
        for key, value in statistics.items():
            if key == "Top 5 most frequent words":
                file.write(f"{key}:\n")
                for word, count in value:
                    file.write(f"  {word}: {count} times\n")
            else:
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
        if key == "Top 5 most frequent words":
            print(f"{key}:")
            for word, count in value:
                print(f"  {word}: {count} times")
        else:
            print(f"{key}: {value}")

    # Generate output file name
    base_name, ext = os.path.splitext(input_file)
    output_file = f"{base_name}-statistics{ext}"

    # Save statistics to the output file
    save_statistics_to_file(statistics, output_file)

if __name__ == "__main__":
    main()
