# program for counting how much money I've spent on Amazon purchases
# log it into a text file with a running total of dollar amounts
# SLOW FINANCES YAY
import os.path
import csv
import re
from decimal import *
from datetime import datetime
# https://docs.python.org/2/library/decimal.html


test_data = """Entry, CDN/USD, Price, Book or Other, Date of Purchase, Date added, Title,
01. , CDN,      11.33, Other, 05/17/2019, 5/21/2019,         Mennen Speed Stick Unscented,
02. , CDN,      7.10, Book, 05/17/2019, 5/21/2019,           Think Big: Make It Happen in Business and Life,
03. , CDN,      17.18, Other, 05/07/2019, 5/21/2019,          Ceinture Noire,
04. , CDN,      9.85, Other, 05/02/2019, 5/21/2019,           Merkur Double Edge Razor Blades,
05. , CDN,      19.79, Book, 01/ 22/ 2019, 5/21/2019,      Ask and It Is Given,
06. , CDN,      5.57, Book, 12/22/ 2018, 5/21/2019,      Good Manners for Nice People Who Sometimes Say F*ck,
07. , CDN,      1.92, Book, 12/22/ 2018, 5/21/2019,      Overcoming Bipolar Disorder,
08. , CDN,      9.65, Book, 12/17/2018, 5/21/2019,      Models: Attract Women Through Honesty,
09. , CDN,      22.99, Other, 12/10/ 2018, 5/21/2019,    NOW Nac-Acetyl Cysteine Veg Capsules,
10. , CDN,      14.80, Book, 12/6/2018, 5/21/2019,      The Rational Male,
11. , USD,      14.07, Book, 02/17/ 2019, 5/21/2019,     4D Warfare: A Doctrine for a New Generation of Politics,
12. , USD,      10.19, Book, 12/29/ 2018, 5/21/2019,     Sh#t Your Ego Says,
13. , USD,      13.25, Book, 12/23/ 2018, 5/21/2019,     Time's Up,
14. , USD,      7.64, Book, 12/22/ 2018, 5/21/2019,      Bipolar Disorder: A Guide for Patients and Families,
15. , USD,      14.92, Book, 12/8/ 2018, 5/21/2019,      In an Unspoken Voice,
"""


# Thoughts so far:
# Wwanna get a function to clean up user inputs. I.e. Canada, canada, CDN, cdn, Cdn, all become CDN
# $09.33 and $ 9.33 and 9.33 and `09.33 all become: 9.33
# Yes/Book vs No, Other, and literally Any Other Response
# date confirmations, and other ways of turning dates into, well, dates
# Option to re-enter the title as something else
# FEATURE CREEP.


def get_current_date():
    now = datetime.now()  # current date and time
    year = now.strftime("%Y")
    # print("year:", year)
    month = now.strftime("%m")
    # print("month:", month)
    day = now.strftime("%d")
    # print("day:", day)
    date_to_print = day + "/" + month + "/" + year

    return date_to_print


def collector():

    print("What was the country of origin?")
    acceptable_countries = ["Canada", "canada", "USA", "America", "america", "CDN", "USD"]
    a = input("> ")

    print("what was the dollar value?")
    b = input("> ")
    search_object = re.search(r'[.]\d\d', b)  # Trying to make the inputs conform to a standard
    if search_object:
        b2 = b
        print(b2 + "  This is b2")
    else:
        b = input("Try again > ")

    print("was it a book?")
    c = input("> ")
    booklist = ["book", "Book"]
    if c in booklist or affirmatives:
        pass
    else:
        c = input("Must reply using {book} or {aff}. > ".format(
            book=booklist, aff=affirmatives))  # Insufficient job

    print("what is the date of purchase?")
    d = input("> ")
    print("What was the title?")
    e = input("> ")
    local_list = [a, b2, c, d, e]
    # collect all of these in a list to feed into the next function
    as_csv = str(local_list[0]) + "," + str(local_list[1]) + "," + str(
        local_list[2]) + "," + str(local_list[3]) + "," + str(local_list[4])
    return local_list, as_csv


def add_new_receipt(country, value, book, date_of_purchase, title):
    # Put the datetime value as the time added to the database

    prev = country
    finalform = prev.strip(" ")
    return None


affirmatives = ["Yes", "YES", "Y", "y", "yes"]
negatives = ["N", "n", "no", "No", "NO"]

data_base = []  # A place to add newly added receipts while working with them in the program


def get_new_receipt():
    print("Add a new receipt?")  # begin by prompting the user with a simple question
    #  internal_reply = input("Y / N? > ")  # Ask for one of two inputs
    internal_reply = "y"
    if internal_reply in affirmatives:  # If the reply "makes sense," return the reply
        return "Y"  # return a single letter to simplify things
    elif internal_reply in negatives:  # again, just a check for "sense"
        return "N"
    else:  # how would I test this?
        print("Please type one of {affirmatives} or {negatives}").format(
            negatives=negatives, affirmatives=affirmatives)  # Tell the user they did something wrong
        get_new_receipt()  # ...and loop back into the start of the function for attempt #2


reply = get_new_receipt()
print(reply)

mainlist = []

if reply == "Y":
    # print("Write the info out for the program")
    # new_info = collector()[0]  # Call this function to do a bunch of raw input stuff for me
    # print(new_info)

    info_1 = ['canada', '11', 'yes', '05/25/2019', 'Mennen']
    info_2 = ['CDN', '22', 'yes', '05/25/2019', 'San Diego']
    info_3 = ['USA', '15.15', 'book', '05/24/2019', 'War of Art']
    mainlist.append(info_1)
    mainlist.append(info_2)
    mainlist.append(info_3)
elif reply == "N":
    print("Exit Program Now?")
    reply2 = input("Ok? Type OK > ")
    if reply2 != "OK":
        # go to start of program
        pass  # should loop recursively into the start of the program... but how? can I do that?
        # "def ProgramStart" and its all built within ProgramStart ??
        exit()
    else:
        print("Goodbye!")
        exit()
else:
    # go to start of if chain
    print("Your Code Should Never Go Here")
    exit()

getcontext().prec = 5


def add_totals_from_file(file_source_material):
    # need the file source material and then an operation to add the numbers
    # 5/28/2019 note: as a list or as a csv? I think its .csv and thats bad... yeah gotta program arounde it
    split_up_content = file_source_material.rsplit(",")
    function_numbers_list = []

    c = 0

    for entry_contents in split_up_content:
        if ". " not in entry_contents:
            if "." in entry_contents:
                sanitized_whitespace = entry_contents.lstrip()
                function_numbers_list.append(sanitized_whitespace)
                c = c + Decimal(sanitized_whitespace)

    return c  # Returns the total dollars spent

total_dollars_spent = add_totals_from_file(test_data)
# Now I have a way to take a large list of data and get the total $ spent
# write_to_csv
total_dollars_spent = "New Total:," + "CAD," + str(total_dollars_spent)


# f = open("testfile_6.csv", "w+")
# f.write(test_data)
# f.write(total_dollars_spent)
# f.close()
# ^^^ Keep that part as it is sort of "part of" the process

with open("testfil5_tester.csv", "r+") as csvfile:
    text_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    storage = list(text_reader)  # Transfer the csv info to a list

storage_edited = []

for item in storage[:-1]:  # To -1 because I don't want the final entry, which is the total
    for content in item:
        if content is "":
            pass  # Because there were some empty strings in the list
        else:
            # Because I need to remove whitespace from places
            storage_edited.append(content.lstrip())

lines_list = []

for item in storage_edited:  # Discover how many rows there are, basically.
    if re.search(r"\d[.]\s", item):  # "Does it go to 09., 10., or 15.?"
        lines_list.append(item)


def new_final_line_func(prev_final_source):
    # Congrats to me on having a function that transforms the last of the Entry column and adds 1 to it
    new_final_line = Decimal(prev_final_source) + Decimal(1)
    new_final_line = str(new_final_line) + ". "
    return new_final_line

# new_final_line = Decimal(lines_list[-1][0:2]) + Decimal(1)
# lines_list.append(str(new_final_line) + ". ")
# print(lines_list[-1])

next_line_to_add = new_final_line_func(lines_list[-1][0:2])
print(next_line_to_add)
# THIS IS SPECIAL
the_line_itself = next_line_to_add + "," + info_1[0] + "," + info_1[1] + "," \
                  + info_1[2] + "," + info_1[3] + "," + get_current_date() + "," + info_1[4]
print(the_line_itself)  # THIS IS SPECIAL


# Now open the file again and write more lines to it, CORRECTLY, in the right order

file_to_process = open("testfile_6.csv", "r+")


def process_to_open_file(file_variable):
    # Simply plugin the results of open(filename, "r+") and out comes a list
    nu_data = file_variable.read()
    first_cycle = nu_data.split("\n")

    storage_box = []

    for item2 in storage_box[:-1]:  # To -1 because I don't want the final entry, which is the total
        for content2 in item2:
            if content2 is "":
                pass  # Because there were some empty strings in the list
            else:
                # Because I need to remove whitespace from places
                storage_box.append(content2.lstrip())

    return storage_box


def process_to_open_file_w_lines(file_variable):
    nu_data = file_variable.read().split("\n")[1:]
    # ok. this method produces a list of lines. cool. I want to add the next 3 lines to the file.
    return nu_data


def input_new_lines(base_info, new_line_to_append):
    # To add 3 new lines, run the function 3 times.
    # New Line To Append comes from the "new_final_line_func" on line 228.
    if not re.search(r"\d[.]\s", base_info[-1]):
        # This if statement just checks if the final line is a Financial Total or an Entry
        # i.e. without it, the code might append in the wrong place...
        # meaning, it might append after the "Total: xyz dollars" part, instead of before it.
        base_info = base_info[0:-1]
    base_info.append(new_line_to_append + ",")
    return base_info

basic_file = process_to_open_file_w_lines(file_to_process)

another_file_sorta = input_new_lines(basic_file, the_line_itself)
# Made the following two variables so I could add another 2 entries into the mix
handcrafted_with_love = "17. " + "," + info_2[0] + "," + info_2[1] + "," \
                  + info_2[2] + "," + info_2[3] + "," + get_current_date() + "," + info_2[4]
handcrafted_with_love_again = "18. " + "," + info_3[0] + "," + info_3[1] + "," \
                  + info_3[2] + "," + info_3[3] + "," + get_current_date() + "," + info_3[4]
another_file_sorta = input_new_lines(another_file_sorta, handcrafted_with_love)
another_file_sorta = input_new_lines(another_file_sorta, handcrafted_with_love_again)


def formatted_for_totalup(current_format):
    # Take the list version and make it into a continuous csv file for usage
    # in the function: "add_totals_from_file," which takes .csv
    style_new = ""
    total_length_of_list = len(current_format) - 2
    print("Index length:" + str(total_length_of_list))
    for entry in current_format:
        if re.search(r"\d[.]\s", entry):
            style_new += "\n"
            style_new += entry
        else:
            style_new += entry
    return style_new

# NOW: Run the Total Up Function on this thing, so I can have the list of how much i spent
# Commit that new list with the Total to a new file, and delete the old file!
# BOOM Progress


ready_player_one = formatted_for_totalup(another_file_sorta)
nouveau_dollars_spent = "\nNew Total:," + "CAD," + str(add_totals_from_file(ready_player_one))

f = open("testfile_again_6.csv", "w+")
f.write(ready_player_one)
f.write(nouveau_dollars_spent)
f.close()

