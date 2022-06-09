""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

import enum
from model import data_manager, util
from view import terminal


DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]


def get_list_tansactions():
    table = data_manager.read_table_from_file(DATAFILE, separator=";")
    return HEADERS, table


def add_new_transaction(data):
    transaction_info = data_manager.read_table_from_file(DATAFILE, separator=";")
    data = [util.generate_id()] + data
    transaction_info.append(data)
    data_manager.write_table_to_file(DATAFILE, transaction_info, separator=";")


def update_transaction(data):
    table = data_manager.read_table_from_file(DATAFILE, separator=";")
    for i in table:
        if i[0] == data[0]:
            i[1] = data[1]
            i[2] = data[2]
            i[3] = data[3]
            i[4] = data[4]
    data_manager.write_table_to_file(DATAFILE, table, separator=";")


def delete_transaction(id):
    table = data_manager.read_table_from_file(DATAFILE, separator=";")
    for row in table:
        if row[0] == id:
            table.remove(row)
    data_manager.write_table_to_file(DATAFILE, table, separator=";")


def max_revenue():
    table = data_manager.read_table_from_file(DATAFILE, separator=";")
    Price_col = [row[3] for row in table]
    prices_floats = [float(x) for x in Price_col]
    int_prices = [int(x) for x in prices_floats]
    biggest_gain = max(int_prices)

    return biggest_gain


def biggest_revenue_product():
    table = data_manager.read_table_from_file(DATAFILE, separator=";")
    Price_col = [row[3] for row in table]
    Prod_col = [row[2] for row in table]
    prices_floats = [float(x) for x in Price_col]
    max_price = max(prices_floats)
    max_str = str(max_price)
    index_to_search = Price_col.index(max_str)
    prod = Prod_col[index_to_search]
    return prod


def transactions_between_dates(date):
    table = data_manager.read_table_from_file(DATAFILE, separator=";")
    date_1, date_2 = date
    yy_1, mm_1, dd_1 = map(int, date_1.split("-"))
    yy_2, mm_2, dd_2 = map(int, date_2.split("-"))
    date_col_DB = [row[4] for row in table]
    years = []
    months = []
    days = []

    for item in date_col_DB:
        yr = item[0:4]
        years.append(yr)
        mm = item[5:7]
        months.append(mm)
        dd = item[8:]
        days.append(dd)
    dates = [years, months, days]
    int_years = [int(x) for x in years]
    int_months = [int(x) for x in months]
    int_days = [int(x) for x in days]
    int_dates = [int_years, int_months, int_days]
    for year in int_years:
        if year <= yy_1:
            start_date = int_years.index(year)
        elif yy_2 in int_years:
            end_date = int_years.index(year)

    return f" there are {end_date - start_date} transactions"


def sum_of_transactions(dates):
    table = data_manager.read_table_from_file(DATAFILE, separator=";")
    date_1, date_2 = dates
    yy_1, mm_1, dd_1 = map(int, date_1.split("-"))
    yy_2, mm_2, dd_2 = map(int, date_2.split("-"))
    date_col_DB = [row[4] for row in table]
    price_list = [row[3] for row in table]
    prices_floats = [float(x) for x in price_list]
    years = []
    for item in date_col_DB:
        yr = item[0:4]
        years.append(yr)
    int_years = [int(x) for x in years]
    for year in int_years:
        if year <= yy_1:
            start_date = int_years.index(year)
        elif yy_2 in int_years:
            end_date = int_years.index(year)
    return f"the sum is {sum(prices_floats[start_date: end_date])}"


def check_transaction_id(id):
    table = data_manager.read_table_from_file(DATAFILE, separator=";")
    ID_col = [row[0] for row in table]
    if id in ID_col:
        return True
    else:
        False
