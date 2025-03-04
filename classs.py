from os import access

famous_person = "Albert Einstein"
message = f'\t{famous_person} once said, "A person who never made a\n\tmistake never tried anything new."\n'
print(message)


class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def sit(self):
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		print(f"{self.name} is rolled over.!\n")

dog1 = Dog("Rocky", 3)
dog1.sit()
dog1.roll_over()


class Person:
	def __init__(self, name, gender, age):
		self.name = name
		self.gender = gender
		self.age = age

personOne = Person("Nagesh", "Male", 31)
personTwo = Person("Teju", "Female", 25)

class Email:
	def __init__(self, date, subject, body, to, from_whom):
		self.date = date
		self.subject = subject
		self.body = body
		self.to = to
		self.from_whom = from_whom

	def sendEmail(self):
		print(f"Email started sending...\nEmail sent to {self.to}!\n")

nagesh = Email('03/03', 'Leave Letter', 'Unable to come office', 'nagesh@gmail.com', 'teju09@gmail.com')
nagesh.sendEmail()

infosys = Email('04/03', 'Walk-in Interview', 'I am attending interview for SW', 'infosys-hr@infosys.com', 'teju09@gmail.com')
infosys.sendEmail()


# stimulate Student class

class Student:
	def __init__(self, name, roll_no, which_class, maths, science, english, hindi, kannada, social):
		self.name = name
		self.roll_no = roll_no
		self.which_class = which_class
		self.maths = maths
		self.science = science
		self.english = english
		self.hindi = hindi
		self.kannada = kannada
		self.social = social

	def get_total(self):
		return self.maths + self.science + self.english + self.hindi + self.kannada + self.social

	def get_percentage(self):
		total = self.get_total()
		max_marks = 625
		percentage = (total / max_marks) * 100
		print(f"{self.name} scored {total} total marks.\nPercentage = {percentage:.2f}%")
		return total, percentage

	def get_result(self):
		total, percentage = self.get_percentage()
		if total < 400:
			print(f"{self.name} Failed.!!")
		else:
			print(f"{self.name} Passed 'IX' Class & Promoted to 'X' Class.\nAll the Best.!!\n")

student_1 = Student("Rakesh", "6100", "IX", 40, 30, 35, 35, 45, 85)
student_1.get_result()

# student_2 = Student("Kushi Raj", "6059", "IX", 89, 90, 100, 100, 123, 98)
# student_2.get_percentage()
# student_2.get_result()
#
# student_3 = Student("Ankitha M", "6001", "IX", 75, 79, 95, 93, 106, 85)
# student_3.get_percentage()
# student_3.get_result()


class Rectangle:
	def __init__(self, length,breadth):
		self.length = length
		self.breadth = breadth

	def find_area(self):
		return self.length * self.breadth


values = Rectangle(10, 20)
print("The area of a Rectangle is:",values.find_area(),"cms")


class Students:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades  # List of grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

s1 = Students("John", [90, 80, 85, 95])
print(f"{s1.name}'s Average Grade:", s1.average_grade())



class Bank_account:
	def __init__(self, balance=0):
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
		print(f"Deposited: Rs.{amount}, New Balance: Rs.{self.balance}")

	def withdraw(self, amount):
		if amount > self.balance:
			print("Insufficient funds")
		else:
			self.balance -= amount
			print(f"Withdrawn: Rs.{amount}, New Balance: Rs.{self.balance}")

account = Bank_account(1000)
account.deposit(500)
account.withdraw(600)


