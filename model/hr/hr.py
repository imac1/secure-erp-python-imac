""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""


from model import data_manager, util
from view import terminal


DATAFILE = "/Users/macbook/Documents/CodeCool/secure-erp-python-imac1/model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def get_HR_data():
    table = data_manager.read_table_from_file(DATAFILE, separator=";")
    return HEADERS, table


def write_HR_employee(employee):
    table = data_manager.read_table_from_file(DATAFILE, separator=';')
    table.append(employee)
    data_manager.write_table_to_file(DATAFILE, table, separator=';')



def update_HR_employee(data):
    table = data_manager.read_table_from_file(DATAFILE, separator=';')
    for i in table:
        if i[0] == data[0]:
            i[1] = data[1]
            i[2] = data[2]
            i[3] = data[3]
            i[4] = data[4]
    data_manager.write_table_to_file(DATAFILE, table, separator=';')



def delete_HR_employee(id):
    table = data_manager.read_table_from_file(DATAFILE, separator=';')
    for row in table:
        if row[0] == id:
            table.remove(row)
    data_manager.write_table_to_file(DATAFILE, table)


def substract_youngest_oldest():
    HR_employee_data = data_manager.read_table_from_file(DATAFILE, separator=';')
    date_col_ID = [row[2] for row in HR_employee_data]
    years = []
    for item in date_col_ID:
        yr = item[0: 4]
        years.append(yr)
    int_years = [int(x) for x in years]
    youngest_empl = min(int_years)
    oldest_empl = max(int_years)
    young_old_dif = oldest_empl - youngest_empl
    return (f' the age difference is {young_old_dif}')


def calc_average_age():
    table = data_manager.read_table_from_file(DATAFILE, separator=';')
    for item in range(len(HEADERS)):
        if HEADERS[item] == 'Date of birth':
            date_index = item
    date_col_ID = [row[date_index] for row in table]
    years = []
    current_yr = 2022
    for item in date_col_ID:
        year = current_yr - int(item[0: 4])
        years.append(year)

    average_age = sum(years) / len(years)
    return average_age

def calculate_no_days_2(yy, mm, dd):
    if mm <= 2:
        mm = mm + 12
        yy = yy - 1
    no_of_days = (146097 * yy)/400 + (153*mm + 8)/5 + dd
    return no_of_days

def calculate_no_of_days_1(yy, mm, dd):

    '''
    1. calculate both dates in number of days
    If Month <= 2, then subtract 1 from Year ( if mm <=2 then 
    Year = Year - 1 else Year = Year)
    If Month <= 2, then add 13 to month or add 1 to month
     ( if mm <=2 then mm = mm+13 else mm = mm+1)
    '''

    if mm <= 2:
        yy -= 1
        if mm <= 2:
            mm += 13
        else:
            mm += 1
    else:
        yy = yy
        '''
        2 formula to convert years, months, days => days
        '''
    nr_of_days = (1461*yy/4) + (153*mm/5) + dd

    '''
    or
    '''
    if mm <= 2:
        mm = mm + 12
        yy = yy-1

    no_of_days = (146097 * yy)/400 + (153*mm + 8)/5 + dd



def next_birthday_2wks(input_date, table_date):
    HR_employee_data = data_manager.read_table_from_file(DATAFILE, separator=';')
    for item in range(len(HEADERS)):
        if HEADERS[item] == 'Date of birth':
            date_index = item

    date_col_ID = [row[date_index] for row in HR_employee_data]
    
    in_year = int(input_date[0: 4])
    in_month_date = int(input_date[5: 7])
    in_day_date = int(input_date[8: 10])

    table_date = date_col_ID[0]
    tb_year = int(table_date[0: 4])
    tb_month_date = int(table_date[5: 7])
    tb_day_date = int(table_date[8: 10])

    in_days = calculate_no_days_2(2000, 5, 10)
    tab_days = calculate_no_days_2(2000, 5, 30)

    return abs(tab_days - in_days)


def calc_clearance():
    table = data_manager.read_table_from_file(DATAFILE, separator=';')
    date_col_ID = [row[4] for row in table]
    int_clearance = [int(x) for x in date_col_ID]
    for item in int_clearance:
        if item > 0:
            return len(date_col_ID)


def calc_empl_by_dep():
    table = data_manager.read_table_from_file(DATAFILE, separator=';')
    date_col_DEP = [row[3] for row in table]
    counter_s = 0
    counter_p = 0
    for item in date_col_DEP:
        if item == 'Sales':
            counter_s += 1
        else:
            counter_p += 1
    dep_counter = {'sales': counter_s, "Production": counter_p}
    return dep_counter

        


def check_employee_id(id):
    table = data_manager.read_table_from_file(DATAFILE, separator=";")
    ID_col = [row[0] for row in table]
    if id in ID_col:
        return True
    else:
        False










 







