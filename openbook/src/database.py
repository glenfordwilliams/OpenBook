import sqlite3


class Database(object):

    def __init__(self):
        self.conn = sqlite3.connect("library.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS library
                        (First Name text , Middle text, Last text, Year text,
                             ID text, Title text,
                             ISDN text,
                             Author text,
                         Borrowed text, Returned text)
                        ''')

    def add(self, dic):
        """
        stores all data in the SQLite Database
        """
        self.__init__()
        self.cursor.executemany('''INSERT into library values
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', dic)
        print "added"

    def closeDatabase(self):
        """point of exit for database"""
        self.conn.commit()
        self.conn.close()
        print "Database Closed"

    def viewDatabase(self):
        print "viewpoint open"
        self.__init__()
        self.cursor.execute('SELECT * FROM library')
        self.populate = self.cursor.fetchall()
        return self.populate

    def remove(self):
        pass

    def getRowCount(self):
        """ returns the total number of rows in our table"""
        _all = self.cursor.fetchall()
        print len(_all)

    def search(self):
        pass

    def update(self):
        pass

    def show(self):
        from PySide.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("library.db")
        self.db.open()

        projectModel = QSqlTableModel()
        projectModel.setTable("library")
        projectModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        projectModel.select()
        query = QSqlQuery()
        query.exec_("SELECT * FROM library")

        projectModel.setQuery(query)
        return projectModel
