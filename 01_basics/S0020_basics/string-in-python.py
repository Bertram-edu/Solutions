

string_1 = "word1"
string_2 = 'word2'  # I Python kan du benytte " eller ' for strings. Det er ligemeget.
print(string_1 + string_2)
print(string_1 + " " + string_2)

print("")

number1 = 5
number2 = 3
print(number1, "is greater than ", number2) # man kan ikke sette str og int sammen med +

print("")

string1 = "hej"
print(string1)

string1 += ", "
print(string1)

string1 += string1
print(string1)

print(string1.upper())

print(string1.isupper())

print(string1.replace("e", "ø"))

print(string1.split("j"))

string2 = "software"
print("h" in string2)

print(len(string2))

print(string2 + "\nNy linje!")

print(string2[0])

print(string2[3])

print(string2[-1])

print(string2[-4])

print(string2[2:])

print(string2[2:6])

