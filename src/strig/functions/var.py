from typing import Optional, List, Literal, TypedDict
from datetime import datetime, Typ

class Methods:
    today: Optional[datetime]

    def __get_today__(self):
        self.today = datetime.today()

    def yyyy(self): 
        if self.today == None:
            self.__get_today__()
        
        return self.today.year
        
# def parse_varstring(varstring: str) -> List[Methods]:
#     for i, var in enumerate(varstring.split("%")):
#         if i == 0: continue ## Varstring starts with %
#          
#
#     return []

def var(varstring: str, prefix: Optional[str] = None):
    """
    Generate a string from specified variables
    """

    vars: List[Methods] = []
    for i, var in enumerate(varstring.split("%")):
        if i == 0: continue ## Varstring starts with %

    vars["yyyy"]

    return
