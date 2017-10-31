'''
Write a program to input ten book titles and author’s names then save them to a file named books.txt. 


Format:
TO KILL A MOCKINGBIRD		Lee, Harper


All book titles should be in upper case and the author’s name should be capitalized. 
'''

outfile = open("books.txt", "w")
for i in range(0, 10):
    title = input("Enter the title: ")
    authorFname = input("Enter the author first name: ")
    authorLname = input("Enter the author last name: ")
    output = title.upper() + "\t" + authorFname.capitalize() + ", " + authorLname.capitalize()
    print("\n" + output)
    outfile.write(output + "\n")

outfile.close()
