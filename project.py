# Name: Jorge Barrueta, Alejandro Lopez
# Date: 12/02/19
# Course: COSC 2316 Fall 2019 (Dr. Shebaro)
# Program Description:

######### Algorithm/Psuedocode ########

# 1. define a Student Class, with the needed methods (Ex: average)
# 2. write a toString of the class to write into the text file
# 2.1. Create function that reads a file and returns list of lines
# TODO 3. when the program begins, read the text files that exist (users.txt, learn.txt)
# 4. for each user in user.txt create a new instance of a Student. Save each into a users list.
# TODO 5. save each translation into a dictionary - learnDict
# TODO 6. save each key of the learnDict into a list
# TODO 7. begin the menu, which includes Learn, Test, Leaderboard
# TODO 8. if Learn is pressed, step though the learn dictionary and present the key. Once the user presses
#         enter show the value, the next enter will go to the next key.
##### 9. if Test is pressed, the user will be asked to either create a new Student instance or sign into a previous one
##### 10. a function will randomly select 5 keys from the dictionary, the user will be displayed the key and must enter
#####     the equivalent to the value.
##### 11. if correct, the instance correct will go up as well as total, if wrong, wrong will go up one as well as total
# TODO 12. Leaderboard will sort the list of users based on total correct, and display the top five.
# TODO 13. Exit will end the program, saving the changes in users to the text file. (format: average correct wrong total name\n)


############# Python Code #############

class Student:
    def __init__(self, name, correct=0, wrong=0, total=0):
        self.name = name
        self.correct = correct
        self.wrong = wrong
        self.total = total
        self.average = 0 if self.total <= 0 else self.correct / self.total

    def __str__(self):
        return self.average, self.correct, self.wrong, self.total, self.name


# Function Description: readFile function will read a file and save it into a list, if text file doesn't exits, it will create it
# Precondition: readFile will receive a text file
# Postcondition: will return a list of file lines
def readFile(txtFile):
    txtList = []
    try:
        with open(txtFile, "r") as inFile:
            txtList = inFile.readlines()
    except IOError:
        createdFile = open(txtFile, "w")
        createdFile.close()
    return txtList


# Function Description: extract users from the text file users.txt
# Precondition: must receive a list of users from the text file, a user by line
# Postcondition: will return a list of Student instances
def extractUsers(list1):
    users = []
    count = 0
    for user in list1:
        splitUser = user.split()
        correctFormat = True
        print(splitUser)
        try:
            avg = float(splitUser[0])
            print(avg)
            correct = int(splitUser[1])
            print(correct)
            wrong = int(splitUser[2])
            print(wrong)
            total = int(splitUser[3])
            print(total)
            name = " ".join(splitUser[4:])
            users.append(Student(name.strip(), correct, wrong, total))
        except ValueError:
            count += 1
    print("WARNING:", count, "could not be read and were skipped, please fix text file to be in the correct format")
    return users


# Driver Program
usersList = readFile("users.txt")
print(usersList)
users = extractUsers(usersList)
# print(users[1].__str__())
