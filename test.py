def analyze_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Line count
        line_count = len(lines)

        # Word processing
        words = []
        for line in lines:
            words += line.strip().split()

        word_count = len(words)

        # Count most common word
        word_freq = {}
        for word in words:
            word = word.lower().strip(".,!?\"'")  # Normalize words
            word_freq[word] = word_freq.get(word, 0) + 1

        most_common = max(word_freq, key=word_freq.get) if word_freq else None

        return line_count, word_count, most_common

    except FileNotFoundError:
        print("❌ File not found.")
        return None
lines, words, common = analyze_file("sample.txt")
print(f"Lines: {lines}")
print(f"Words: {words}")
print(f"Most common word: {common}")
