def count_letters(word, letters):
    """Counts occurrences of specific letters in a word."""
    total = 0
    for letter in letters:
        total += word.count(letter)
    return total

# Input names
name1 = input("Enter the first name: ").strip()
name2 = input("Enter the second name: ").strip()

# Combine names and convert to lowercase
combined_names = (name1 + name2).lower()

# Count occurrences for TRUE and LOVE
true_score = count_letters(combined_names, "true")
love_score = count_letters(combined_names, "love")

# Combine scores into a two-digit number
total_score = int(f"{true_score}{love_score}")

# Output the result
print(f"Your love score is {total_score}")

# Additional feedback based on score
if total_score > 90:
    print("You are a perfect match!")
elif 40 < total_score <= 90:
    print("You have a strong bond!")
else:
    print("It might not be a great match, but love works in mysterious ways!")
