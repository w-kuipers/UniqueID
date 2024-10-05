from typing import Optional, Callable
from datetime import datetime
import inspect

class Methods:
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

    def dd(self):
        if self.today == None:
            self.__get_today__()

        day = str(self.today.day)
        if len(day) == 2: 
            return day

        return "0" + day

def var(varstring: str, prefix: Optional[str] = None, methods: Callable = Methods):
    """
    Generate a string from specified variables
    """

    generated = ""

    method_names = [i[0] for i in inspect.getmembers(methods, predicate=inspect.isfunction)]
    methods = methods()

    for i, var in enumerate(varstring.split("%")):
        if i == 0: continue ## Varstring starts with %
        if not var in method_names:
            raise TypeError(f"Unrecognized variable '{var}'")

        generated += getattr(methods, var)()

    if not prefix == None:
        generated = prefix + generated
    
    return generated
