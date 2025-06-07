import os
from collections import Counter
def get_file(file_content):
   #Total number of lines.
   lines = file_content.splitlines()
   no_lines=len(lines)

   #Total number of words.
   words = file_content.split()
   no_words = len(words)

   #Total number of characters (including spaces).
   no_characters = len(file_content.replace("\n",""))

   #Number of unique words (case-insensitive).
   unique_words = [word.strip(".,!?;:@~#$").lower() for line in lines for word in line.split()]
   no_unique_words = len(set(unique_words))

   #The top 5 most frequent words and their counts.
   word_frequencies = Counter(unique_words)   
   five_words = word_frequencies.most_common(5)

   return{
      "Total number of lines ":no_lines,
      "Total number of words ":no_words,
      "Total number of characters ":no_characters,
      "Number of unique words (case-insensitive) ":no_unique_words,
      "The top 5 most frequent words and their counts ": five_words      
      }

def save_statistics_file(statistics_file,input_filename):
   output_file = input_filename[0:-5]+"-statistics.txt"
   with open(output_file, "w") as file:
        for key, value in statistics_file.items():
            if key == "The top 5 most frequent words and their counts ":
                file.write(f"{key}:\n")
                for word, count in value:
                    file.write(f"  {word}: {count} times\n")
            else:
                file.write(f"{key}: {value}\n")
        print(f"Statistics saved to {output_file}")


def main():
    input_filename = input("Enter file name with extention that suppose to annalyse: ")
    if os.path.exists(input_filename):
     print("file procrssing")
    else:
       print("File not found Error!")
    with open(input_filename, "r") as file:
        file_content = file.read()
        
        print(file_content)        
    
    # Analyzing the file content
    statistics_file = get_file(file_content)

    # Display the statistics
    print("\nFile Statistics:")
    for key, value in statistics_file.items():
        if key == "The top 5 most frequent words and their counts ":
            print(f"{key}:")
            #print(dict(value))
            #times = dict(statistics.values())
            for word, count in value:
                print(f"{word}:{count}")
                #print(f"{word}:{count} times")
        else:
            print(f"{key}: {value}")

    save_statistics_file(statistics_file,input_filename)  
    
       
if __name__ == "__main__":
   main()
