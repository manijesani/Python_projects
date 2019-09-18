#Main
#Welcome To Library you can issue any 3 books that you want
#1. Student Registration
    # Student Registration
    # Name age dep
    # Provide Student id
#2. Issue Book
    #Issue Books
    # Enter Your Student id and Verify your name
    # Dep --> book
    # add book in students dict and remove it from books dict
#3. Book Status
    #book Status
    # print aval books
#4. Student Status
    #Student Status
    # print Books issued to students
#5. Add Book
    # add books
    # Add books to books dict according to dep
#6. Exit
import pickle
import os
with open("libstudent.pkl","rb") as f:
    student = pickle.load(f)
with open("libbook.pkl","rb") as f:
    book = pickle.load(f)
idlist = list(student)
def studentreg():
    name = input("Enter Your Name --> ").strip().title()
    age = int(input("Enter Your Age --> ").strip())
    year = input("Enter your year with dep ").strip()
    sid = idlist[-1]+1
    idlist.append(sid)
    student.setdefault(sid,[[],[name,age,year]])
    print("Student Registration Completed\nStudent id --> ",sid)
    if input("Press Any key for Main Menu"):
        return 0
def issuebook():
    sid = int(input("Enter Your Student id").strip())
    if sid in student:
        print("Select any dep\n",*list(book))
        dep = input("Select any dep -->").strip().lower()
        print("Select any book\n",*book[dep])
        bk = input("Enter Book Name --> ").strip().lower()
        book[dep].remove(bk)
        student[sid][0].append(bk)
        print("Book issued")
    if input("Press Any key for Main Menu"):
        return 0
def bookstatus():
    for dep,books in book.items():
        print(f"{dep} --> ",*books)
    if input("Press Any key for Main Menu"):
        return 0
def studentstatus():
    for sid,sdetails in student.items():
        bk,sdet = sdetails
        print(f"{sid} ->",*sdet,bk)
    if input("Press Any key for Main Menu"):
        return 0
def addbooks():
    print("Select any dep\n",*list(book))
    dep = input("Select any dep -->").strip().lower()
    name = input("Enter Book name").strip().lower()
    book[dep].append(name)
    print("Book added")
    if input("Press Any key for Main Menu"):
        return 0
def main():
    print("Welcome to National College Library")
    opt = int(input("1.Student Registration\n2.Issue Books\n3.Book Status\n4.Student Status\n5.Add Books\n6.Exit\nEnter Your Choice --> ").strip())
    if opt == 1:
        studentreg()
    elif opt == 2:
        issuebook()
    elif opt == 3:
        bookstatus()
    elif opt == 4:
        studentstatus()
    elif opt == 5:
        addbooks()
    elif opt ==6:
        with open("libstudent.pkl","wb") as f:
            pickle.dump(student,f)
        with open("libbook.pkl","wb") as f:
            pickle.dump(book,f)
        print("Done")
        exit()
    else:
        print("Wrong input")
while True:
    print("\n"*7)
    main()
    os.system("cls")
