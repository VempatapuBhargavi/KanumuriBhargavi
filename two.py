import re


def find_python_occurrences(text):
    occurrences = re.findall(r'\bPython\b', text)
    return occurrences


# Example usage:
text = "Python is a widely used programming language. Python allows you to work quickly and integrate systems more effectively."
python_occurrences = find_python_occurrences(text)
print("Occurrences of 'Python':", python_occurrences)
