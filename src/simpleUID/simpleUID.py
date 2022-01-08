import string as _string
import random
import secrets

#### 0123456789
digits = _string.digits

#### Return random integer value
def integer(length=6, prefix=None):

    #### Prefix should be of type int
    if not isinstance(prefix, int):
        raise Exception('Prefix should be of type int')
    
    randomInteger = int(''.join(random.choice(digits) for i in range(length)))

    if not prefix == None:
        randomInteger = prefix + randomInteger

    return randomInteger

#### Return random string value
def string(length=6, prefix=None):

    alphabet = _string.ascii_letters + _string.digits
    generated = ''.join(secrets.choice(alphabet) for i in range(length))

    if not prefix == None:
        generated = str(prefix) + generated

    return str(generated)

def password(length=10, prefix=None):

    alphabet = _string.ascii_letters + _string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break

    return password


### TODO create function to accept a database cursor
#### Function to create a unique ID for in the database....
# def uniqueID(table, column, stringLength=6, prefix=None):
#     idExists = True
#     while idExists:
#         randomID = self.randomStringDigits(stringLength, prefix=prefix)

#         with connections['FMM'].cursor() as cursor:
#             cursor.execute('SELECT * FROM {} WHERE {} = "{}"'.format(table, column, randomID))

#             if not len(cursor.fetchall()):
#                 idExists = False
    
#     return randomID