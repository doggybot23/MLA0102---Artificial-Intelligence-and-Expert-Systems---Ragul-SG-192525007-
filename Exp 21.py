patterns = {
    "circle": "Round shape",
    "square": "Four equal sides",
    "triangle": "Three sides",
    "rectangle": "Four sides"
}

pattern = input("Enter pattern: ").lower()

if pattern in patterns:
    print("Pattern Recognized:", pattern)
    print("Description:", patterns[pattern])
else:
    print("Pattern not recognized")
