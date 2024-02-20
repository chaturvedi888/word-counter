def word_count(text):
    words = text.split()
    return len(words)
def main():
    text = input("Enter some text: ")
    print("Number of words:", word_count(text))
if __name__ == "__main__":
    main()
