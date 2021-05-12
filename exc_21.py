if __name__ == "__main__":
    filename = input("specify filename: ")
    open_file = open(filename + ".txt", "w")
    open_file.write("hahahahahahahhahahahahahahah")
    open_file.close()