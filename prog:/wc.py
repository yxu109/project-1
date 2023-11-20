import argparse
import sys

def count_in_text(text):
    lines = text.splitlines()
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)
    return len(lines), word_count, char_count

def count_in_file(filename):
    try:
        with open(filename, 'r') as file:
            return count_in_text(file.read())
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return 0, 0, 0

parser = argparse.ArgumentParser(description="Word count utility")
parser.add_argument('files', nargs='*', help='Files to count')
parser.add_argument('-l', '--lines', action='store_true', help='Count lines')
parser.add_argument('-w', '--words', action='store_true', help='Count words')
parser.add_argument('-c', '--chars', action='store_true', help='Count characters')

args = parser.parse_args()

# Handling no flag as all flags
if not (args.lines or args.words or args.chars):
    args.lines, args.words, args.chars = True, True, True

total_lines, total_words, total_chars = 0, 0, 0

if not args.files:
    # No files provided, read from STDIN
    input_text = sys.stdin.read()
    lines, words, chars = count_in_text(input_text)
else:
    # Files are provided
    for filename in args.files:
        lines, words, chars = count_in_file(filename)
        total_lines += lines
        total_words += words
        total_chars += chars

        counts = []
        if args.lines:
            counts.append(str(lines))
        if args.words:
            counts.append(str(words))
        if args.chars:
            counts.append(str(chars))

        print("\t".join(counts) + f"\t{filename}")

if len(args.files) > 1:
    total_counts = []
    if args.lines:
        total_counts.append(str(total_lines))
    if args.words:
        total_counts.append(str(total_words))
    if args.chars:
        total_counts.append(str(total_chars))

    print("\t".join(total_counts) + "\ttotal")
