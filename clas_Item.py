

class Item:
    def __init__(self, name=None) -> None:
        self.name = name
        
    def __repr__(self) -> str:
        return f"{self.name}"
    
    def __str__(self) -> str:
        return f"{self.name}"
    

class Substract(Item):
    def __init__(self, name) -> None:
        super().__init__(name)  

    def __eq__(self, other): # it is required for win_check method()
        if isinstance(other, Substract):
            return self.name == other.name
        return False

class Tool(Item):
    def __init__(self, name) -> None:
        super().__init__(name)

    def CutVegetables(self,room):
        found = False
        for vege in list(room.items):           #iteration for copy a list, room items is changed in code below so it would have been overwritten !!! 
            if vege.name == "uncut vegetables":
                room.items.remove(vege)
                room.items.append(Substract("vegetables"))
                found = True
                print(f"You've cut vegetables, they are ready to be used in a burger.")
        if not found:
            print("There is nothing to cut here")

    def cookMeat(self,room):
        found = False
        for meat in list(room.items):           #iteration for copy a list, room items is changed in code below so it would have been overwritten !!! 
            if meat.name == "raw meat":
                room.items.remove(meat)
                room.items.append(Substract("burger meat"))
                found = True
                print(f"You've cooked meat, it's ready to be used in a burger.")
        if not found:
                print("There is nothing to cook here")


    



