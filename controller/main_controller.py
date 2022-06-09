from ast import arg
from view import terminal as view
from controller import crm_controller, sales_controller, hr_controller
import sys


def load_module(option):
    if option == 1:
        sys.exit()
    elif option == 2:
        crm_controller.menu()
    elif option == 3:
        sales_controller.menu()
    elif option == 4:
        hr_controller.menu()
    elif option == 0:
        return 0
    else:
        raise KeyError()


def display_menu():
    options = [
        "Exit program",
        "Customer Relationship Management (CRM)",
        "Sales",
        "Human Resources",
    ]
    view.print_menu("Main menu", options)


def menu():
    option = None
    while option != "0":
        display_menu()
        try:
            option = view.get_input("Select module\n")
            load_module(int(option))
            view.print_menu(*arg)
        except KeyError:
            view.print_error_message("There is no such option!")
        except ValueError:
            view.print_error_message("Please enter a number!\n")
    view.print_message("Good-bye!")
