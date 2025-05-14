from class1 import student

student1 = student("john", 5.00, "one")
student2 = student("cat", 4.00, "two")
student2 = student("rat", 4.00, "two")
for i in range(10):
    with open('hehe.txt' , 'w') as f:
        f.write(student1.roll)
