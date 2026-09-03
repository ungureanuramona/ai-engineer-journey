from collections import Counter


def analyze_text(text):
    return {
        "words": len(text.split()),
        "characters": len(text),
        "question_marks": text.count("?"),
        "uppercase": text.upper(),
    }


def find_common_words(text):
    cleaned_text = text.lower()

    for character in ".,!?":
        cleaned_text = cleaned_text.replace(character, "")

    words = cleaned_text.split()
    return Counter(words).most_common(3)


def main():
    text = input("Write a sentence: ")

    if not text.strip():
        print("Please write a sentence.")
        return

    analysis = analyze_text(text)
    common_words = find_common_words(text)

    print("\n--- Analysis ---")
    print(f"Words: {analysis['words']}")
    print(f"Characters: {analysis['characters']}")
    print(f"Question marks: {analysis['question_marks']}")
    print(f"Uppercase: {analysis['uppercase']}")

    print("\nMost frequent words:")
    for word, count in common_words:
        print(f"- {word}: {count}")


if __name__ == "__main__":
    main()