
class Operations():

    def __init__(self, first, middle, last, yg, _id,
    title, isdn, author, bdate, rdate = None):
        self._first = first
        self._middle = middle
        self._last = last
        self._yg = yg
        self._id = _id
        self._title = title
        self._isdn = isdn
        self._author = author
        self._bdate = bdate
        self._rdate = rdate
        self.timeDateFix()
        self.dataQuery()

    def timeDateFix(self):
        """
        Displays the time and date in a easily understood format
        format - d/m/y
        """

        from PySide.QtCore import QDate
        currentDate = QDate.currentDate()
        day = str(currentDate.day())
        month = str(currentDate.month())
        year = str(currentDate.year())
        date = day + "/" + month + "/" + year
        self._bdate = str(date)

    def dataQuery(self):
        """creates a temporary dictionary that stores values collected from
           widgets in the programs __init__() method
        """
        tempDic = {}
        tempDic["First"] = self._first
        tempDic["Middle"] = self._middle
        tempDic["Last"] = self._last
        tempDic["yearGroup"] = self._yg
        tempDic["ID#"] = self._id
        tempDic["Title"] = self._title
        tempDic["ISDN"] = self._isdn
        tempDic["Author"] = self._author
        tempDic["Date Borrowed"] = self._bdate
        tempDic["Date Returned"] = self._bdate

        from database import Database

        data = Database()
        ls = [(self._first, self._middle, self._last, self._yg, self._id,
               self._title, self._isdn, self._author, self._bdate, self._rdate,
             )]

        data.add(ls)
        fob = open("data.dat", "a+b")

        for i in tempDic.keys():
            a = str(i + ": " + tempDic[i] + "\n")
            fob.write(a)
        fob.close()


def rowCount():
    """
    returns the number of rows in database
    """
    from database import Database
    data = Database()
    return data.getRowCount()
