text = input("Enter a sentence: ")
text = text.strip()
print("Clean Sentence:", text.title())

word = input("Enter a word to search: ")
print(f"word index: {text.find(word)}")

updated_text = text.replace(word, "python")
print(f"Updated sentence: {updated_text}")

