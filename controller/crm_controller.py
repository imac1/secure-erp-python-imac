from email import header
from turtle import title
from model.crm import crm
from view import terminal
import sys
import erp
from controller import main_controller


def list_customers():
    header, table = crm.get_CRM_data()
    terminal.print_table(header, table)


def add_customer():
    header, table = crm.get_CRM_data()
    user = []
    user_ID = terminal.get_input(label='please, enter an ID\n')
    user.append(user_ID)
    # search all emails in table and check if email matches one
    ID_col = [row[0] for row in table]
    if user_ID in ID_col:
        terminal.get_input(label='ID in DB, please, enter another ID or press 3 to try again\n')
    else:
        user_name = terminal.get_input(label="please, enter customer name\n")
        user.append(user_name)
        user_email = terminal.get_input(label="Please enter an email\n")
        user.append(user_email)
        user_subscribed_check = terminal.get_input(label="Please, enter 1 for subscribed / 0 for unsubscribed \n")
        user.append(user_subscribed_check)
    crm.write_CRM_data(user)
    header, table = crm.get_CRM_data()
    terminal.print_table(header, table)


def update_customer():
    header, table = crm.get_CRM_data()
    updated_user = []
    
    for item in range(len(header)):
        if header[item] == 'id':
            id_index = item
 
    user_ID = terminal.get_input(label='please, enter an ID\n')
    ID_col = [row[id_index] for row in table]
    if user_ID in ID_col:
        updated_user.append(user_ID)
        user_name = terminal.get_input(label="please, enter customer name\n")
        updated_user.append(user_name)
        user_email = terminal.get_input(label="Please enter an email\n")
        updated_user.append(user_email)
        user_subscribed_check = terminal.get_input(label="Please, enter 1 for subscribed / 0 for unsubscribed \n")
        updated_user.append(user_subscribed_check)
    else:
        terminal.print_error_message('Please, select 3 to add a new customer\n')
    
    table = crm.update_CRM_user(updated_user, user_ID)
    header, table = crm.get_CRM_data()
    terminal.print_table(header, table)
    

def delete_customer():
    header, table = crm.get_CRM_data()
    user_ID = terminal.get_input(label='please, enter an ID to remove\n')
    crm.remove_user(user_ID)
    terminal.print_table(header, table)


def get_subscribed_emails():
    emails = crm.get_subscribed_emails()
    print(emails)


def run_operation(option):
    if option == 1:
        erp.main_controller.menu()
    elif option == 2:
        list_customers()
    elif option == 3:
        add_customer()
    elif option == 4:
        update_customer()
    elif option == 5:
        delete_customer()
    elif option == 6:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = [
        "Back to main menu",
        "List customers",
        "Add new customer",
        "Update customer",
        "Remove customer",
        "Subscribed customer emails",
    ]
    terminal.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != "0":
        display_menu()
        try:
            operation = terminal.get_input("Select an operation\n")
            run_operation(int(operation))
        except KeyError as err:
            terminal.print_error_message(err)
