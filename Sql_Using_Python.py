# list the name of every table
def print_table(cursor):
    print()
    print("----------> Tables in this database are :")
    query = 'SELECT name FROM sqlite_master WHERE type="table"'
    # self.cursor will take our commands(queries) as string and will execute it.
    result = cursor.execute(query)
    for var in result:
        print(var)

class InitializeTable(object):
    
    def __init__(self, table_name, cursor):
        self.table_name = table_name
        self.cursor = cursor

    def unpack(self, list_of_features):
        return (", ".join(["%s"] * len(list_of_features))) % tuple(list_of_features)

    # example:
    # this function will return column name from given table
    def print_columns(self):
        print()
        print("----------> Columns in '{}' are :".format(self.table_name))
        query = 'SELECT * FROM {}'.format(self.table_name)
        result = self.cursor.execute(query)
        # get the columns name from table table_name
        column = [description[0] for description in result.description]
        for var in column:
            print(var)

    def head(self, limit=5):
        print()
        print('----------> List of first {} people are:'.format(limit))
        query = 'SELECT * FROM {} LIMIT {}'.format(self.table_name, limit)
        result = self.cursor.execute(query)
        for var in result:
            print(var)

    # calculates the total numer of entries in a feature, pass the id to calculate 
    # number of rows in table.
    def count_rows(self, features):
        print()
        print('----------> Number of rows are :')
        query = 'SELECT COUNT(DISTINCT {}) FROM {}'.format(features, self.table_name)
        result = self.cursor.execute(query)
        for var in result:
            print(var)

    # pass a list of columns/features, if nothing is passed will
    # print each and every entries present in the table
    def select(self, columns='*'):
        print()
        query = 'SELECT {} FROM {}'.format(self.unpack(columns), self.table_name)
        result = self.cursor.execute(query)
        for var in result:
            print(var)

    def select_distinct(self, feature):
        print()
        print("----------> Distinct features are: ")
        query = 'SELECT DISTINCT {} FROM {}'.format(feature, self.table_name)
        result = self.cursor.execute(query)
        for var in result:
            print(var)

    def count_distinct(self, feature):
        print()
        print("----------> Number of distinct {} are: ".format(feature))
        query = 'SELECT COUNT(DISTINCT {}) FROM {}'.format(feature, self.table_name)
        result = self.cursor.execute(query)
        for var in result:
            print(var)

    def where(self, columns, condition):
        print()
        print("----------> Entries along the features {} which satistfy \
the condition {}".format(self.unpack(columns), condition))

        query = 'SELECT {} FROM {} WHERE {}'.format(self.unpack(columns), self.table_name, condition)
        result = self.cursor.execute(query)
        for var in result:
            print(var)

if __name__ == '__main__':
    pass