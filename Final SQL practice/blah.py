import sqlite3

class database:
    def __init__(self, name, col1, col2):
        self.tablename = name
        self.filename = name + '.db'
        self.connection = sqlite3.connect(self.filename)
        self.cursor = self.connection.cursor()
        self.col1 = col1
        self.col2 = col2
        try:
            self.cursor.execute("CREATE TABLE {tn} ({c1} TEXT)".format(tn=self.tablename, c1=self.col1))
        except Exception as err:
            print(err)
        try:
            self.cursor.execute("ALTER TABLE {tn} ADD COLUMN {c2} INTEGER".format(tn=self.tablename, c2=self.col2))
        except Exception as err:
            print(err)

    def insert(self, val1, val2):
        try:
            self.cursor.execute("UPDATE {tn} SET {c2}='{v2}' WHERE {c1}='{v1}'".format(tn=self.tablename, c2=self.col2, v2=val2, c1=self.col1, v1=val1))
        except Exception as err:
            print(err)
            try:
                self.cursor.execute("INSERT INTO {tn} ({c1},{c2}) VALUES ('{v1}', '{v2}')".format(tn=self.tablename,c1=self.col1, c2=self.col2, v1=val1, v2=val2))
            except Exception as err:
                print(err)
        self.connection.commit()

    def getValues(self):
        self.cursor.execute("SELECT * FROM {tn} ORDER BY {c2} DESC".format(tn=self.tablename, c2=self.col2))
        return self.cursor.fetchall()


def main():
    leaderboard = database('leaderboard', 'Name', 'Score')
    leaderboard.insert('Kevin', 20)
    leaderboard.insert('Joe', 2)
    leaderboard.insert('Jax', 30)
    print(leaderboard.getValues())

main()
