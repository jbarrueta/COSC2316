# Name: Jorge Barrueta, Alejandro Lopez
# Date: 12/02/19
# Course: COSC 2316 Fall 2019 (Dr. Shebaro)
# Program Description:

######### Algorithm/Psuedocode ########

# 1. define a Student Class, with the needed methods (Ex: average)
# 2. write a toString of the class to write into the text file
# 3. when the program begins, read the text files that exist (users.txt, learn.txt)
# 4. for each user in user.txt create a new instance of a Student. Save each into a users list.
# 5. save each translation into a dictionary - learnDict
# 6. save each key of the learnDict into a list
# 7. begin the menu, which includes Learn, Test, Leaderboard
# 8. if Learn is pressed, step though the learn dictionary and present the key. Once the user presses
#   enter show the value, the next enter will go to the next key.
# 9. if Test is pressed, the user will be asked to either create a new Student instance or sign into a previous one
# 10. a function will randomly select 5 keys from the dictionary, the user will be displayed the key and must enter the
#     equivalent to the value.
# 11. if correct, the instance correct will go up as well as total, if wrong, wrong will go up one as well as total
# 12. Leaderboard will sort the list of users based on total correct, and display the top five.
# 13. Exit will end the program, saving the changes in users to the text file.


############# Python Code #############

class Student:
    def __init__(self, name, average, correct, wrong, total):
        self.name = name
        self.average = average
        self.correct = correct
        self.wrong = wrong
        self.total = total

    def __init__(self, name):
        self.name = name
        self.average = 0
        self.correct = 0
        self.wrong = 0
        self.total = 0

# Function Description:
# Precondition:
# Postcondition:


# Driver Program


#     def transcribe(self,DNA):
#         self.DNA = DNA.upper()
#         lines = self.file.readlines()
#         dict = {}
#         for i in lines:
#             # print(i)
#             i = i.strip("\n")
#             i = i.strip(" ")
#             i = i.split()
#             for x in i[3:]:
#                 newV = i[1]
#                 newK = x
#                 dict[newK] = newV
#         # print(dict)
#         if len(self.DNA) % 3 == 0:
#             codon = [self.DNA[letter:letter+3] for letter in range(0,len(self.DNA),3)]
#             for y in codon:
#                 if y == "ATG":
#                     start=codon.index("ATG")
#                     cleanCodon=codon[start:]
#                     dict["ATG"]="Met"
#             try:
#                 for h in cleanCodon:
#                     if h == 'TAG' or h == "TAA" or h == 'TGA':
#                         stop=cleanCodon.index(h)
#                         fineCodon = cleanCodon[:stop+1]
#                         break
#
#
#                 for t in fineCodon:
#                     print(dict[t],end=':')
#
#             except UnboundLocalError:
#                 print("The DNA string does not have a start or stop codon. ")
#             except KeyError:
#                 print("The DNA string after these codons did not consists of only C,A,T, or G characters.")
#         else:
#             print("Length of DNA string must be a multiple of 3.")
#
#
# def main():
#     DNA = "CATATGACAGATATGACAGATACAGATACAGGTCAGATCAGATTATAA"
#     file = open("codonTable.txt")
#     t = Transcriber(file)
#     t.transcribe(DNA)
# main()
