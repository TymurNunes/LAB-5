roman = input("Enter Roman number: ")

numbers = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

result = 0

for i in range(len(roman)):
    if i + 1 < len(roman) and numbers[roman[i]] < numbers[roman[i + 1]]:
        result -= numbers[roman[i]]
    else:
        result += numbers[roman[i]]

print(f"The integer value of the Roman number is: {result}")