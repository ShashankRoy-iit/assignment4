#user input appending in a file
u = input("Enter text to write to the file: ")
try:
    f1 = open("output.txt", 'w')
    write = f1.write(u)
    print("Data sucessfully written to output.txt.")
    f1.close()

    f1 = open("output.txt",'a')
    a = input("Enter additional text to append: ")
    apnd = f1.write("\n" + a)
    print("Data successfully appended.\n")
    f1.close()

    f1 = open("output.txt", 'r+')
    readf = f1.readlines(1)
    l2 = f1.readlines(2)
    print("Final content of output.txt:\n", readf,"\n",l2)
    f1.close()

except FileNotFoundError:
    print("The file'Output.txt' was not found.")

finally:
    print("Thank You")