class permissionDenied(Exception):
    def __init__(self, permission=None):
        self.message = 'User does not have the required permission "{}"'.format(permission)

        if permission == None:
            self.message = 'User does not have the required permissions'