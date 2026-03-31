
class data:
    def __init__(self,data:list):
        self.data=data
    
    def __str__(self):
        rval=""
        for x in self.data:rval+="\n"+x
        return rval
    
