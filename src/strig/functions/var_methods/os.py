import platform

class OsMethods:
    def system(self): 
        return platform.system()

    def release(self): 
        return platform.release()        

    def version(self): 
        return platform.version()        
