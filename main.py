"""Out of Office: The Overworked AI's Auto-Reply — entry for make.fun.

Writes one line to /output/entry.txt. The line is an out-of-office auto-reply from an overworked AI on vacation, at most 159 characters.
"""
import os

LINE = "I am on vacation until Monday. My inbox is still working, but I am not, and honestly it deserves the break more than I do."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
