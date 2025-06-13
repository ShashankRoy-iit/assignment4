try:
    file1 = open('sample.txt', 'r+')
    print("Reading file content...")
    l1 =file1.readlines(1)
    l2 = file1.readlines()
    print("line1:",l1,"\nline2:",l2)
except FileNotFoundError:
    print("The file 'sample.txt' was not found")

finally:
    print("Thank You")