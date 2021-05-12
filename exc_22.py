if __name__ == "__main__":
    with open('Training_01.txt', 'r') as open_file:
        file_text = open_file.read().rstrip()
        category_dictionary = {}
        
    for line in file_text.split('\n'):
        cat = line.split("/")[2]
        if cat not in category_dictionary:
            category_dictionary[cat] = 1
        else :
            category_dictionary[cat] += 1
    print(category_dictionary)