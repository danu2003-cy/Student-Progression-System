from graphics import *

# Coursework Part - 2
print('''
I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
Any code taken from other sources is referenced within my code solution.

Student ID: w2051668
IIT ID: 20230443

Date: 09/12/2023 
''')

scores = [0, 20, 40, 60, 80, 100, 120]

progress = 0
module_trailer = 0
module_retriever = 0
exclude = 0

progress_list = []
trailer_list = []
retriever_list = []
exclude_list = []


def person_selection():
    global person
    while True:
        person = input("Choose student or staff \n's' for Student\n't' for staff\nEnter your choice : ")
        if person == 's' or person == 't':
            start()
        else:
            print("Invalid Input")


def validation(Pass, Defer, Fail):
    if Pass + Defer + Fail != 120:
        print("Total incorrect")
        start()
    else:
        progression_outcome(Pass, Defer, Fail)


def progression_outcome(Pass, Defer, Fail):
    global progress, module_trailer, module_retriever, exclude
    if Pass == 120:
        progress_list.append([Pass, Defer, Fail])
        print("Progress")
        progress += 1
    elif Pass == 100:
        trailer_list.append([Pass, Defer, Fail])
        print("Progress (module trailer) ")
        module_trailer += 1
    elif Fail >= 80:
        exclude_list.append([Pass, Defer, Fail])
        print("Exclude")
        exclude += 1
    elif Fail <= 60:
        retriever_list.append([Pass, Defer, Fail])
        print("Do not Progress – module retriever")
        module_retriever += 1
    if person == "t":
        multiple_outcomes()


def multiple_outcomes():
    print()
    print("Would you like to enter another set of data?")
    answer = input("Enter 'y' for yes or 'q' to quit and view results: ")

    if answer == "y":
        start()
    elif answer == "q":
        list_part()
#Part-3 save data to a text file
        with open("CW_DataStore.txt", "w") as file:
            file.write("\n")
            printDataList = [progress_list, trailer_list, exclude_list, retriever_list]
            for dataList in printDataList:
                for entry in dataList:
                    line = ",".join(str(x) for x in entry)
                    file.write(line + "\n")
        exit()
    else:
        print("Wrong command choose again")
        multiple_outcomes()


def list_part():
    for values in progress_list:
        print("Progress - " + str(values[0:])[1:-1])
    for values in trailer_list:
        print("Progress (module trailer) - " + str(values[0:])[1:-1])
    for values in retriever_list:
        print("Module Retriever - " + str(values[0:])[1:-1])
    for values in exclude_list:
        print("Exclude - " + str(values[0:])[1:-1])


def start():
    while True:
        while True:
            try:
                Pass = int(input("Please enter your credits at Pass: "))
                if Pass not in scores:
                    print("Out of range")
                else:
                    break
            except ValueError:
                print("Integer Required")

        while True:
            try:
                Defer = int(input("Please enter your credits at Defer: "))
                if Defer not in scores:
                    print("Out of range")
                else:
                    break
            except ValueError:
                print("Integer Required")

        while True:
            try:
                Fail = int(input("Please enter your credits at Fail: "))
                if Fail not in scores:
                    print("Out of range")
                else:
                    validation(Pass, Defer, Fail)
                    break
            except ValueError:
                print("Integer Required")

        break
person_selection()
