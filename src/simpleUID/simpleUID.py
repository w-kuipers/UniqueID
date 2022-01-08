import string as _string
import random

#### 0123456789
lettersAndDigits = _string.digits

#### Return random integer value
def integer(length=6, prefix=None):

    print(prefix)

    #### Prefix should be of type int
    if not isinstance(prefix, int):
        raise Exception('Prefix should be of type int')
    
    randomInteger = int(''.join(random.choice(lettersAndDigits) for i in range(length)))

    #### Add prefix
    if not prefix == None:
        randomInteger = int(str(prefix) + str(randomInteger))
        
    return randomInteger

#### Return random string value
def string(length=6, prefix=None):
    randomString = int(''.join(random.choice(lettersAndDigits) for i in range(length)))

    if not prefix == None:
        randomString = prefix + str(randomString)

    return str(randomString)


#### Check database cursor....
def database(cursor, **kwargs):
    
    print(kwargs)

    method = 'string' if not 'method' in kwargs else kwargs['method']
    del kwargs['method'] #### Kwargs need to be passed to generation functions

    idExists = True

    count = 1
    while idExists:

        generatedID = string(**kwargs) if method == 'string' else integer(**kwargs) if method == 'integer' else None

        cursor['cursor'].execute('SELECT "{}" FROM {} WHERE {} = "{}"'.format(cursor['column'], cursor['table'], cursor['column'], generatedID))

        if not len(cursor['cursor'].fetchall()):
            idExists = False

        count += 1

    return generatedID