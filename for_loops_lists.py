# Find the total num

prices = [10, 20, 30, 40, 50 , 100, 150, 23, 987, 456, 34]
total = 0

for price in prices:
	total += price
print(f"Your Total price is: {total}")


# create "L" shape using loops
numbers = [1,1,1,1,1,7]
for num in numbers:
	output = ""
	for i in range(num):
		output += 'x'
	print(output)


# finding largest num in lst
nums = [1013, 20, 307, 40, 50 , 100, 150, 999, 987, 456, 34]
largest_num = nums[0]
for num in nums:
	if i > largest_num:
		largest_num = num
print(f"Largest num in the list is: {largest_num}")

# matrix

matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
for row in matrix:
	for item in row:
		print(item)


