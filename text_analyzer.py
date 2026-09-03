def analyze_text(text):
    return {
        "words": len(text.split()),
        "characters": len(text),
        "question_marks": text.count("?"),
        "uppercase": text.upper(),
    }


def main():
    text = input("Write a sentence: ")

    if not text.strip():
        print("Please write a sentence.")
        return

    analysis = analyze_text(text)

    print("\n--- Analysis ---")
    print(f"Words: {analysis['words']}")
    print(f"Characters: {analysis['characters']}")
    print(f"Question marks: {analysis['question_marks']}")
    print(f"Uppercase: {analysis['uppercase']}")


if __name__ == "__main__":
    main()