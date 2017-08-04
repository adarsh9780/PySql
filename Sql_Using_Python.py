# this program teaches SQL using python.

# import necessary packages
# we are using SQLITE3 as a database. In general, most of the functionality
# are more or less same with the other distribution database system.
import sqlite3 as sql

# connect to database
connection = sql.connect("chinook.db")

# now u r connected to the database, but to access the features of it we need
# a cursor to move around. A cursor is a object of 'connection'
cursor = connection.cursor()

# list the name of every table
def print_table():
    query = 'SELECT name FROM sqlite_master WHERE type="table"'
    # cursor will take our commands(queries) as string and will execute it.
    result = cursor.execute(query)
    for var in result:
        print(var)

# print_table()

class Employees(object):
    def __init__(self, table_name):
        self.employees = table_name

    # example:
    # this function will return column name from given table
    def print_column(self, columns=['*']):
        print()
        query = 'SELECT {} FROM {}'.format(columns, self.employees)
        result = cursor.execute(query)
        # get the columns name from table employees
        column = [description[0] for description in result.description]
        for var in column:
            print(var)

    def head(self, limit=5):
        print()
        print('                     ######## List of first {} people ##########'.format(limit))
        query = 'SELECT * FROM {} LIMIT {}'.format(self.employees, limit)
        result = cursor.execute(query)
        for var in result:
            print(var)

    # find all the employees name who reports to {}
    def ReportsTo(self, id):
        print()
        print('                     ######## List of people who reports to {} ##########'.format(id))
        query = 'SELECT * FROM {} WHERE ReportsTo={}'.format(self.employees, id)
        result = cursor.execute(query)
        for var in result:
            print(var)

    # which are the countries our employees belong to
    def Countries(self):
        print()
        print('                     ######## List of all countries ##########')
        query = 'SELECT DISTINCT Country FROM {}'.format(self.employees)
        result = cursor.execute(query)
        for var in result:
            print(var)

    # which are the distinct values in a column
    def Distinct(self, features):
        print()
        print('                     ######## List of Distinct values in {} ##########'.format(features))
        query = 'SELECT DISTINCT {} FROM {}'.format(features, self.employees)
        result = cursor.execute(query)
        for var in result:
            print(var)

    def find_null(self, features):
        print()
        print('                     ######## List of null columns ##########')
        query = 'SELECT * FROM employees WHERE {} IS NOT NULL'.format(features)
        result = cursor.execute(query)
        for var in result:
            print(var)

    def count_rows(self):
        print()
        print('                     ####### number of rows are : ###########')
        query = 'SELECT COUNT(DISTINCT employeeid) FROM employees'
        result = cursor.execute(query)
        for var in result:
            print(var)

    def inner_join(self, )

emp = Employees('employees')
# emp.print_column()
# emp.head(8)
# emp.ReportsTo(1)
# emp.Countries()
# emp.Distinct(('State', 'City'))
# emp.find_null('LastName')
# emp.count_rows()

a = Employees('customers')
# a.print_column()
# a.count_rows()
# a.head(8)
