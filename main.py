import  tkinter as TK
import PIL
import pyperclip
import rich
import re


def GetWords(text):
    words = re.findall(r'\w+\b', text.lower())
    return words


def CalculateEmphasis(words):
    def CalculateEmphasis(words):
        emphasis_data = []

        for word in words:

            length = len(word)

            # Determine the number of characters to emphasize based on word length
            if length <= 4:
                emphasize_count = 1  # Short words (3–4 characters) emphasize 1 letter
            elif 5 <= length <= 7:
                emphasize_count = 2  # Medium words (5–7 characters) emphasize 2 letters
            else:
                emphasize_count = 3  # Long words (8+ characters) emphasize 3 letters


            emphasis_data.append((word, emphasize_count))

        return emphasis_data



