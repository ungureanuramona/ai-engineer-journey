text = input("Write a sentence: ")

word_count = len(text.split())
character_count = len(text)
question_count = text.count("?")
uppercase_text = text.upper()

print("\n--- Analysis ---")
print(f"Words: {word_count}")
print(f"Characters: {character_count}")
print(f"Question marks: {question_count}")
print(f"Uppercase: {uppercase_text}")