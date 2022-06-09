from controller import crm_controller
from model.crm.crm import HEADERS


def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(f"{title} : ")
    for i in range(len(list_options)):
        print(f"{i + 1} {list_options[i]}")
    pass


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    message = "mesaj din print_message"
    return message
    pass


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """

    print(label, ":", result)
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(title, table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    """
    TODO calculate the width of the longest cell in table
    """
    """
    find the max length of each column and save it in a list
    """

    max_cell_width = []
    for items in table:
        for i, item in enumerate(items):
            try:
                if max_cell_width[i] < len(str(item)):
                    max_cell_width[i] = len(str(item))
            except:
                max_cell_width.append(len(item))

    for i, title in enumerate(title):
        if i == 0:
            print("/" + "________" * len(table) + "\\")
            print()

        print("| {:{width}} ".format(title, width=max_cell_width[i]), end="")

    print("\n" + "|" + ("_____________" * (len(max_cell_width))) + "|")
    print()

    for items in table:
        for i, item in enumerate(items):
            if i == 0:
                print("|", end="")
            print("{:{width}} |".format(item, width=max_cell_width[i]), end="")

        print("\n" + "________" * len(table))
        print()

    pass


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    return input(label)
    pass


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    inputs = []
    for element in labels:
        new_label = input(element)
        inputs.append(new_label)

    return inputs
    pass


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    message = "Sorry, there is an error"
    return print(message)
    pass


def print_subscribed_CRM_emails(emails):
    for email in emails:
        print(email)
