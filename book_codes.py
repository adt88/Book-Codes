file = open("/usercode/files/books.txt", "r")

#your code goes here
book_names = file.readlines()
# for names in book_names:
#     first_letter = names[0]
#     number = len(names)
#     print(first_letter + str(number))
alpha = (lambda x:[i[0] for i in x])(book_names)
numeric = (lambda x:[len(i) for i in x])(book_names)
codes = []

for i in range(len(book_names)):
    codes.append(alpha[i]+str(numberic[i]))

print(codes)



file.close()
 # read the lines of the file
 # write a loop for read each line
 # in the for loop take the first letter of the title (index)
 # then take the length of each line to use as the number
 # combine the the first letter and the number into a string
