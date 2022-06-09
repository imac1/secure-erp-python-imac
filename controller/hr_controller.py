
from model.hr import hr
from view import terminal
import erp
from controller import main_controller


def list_employees():
    header, table = hr.get_HR_data()
    terminal.print_table(header, table)


def add_employee():
    employee_info = ["Id\n", "Name\n", "Date of birth\n", "Department\n", "Clearance\n"]
    data = terminal.get_inputs(employee_info)
    hr.write_HR_employee(data)
    header, table = hr.get_HR_data()
    terminal.print_table(header, table)


def update_employee():
    list_employees()
    data = ["Id\n", "Name\n", "Date of birth\n", "Department\n", "Clearance\n"]
    
    info = terminal.get_input(label="please, enter an ID\n")
    if hr.check_employee_id(info):
        info = terminal.get_inputs(data)
        hr.update_HR_employee(info)
    else:
        print('Please, enter a correct ID\n')
        terminal.get_inputs(info)
    list_employees()



def delete_employee():
    list_employees()
    employee_data = terminal.get_input(label="Please, enter an id to be deleted \n")
    hr.delete_HR_employee(employee_data)
    list_employees()


def get_oldest_and_youngest():
    list_employees()
    age_diff = hr.substract_youngest_oldest()
    print(age_diff)


def get_average_age():
    age = hr.calc_average_age()
    print(f'average age is {age}')


def next_birthdays():
    try:
        header, table = hr.get_HR_data()
        terminal.print_table(header, table)
        expected_period = terminal.get_input(label="please, enter a year 'yyyy-mm-dd' format\n")
        date_from_table = terminal.get_input(label="please, enter a year 'yyyy-mm-dd' format\n")
    except ValueError:
        print("please enter a number")
    x = hr.next_birthday_2wks(date_from_table, expected_period)
    
    print(f'the next birthday is in {x} days from {date_from_table}')


def count_employees_with_clearance():
    list_employees()
    clearance_empl = hr.calc_clearance()
    print(f'number of employees with clearance is {clearance_empl}')



def count_employees_per_department():
    empl_no_by_dep = hr.calc_empl_by_dep()
    print(f'the number of employees by department is {empl_no_by_dep}')



def run_operation(option):
    if option == 1:
        erp.main_controller.menu()
    elif option == 2:
        list_employees()
    elif option == 3:
        add_employee()
    elif option == 4:
        update_employee()
    elif option == 5:
        delete_employee()
    elif option == 6:
        get_oldest_and_youngest()
    elif option == 7:
        get_average_age()
    elif option == 8:
        next_birthdays()
    elif option == 9:
        count_employees_with_clearance()
    elif option == 10:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = [
        "Back to main menu",
        "List employees",
        "Add new employee",
        "Update employee",
        "Remove employee",
        "Oldest and youngest employees",
        "Employees average age",
        "Employees with birthdays in the next two weeks",
        "Employees with clearance level",
        "Employee numbers by department",
    ]
    terminal.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != "0":
        display_menu()
        try:
            operation = terminal.get_input("Select an operation\n")
            run_operation(int(operation))
        except KeyError as err:
            terminal.print_error_message(err)
