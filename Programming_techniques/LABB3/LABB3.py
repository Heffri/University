# LABB 3
# Sebastijan Babic
# 2024 - 02 - 06



## UPPGIFT 1 ##

# a) # 
def insert_in_sorted(x, sorted_list):
    # Iterate entire sorted_list
    for i in range(len(sorted_list)):
        if x < sorted_list[i]:
            # Insert x before sorted_list[i]
            sorted_list.insert(i, x)
            return sorted_list
    # If x larger than entire sorted_list, insert in the end
    sorted_list.append(x)
    return sorted_list

insert_in_sorted(-1, [0,2,2])


# b) #
def insertion_sort(my_list):
    sorted_list = []
    for x in my_list: # Iterate through my_list
        sorted_list = insert_in_sorted(x, sorted_list)
    return sorted_list

insertion_sort([-1,5,0,2])











## UPPGIFT 2 ##
def number_lines(f):
    # Open og file
    with open(f, 'r') as original_file:
        # Create and open new file
        with open(f'numbered_{f}', 'w') as numbered_file:
            # Iterate through every line in og file
            for line_number, line_content in enumerate(original_file):
                # Add row number
                numbered_file.write(f'{line_number} {line_content}')

number_lines('sommar.txt')






            
            
            




## UPPGIFT 3 ##

# a) #
def index_text(filename):
    index = {}
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file):
            for word in line.split():
                word = word.lower()
                if word not in index:
                    index[word] = {line_number}
                else:
                    index[word].add(line_number)
    # Convert sets back to lists if necessary
    for word in index:
        index[word] = list(index[word])
    return index

index = index_text('idas.txt')
print(index)


# b) #
def important_words(an_index, stop_words):
    # Make a list to save each words frequency
    word_frequencies = []

    # Remove stop_words and find frequencies
    for word, lines in an_index.items():
        if word not in stop_words:
            word_frequencies.append((word, len(lines)))

    # Sort based on frequency
    for i in range(len(word_frequencies)):
        for j in range(i + 1, len(word_frequencies)):
            if word_frequencies[i][1] < word_frequencies[j][1]:
                # Switch places 
                word_frequencies[i], word_frequencies[j] = word_frequencies[j], word_frequencies[i]

    # Find 5 first words with highest frequency
    top_words = [word for word, freq in word_frequencies[:5]]

    return top_words

sommar_index = index_text('idas.txt')
for w in important_words(sommar_index, ['och']):
    print(w)




# c) # FUNKAR EJ ?????
def main():
    stop_words = ['och', 'jag', 'som', 'det', 'för']  # Stop words

    while True:  # Loop for user if file doesnt exist
        filename = input("Ange en textfil: ")

        try:
            # Make index of file
            index = index_text(filename)
            # Find most important words
            important = important_words(index, stop_words)

            print("De viktigaste orden är:")
            for word in important:
                print(word)

            break 

        except FileNotFoundError:  # In case file does not exist
            print(f"Filen '{filename}' hittades inte. Försök igen.")

# if __name__ == "__main__":
#     main()

    
