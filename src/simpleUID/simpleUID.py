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
    
    random_integer = int(''.join(random.choice(digits) for i in range(length)))

    #### Add prefix
    if not prefix == None:
        random_integer = int(str(prefix) + str(random_integer))
        
    return random_integer

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


#### Check database cursor....
def database(cursor, *args, **kwargs):
    
    method = 'string' if not 'method' in kwargs else kwargs['method']
    del kwargs['method'] #### Kwargs need to be passed to generation functions, method is useless here

    id_exists = True

    count = 1
    while id_exists:

        generated_id = string(*args, **kwargs) if method == 'string' else integer(*args, **kwargs) if method == 'integer' else None

        cursor['cursor'].execute('SELECT "{}" FROM {} WHERE {} = "{}"'.format(cursor['column'], cursor['table'], cursor['column'], generated_id))

        if not len(cursor['cursor'].fetchall()):
            id_exists = False

        count += 1

    return generated_id