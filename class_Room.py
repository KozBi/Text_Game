from clas_Item import Item
from clas_Item import Substract
from clas_Item import Tool


class Room:
    def __init__(self, **kwargs) -> None:
        self.name = kwargs["name"]
        self.items=[]

        for new_object in kwargs.keys():
            if new_object =="item":            
                for n in kwargs["item"]:
                    self.items.append((Item(n)))     

            if new_object =="tool":   
                for n in kwargs["tool"]:                
                    self.items.append((Tool(n)))     

            if new_object =="substract":   
                for n in kwargs["substract"]:              
                    self.items.append((Substract(n)))   

    def describe_items(self):
        _list=[]
        try:
            for i in self.items:
                _list.append(str(i))
        except:
            _list=[]
        return _list

class Kitchen(Room):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
                    