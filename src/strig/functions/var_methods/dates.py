from datetime import datetime
from typing import Optional


class DateMethods:
    today: Optional[datetime] = None

    def __get_today__(self):
        self.today = datetime.today()

    def yyyy(self):
        if self.today == None:
            self.__get_today__()

        return self.today.year

    def yy(self):
        if self.today == None:
            self.__get_today__()

        return str(self.today.year)[-2:]

    def mm(self):
        if self.today == None:
            self.__get_today__()

        month = str(self.today.month)
        if len(month) == 2:
            return month

        return "0" + month

    def m(self):
        return self.today.month

    def dd(self):
        if self.today == None:
            self.__get_today__()

        day = str(self.today.day)
        if len(day) == 2:
            return day

        return "0" + day

    def d(self):
        return self.today.day
