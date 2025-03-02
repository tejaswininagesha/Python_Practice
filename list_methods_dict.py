# list functions

# 1. append
num = [20, 30, 45, 99, 40, 35]
num.append(123)
print(num)

# 2. insert
num = [20, 30, 45, 99, 40, 35]
num.insert(3, 86)
print(num)

# 3. remove
num = [20, 30, 45, 99, 40, 35]
num.remove(99)
print(num)

# 4. clear
num = [20, 30, 45, 99, 40, 35]
print(num)
num.clear()
print(num)

# 5. pop (removes last item)
num = [20, 30, 45, 99, 40, 35]
num.pop()
print(num)

# 5. pop (removes given index item)
num = [20, 30, 45, 99, 40, 35]
num.pop(0)
print(num)

# 6. check whether the item is in list or not (True or False)
num = [20, 30, 45, 99, 40, 35]
print(90 in num)

# 7. Count
num = [20, 30, 45, 99, 40, 35, 30, 45, 99 , 35, 89, 45, 35]
print(num.count(35))

#  8. Sort(ascending order)

num = [20, 99, 40, 30, 35, 89, 45]
num.sort()
print(num)

# 9. Sort(descending order)

num = [20, 99, 40, 30, 35, 89, 45]
num.sort()
num.reverse()
print(num)


#  10 copy (won't affect if you made changes in original)
num = [20, 99, 40, 30, 35, 89, 45]
num_2 = num.copy()
print(num_2)
num.remove(99)
print(num)

# 11. set (removes duplicate no's)

num = [20, 30, 45, 99, 40, 35, 30, 45, 99 , 35, 89, 45, 35]
print(num)
print(set(num))

# remove duplicates
numbers = [20, 30, 45, 99, 40, 35, 30, 45, 99 , 35, 89, 45, 35]
unique = []
print(numbers)

for number in numbers:
	if number not in unique:
		unique.append(number)
		unique.sort()
print(f"New list without duplicates :{unique}")


# DICTIONARIES

student_profile = {
	"Name": "Tejaswini H D",
	"Age" : 25,
	"Gender": "Female",
	"Qualification": "B.E",
	"is_married": True
}

student_profile["Place"] = "Kolar"
student_profile["age"] = "26"
print(student_profile)

# digits to words
phone_num = input("Enter no: ")

digits_in_words = {
	"1": "One",
	"2": "Two",
	"3": "Three",
	"4": "Four",
	"5": "Five"
}

output = ""
for char in phone_num:
	output += digits_in_words.get(char, "*") + " "
print(f"{phone_num} = {output}")

# Emojis convertor

message = input(">: ")

words = message.split(" ")
emojis = {
	"143": "❤️",
	":)": "😀",
	":(": "😔",
	"(!)": "🎁"
}

output = ""
for word in words:
	output += emojis.get(word, word) + " "
print(output)