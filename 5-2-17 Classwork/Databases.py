import sqlite3

class database:
    def __init__(self, name, column1, column2):
        self.filename = name + '.db'
        self.tablename = name
        self.connection = sqlite3.connect(self.filename)
        self.cursor = self.connection.cursor()
        self.column1 = column1
        self.column2 = column2
        try:
            self.cursor.execute('CREATE TABLE %s (%s TEXT, %s INTEGER)' % (self.tablename, self.column1, self.column2))
            print('Table created')
        except:
            pass
        try:
            # self.cursor.execute('ALTER TABLE %s ADD COLUMN %s INTEGER' % (self.tablename, self.column2))
            print('Bloop!')
            # print('Second column added')
        except:
            pass
        print('Pass!')

    def insert(self, val1, val2):
        self.cursor.execute('SELECT * FROM %s order by %s DESC;' % (self.tablename, self.column2))
        try:
            self.cursor.execute('UPDATE %s SET %s=%d WHERE %s=%s;' % (self.tablename, self.column2, val2, self.column1, val1))
        except:
            self.cursor.execute('INSERT INTO %s VALUES(%s, %d);' % (self.tablename, val1, val2))

    def getValues(self):
        self.cursor.execute('SELECT * FROM %s order by %s DESC;' % (self.tablename, self.column2))
        return self.cursor.fetchall()

def main():
    leaderboard = database('leaderboard', 'Name', 'Score')
    leaderboard.insert('Kevin', 10)
    leaderboard.insert('Joe', 15)
    print(leaderboard.getValues())


main()
