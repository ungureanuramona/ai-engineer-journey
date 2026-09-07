from collections import Counter


def normalize_text(text):
    cleaned_text = text.lower()

    for character in ".,!?":
        cleaned_text = cleaned_text.replace(character, "")

    return cleaned_text


def analyze_text(text):
    return {
        "words": len(text.split()),
        "characters": len(text),
        "question_marks": text.count("?"),
        "uppercase": text.upper(),
    }


def find_common_words(text):
    words = normalize_text(text).split()
    return Counter(words).most_common(3)


def find_longest_word(text):
    words = normalize_text(text).split()
    return max(words, key=len)


def count_vowels(text):
    vowels = "aeiou"
    vowel_count = 0

    for character in text.lower():
        if character in vowels:
            vowel_count += 1

    return vowel_count


def main():
    text = input("Write a sentence: ")

    if not text.strip():
        print("Please write a sentence.")
        return

    analysis = analyze_text(text)
    common_words = find_common_words(text)
    longest_word = find_longest_word(text)
    vowel_count = count_vowels(text)

    print("\n--- Analysis ---")
    print(f"Words: {analysis['words']}")
    print(f"Characters: {analysis['characters']}")
    print(f"Question marks: {analysis['question_marks']}")
    print(f"Uppercase: {analysis['uppercase']}")
    print(f"Vowels: {vowel_count}")

    print("\nMost frequent words:")
    for word, count in common_words:
        print(f"- {word}: {count}")

    print(f"\nLongest word: {longest_word}")


if __name__ == "__main__":
    main()