from pathlib import Path

# reading a text file
path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)