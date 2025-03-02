# Coursework Part-1
print(
    """
I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
Any code taken from other sources is referenced within my code solution.

Student ID: UOW ID - w2051668

IIT ID - 20230443
 
Date: 09/12/2023 
"""
)

from graphics import *

scores = [0, 20, 40, 60, 80, 100, 120]

progress = 0
module_trailer = 0
module_retriever = 0
exclude = 0
person = ""
total_students = 0

def person_selection():
    global person
    while True:
        person = input(
            "Choose student or staff \n's' for Student\n't' for staff\nEnter your choice : "
        )
        if person == "s" or person == "t":
            start()
        else:
            print("Invalid Input")
            person_selection()


# to get the total number of PASS, FAIL & DEFER


def validation(Pass, Defer, Fail):
    if Pass + Defer + Fail != 120:
        print("Total incorrect")
        start()
    else:
        progression_outcome(Pass, Fail)


# to display the outcome


def progression_outcome(Pass, Fail):
    global progress, module_trailer, module_retriever, exclude
    if Pass == 120:
        print("Progress")
        progress += 1
    elif Pass == 100:
        print("Progress (module trailer) ")
        module_trailer += 1
    elif Fail >= 80:
        print("Exclude")
        exclude += 1
    elif Fail <= 60:
        print("Do not Progress – module retriever")
        module_retriever += 1
    if person == "t":
        multiple_outcomes()


# for the selection of 'YES' or 'NO'


def multiple_outcomes():
    print()
    print("Would you like to enter another set of data?")
    answer = input("Enter 'y' for yes or 'q' to quit  view results: ")

    if answer == "y":
        start()
    elif answer == "q":
        histogram()
    else:
        print("wrong command choose again")
        multiple_outcomes()


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


# for the histogram
# import the graphics.py module (must be in the same folder this file)
def histogram():  # import the graphics.py module (must be in the same folder this file)
    # OPEN THE WINDOW
    win = GraphWin("histogram", 500, 400)
    heading = Text(Point(100, 20), "Histogram Results")
    heading.setStyle("bold")
    heading.draw(win)

    bottom_line = Line(Point(10, 320), Point(490, 320))
    bottom_line.draw(win)

    progress_rectangle = Rectangle(Point(20, 320), Point(120, 320 - progress * 10))
    progress_rectangle.setFill("Yellow")
    p_text1 = Text(Point(60, 340), "Progress")
    p_text1.draw(win)
    p_text2 = Text(Point(60, 310 - progress * 10), progress)
    p_text2.draw(win)
    progress_rectangle.draw(win)

    trailer_rectangle = Rectangle(
        Point(140, 320), Point(240, 320 - module_trailer * 10)
    )
    trailer_rectangle.setFill("lightblue")
    t_text1 = Text(Point(180, 340), "Trailer")
    t_text1.draw(win)
    t_text2 = Text(Point(180, 310 - module_trailer * 10), module_trailer)
    t_text2.draw(win)
    trailer_rectangle.draw(win)

    retriever_rectangle = Rectangle(
        Point(260, 320), Point(360, 320 - module_retriever * 10)
    )
    retriever_rectangle.setFill("Green")
    r_text1 = Text(Point(300, 340), "Retriever")
    r_text1.draw(win)
    r_text2 = Text(Point(300, 310 - module_retriever * 10), module_retriever)
    r_text2.draw(win)
    retriever_rectangle.draw(win)

    exclude_rectangle = Rectangle(Point(380, 320), Point(480, 320 - exclude * 10))
    exclude_rectangle.setFill("Pink")
    e_text1 = Text(Point(420, 340), "Excluded")
    e_text1.draw(win)
    e_text2 = Text(Point(420, 310 - exclude * 10), exclude)
    e_text2.draw(win)
    exclude_rectangle.draw(win)


    win.getMouse()
    win.close()
    main()
    

person_selection()
