# Component two, function that allows user to enter whole and decimal point numbers


def qst_statement(question):
    valid = False
    while not valid:
        try:
            response = float(input(question))
            return response
        except ValueError:
            print("Invalid input, try again")


# Loop for testing purpose
keep_going = ""
while keep_going == "":

    answer = qst_statement("What's 4.35 + 8.11 = ")
