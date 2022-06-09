
""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


# DATAFILE = "model/crm/crm.csv"
'''
TODO de verificat de ce nu preia path-urile automat
'''
DATAFILE = '/Users/macbook/Documents/CodeCool/secure-erp-python-imac1/model/crm/crm.csv'
HEADERS = ["id", "name", "email", "subscribed"]


def get_CRM_data():
    table = data_manager.read_table_from_file(DATAFILE, separator=';')
    return HEADERS, table


def write_CRM_data(user):
    table = data_manager.read_table_from_file(DATAFILE, separator=';')
    table.append(user)
    data_manager.write_table_to_file(DATAFILE, table, separator=';')
    return HEADERS, table

def update_CRM_user(updated_user, user_ID):
    table = data_manager.read_table_from_file(DATAFILE, separator=';')
    
    ID_col = [row[0] for row in table]
    id_index = ID_col.index(user_ID)

    id, name, email, subs = updated_user
    table[id_index][1] = name
    table[id_index][2] = email
    table[id_index][3] = subs

    data_manager.write_table_to_file(DATAFILE, table, separator=';')
    return HEADERS, table

def remove_user(user_id):
    table = data_manager.read_table_from_file(DATAFILE, separator=';')
    
    ID_col = [row[0] for row in table]
    for i, v in enumerate(table):
        if v[0] == user_id:
            table.remove(table[i])
    data_manager.write_table_to_file(DATAFILE, table, separator=';')
    return HEADERS, table

def get_subscribed_emails():
    table = data_manager.read_table_from_file(DATAFILE, separator=';')

    for i, v in enumerate(HEADERS):
        if v == 'email':
            email_index = i
        elif v == 'subscribed':
            subs_col_index = i

    subscribed_emails = []

    for row in range(len(table)):
        if table[row][subs_col_index] == '1':
            email = table[row][email_index] 
            subscribed_emails.append(email)

    return subscribed_emails




