from model.sales import sales
from view import terminal
from controller import main_controller
import erp


def list_transactions():
    header, table = sales.get_list_tansactions()
    terminal.print_table(header, table)


def add_transaction():
    transaction_info = ["Customer\n", "Product\n", "Price\n", "Date\n"]
    data = terminal.get_inputs(transaction_info)
    sales.add_new_transaction(data)
    header, table = sales.get_list_tansactions()
    terminal.print_table(header, table)


def update_transaction():
    list_transactions()
    transaction_info = ["ID\n", "Customer\n", "Product\n", "Price\n", "Date\n"]
    info = terminal.get_input(label="please enter an id\n")
    if sales.check_transaction_id(info):
        info = terminal.get_inputs(transaction_info)
        sales.update_transaction(info)
    else:
        print('Please, enter a correct ID\n')
        terminal.get_inputs(transaction_info)
    header, info = sales.get_list_tansactions()
    terminal.print_table(header, info)


def delete_transaction():
    list_transactions()
    transaction_info = terminal.get_input("ID:")
    sales.delete_transaction(transaction_info)
    list_transactions()


def get_biggest_revenue_transaction():
    max_revenue_trans = sales.max_revenue()
    print(max_revenue_trans)


def get_biggest_revenue_product():
    biggest_rev_prod = sales.biggest_revenue_product()
    print(biggest_rev_prod)
    


def count_transactions_between():
    list_transactions()
    transaction_info = terminal.get_inputs(labels=["Minimum Date (yyyy-mm-dd)", "Maximum Date (yyyy-mm-dd)"])
    date = sales.transactions_between_dates(transaction_info)
    print(date)


def sum_transactions_between():
    list_transactions()
    transaction_info = terminal.get_inputs(labels=["Minimum Date (yyyy-mm-dd)", "Maximum Date (yyyy-mm-dd)"])
    date = sales.sum_of_transactions(transaction_info)
    print(date)


def run_operation(option):
    if option == 1:
        erp.main_controller.menu()
    elif option == 2:
        list_transactions()
    elif option == 3:
        add_transaction()
    elif option == 4:
        update_transaction()
    elif option == 5:
        delete_transaction()
    elif option == 6:
        get_biggest_revenue_transaction()
    elif option == 7:
        get_biggest_revenue_product()
    elif option == 8:
        count_transactions_between()
    elif option == 9:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = [
        "Back to main menu",
        "List transactions",
        "Add new transaction",
        "Update transaction",
        "Remove transaction",
        "Get the transaction that made the biggest revenue",
        "Get the product that made the biggest revenue altogether",
        "Count number of transactions between",
        "Sum the price of transactions between",
    ]
    terminal.print_menu("\033[31m" + "Sales" + "\033[0m", options)


def menu():
    operation = None
    while operation != "0":
        display_menu()
        try:
            operation = terminal.get_input("Select an operation\n")
            run_operation(int(operation))
        except KeyError as err:
            terminal.print_error_message(err)
