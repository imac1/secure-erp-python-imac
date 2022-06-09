# from view import terminal

DATAFILE = '/Users/macbook/Documents/CodeCool/secure-erp-python-imac1/model/crm/crm.csv'
HEADERS = ["id", "name", "email", "subscribed"]

def read_table_from_file(file_name, separator=';'):
    """Read CSV file into a data table.

    Args:
        file_name: The name of the CSV data file.
        separator: The CSV separator character

    Returns:
        The data parsed into a list of lists.
    """
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        return [element.replace("\n", "").split(separator) for element in lines]
    except IOError:
        return []

def write_table(file_name, table, separator=';'):
    with open(file_name, "w") as file:
        for record in table:
            row = separator.join(record)
            file.write(row + "\n")


def get_CRM_data():
    table = read_table_from_file(DATAFILE, separator=';')
    return HEADERS, table



# def add_customer():
#     # header, table = get_CRM_data()
#     '''
#     take a name from the user
#     take an email
#     if the email is in DB - please enter a valid email or / 
#     error message / or email is already in DB, and don't write
#     option to return into the same menu and add another mail
#     make an email validator - ?
#     ask if subscribed
#     if subs add 1, else 0
#     generate an id
#     '''
    # user = []
    # user_labels = ["name: ", "email: ", "subscribed: "]
    # user_email = terminal.get_inputs(user_labels, "please, enter your email\n")
    # # search all emails in table and check if email matches one
    # email_col = [row[2] for row in table]
    # if user_email in email_col:
    #     print('Please, enter another email')
    #     user_email = terminal.get_inputs(user_labels, "please, enter your email\n")
    # else:
    #     user_name = terminal.get_inputs(user_labels, "please, enter your name\n")
    #     user_subscribed_check = terminal.get_inputs(user_labels, "Have you subscribed to our nesletter? Y/N \n")
    #     if user_subscribed_check.lower() == 'y':
    #         user_subscribed = '1'
    #     else: 
    #         user_subscribed = "0"
    #     user_id = "generator"
    #     user.append(user_id)
    #     user.append(user_name)
    #     user.append(user_email)
    #     user.append(user_subscribed)
    #     table.extend([user])


    # print(user)
    # print(table)

# print(add_customer())

# def write_table():
#     # print(user)
#     table = read_table_from_file(DATAFILE, separator=';')
#     print(table)
    # new_table = [['cococ#&', 'Lieselotte ', 'hv8@qsuotla508.com', '1'], ['kH14Ju#&', 'Adrianna Verduzco', 'i-4371v-.rhck@qe8yy3d.com', '0'], ['eH34Jd#&', 'Maude Toll', 't1ytt@vpm5xkvn.com', '1']]
#     # table.extend([user])
#     # print(new_table)

#     extra = write_table(DATAFILE, new_table, separator=';')
#     print(extra)
#     # print(HEADERS, new_table)
#     return HEADERS, extra


# print(write_table())
# print(get_CRM_data())

# table.append(['s', 's', 's', 's'])
# new = []
# new = table
# # print(new)

# with open(DATAFILE, "w") as file:
#     for record in new:
#         row = ';'.join(record)
#         file.write(row + "\n")


table = [['cococ#&', 'Lieselotte ', 'hv8@qsuotla508.com', '1'], ['kH14Ju#&', 'Adrianna Verduzco', 'i-4371v-.rhck@qe8yy3d.com', '0'], ['eH34Jd#&', 'Maude Toll', 't1ytt@vpm5xkvn.com', '1'], ['1', '2', '2', '3']]
# ID_col = [row[0] for row in table]
# print(ID_col)
emails = []
# for row in range(len(table)):
#     for col in range(0, 3):


for i, v in enumerate(HEADERS):
    if v == 'email':
        print(i)





