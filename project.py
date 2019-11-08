class Student:
    def __init__(self,name, average, correct, wrong, total):
        self.name = name
        self.average = average
        self.correct = correct
        self.wrong = wrong
        self.total = total








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
