class InitializeTable(object):
    
    def __init__(self, table_name, cursor):
        """
        DESCRIPTION: Initialize the table. Contains various methods for different
                     manipulations.

        VARIABLES :  table_name--->name of table  to be passed while initializing 
                     this class.

                     cursor----> object of connection which helps to move and access
                     the database.

        USAGE :      a = InitializeTable(table_name, cursor_object)  
        """
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
        """
        DESCRIPTION:  It will select entries along the given columns from the database, 
                      if no argument is provided it will select each & every column.
                      Similar to "SELECT col1, col2.... FROM {}"
                                    OR
                      Similar to "SELECT * FROM {}"

        ARGUMENTS :   columns-----> Whenever & wherever 'columns' is
                      used, it means a list of column names is to be passed.

        RETURN TYPE : Nothing.

        USAGE :       select_distinct(customerId) where 'customerId' is 
                      supposed to be a coulmn name.  
        """
        print()
        query = 'SELECT {} FROM {}'.format(self.unpack(columns), self.table_name)
        result = self.cursor.execute(query)
        for var in result:
            print(var)

    def select_distinct(self, feature):
        """
        DESCRIPTION:  It will select distinct entries in the database.
                      Similar to "SELECT DISTINCT {} FROM {}"

        ARGUMENTS :   feature-----> Whenever & wherever 'feature' is
                      used it means a single column name is to be passed.

        RETURN TYPE : Nothing

        USAGE :       select_distinct(customerId) where 'customerId' is 
                      supposed to be a coulmn name.  
        """
        print()
        print("----------> Distinct features are: ")
        query = 'SELECT DISTINCT {} FROM {}'.format(feature, self.table_name)
        result = self.cursor.execute(query)
        for var in result:
            print(var)

    def count_distinct(self, feature):
        """
        DESCRIPTION:  It will count distinct entries in the database.
                      Similar to "SELECT COUNT(DISTINCT {}) FROM {}"

        ARGUMENTS :   feature-----> Whenever & wherever 'feature' is
                      used it means a single column name is to be passed.

        RETURN TYPE : Nothing

        USAGE :       count_distinct(customerId) where 'customerId' is 
                      supposed to be a coulmn name.  
        """
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

    def insert(self, columns, values):
        """
        DESCRIPTION: Inserts given values in the given features. It may also add duplicate values,
                     if you are using this function in a script. Therefore make sure you don't forget
                     to comment it out after used once, else duplicate values will be inserted
                     every time you would run your file.

        ARGUMENTS  : column----> list of features
                     Make sure to add those features which can't take NULL Values.

                     values----> list of values
                     Make sure values are in same order as in features are passed.

        RETURN TYPE: Nothing.
        
        USAGE      : insert(column, values)

        NOTE(1)    : Format of value:
                     values = ["'value1'", "'value2'", ...... so on]
                     i.e values are to be passed as strings of string.

        NOTE(2)    : In MariaDB, sqlite3 and some others, you may not need to pass
                     the features explicitly if you are adding values for all of the 
                     coulmns.
                     This functionality is not supported yet.
        """
        print()
        print("----------> Inserting along the features {}".format(self.unpack(columns)))

        query = 'INSERT INTO {} ({}) VALUES ({})'.format(self.table_name,
                                                       self.unpack(columns), 
                                                       self.unpack(values))
        result = self.cursor.execute(query)

    def update(self, list_of_feature_value, condition):
        print()
        print('----------> updating ------------>')
        query = 'UPDATE {} SET {} WHERE {}'.format(self.table_name,
                                                   self.unpack(list_of_feature_value),
                                                   condition)
        result = self.cursor.execute(query)
        for var in result:
            print(var)


    




# list the name of every table
def print_table(cursor):
    print()
    print("----------> Tables in this database are :")
    query = 'SELECT name FROM sqlite_master WHERE type="table"'
    # self.cursor will take our commands(queries) as string and will execute it.
    result = cursor.execute(query)
    for var in result:
        print(var)


if __name__ == '__main__':
    pass