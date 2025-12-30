# count vowels , numbers in string

def count_vowels_digits(s):
    vowels = "aeiouAEIOU"
    vowelCount = sum(1 for char in s if char in vowels)
    digitCount = sum(1 for char in s if char.isdigit())
    return vowelCount, digitCount

v,d = count_vowels_digits("Rohit Sharma has scored over 20000 runs and played over 500 international matches")
print(f"Vowels: {v}, Digits: {d}")