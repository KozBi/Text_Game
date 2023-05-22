import pathlib
from pathlib import Path
from clas_Item import Tool
from clas_Item import Substract

from class_Player import Player
from class_Room import Room
from class_Room import Kitchen

HELP_txt=pathlib.Path(r"C:\Users\kozlo\OneDrive\Pulpit\Game-Coocking\HELP.txt")
with HELP_txt.open(mode="r", encoding="utf-8") as file:
    HELP=file.read()

# kitchen= {"name" : "kitchen",
#           "item" : []}

storage= {"name" : "storage",
          "tool" : ["pan", "knife"]}

pantry= {"name" : "pantry",
          "item" : ["uncut vegetables" , "uncut vegetables", "raw meat" ,"raw meat"],
          "substract": ["burger bun" , "burger bun"]}

# kitchen= {"name" : "kitchen",
#           "item" : [],
#           "substract": ["burger bun" , "burger bun","burger meat","vegetables","vegetables","burger meat","vegetables"]}

kitchen= {"name" : "kitchen",
          "item" : [],
          "substract": []}


class Game:


    player=Player()

    @classmethod
    def start(cls):
        print(f"{cls.player.name} You're in the kitchen. You need to make 2 burgers. You need burger buns, meat and vegetables. You'll find them in the pantry." "\n" 
                "To make it, you need tools: a pan and a knife. Bring everything to the Kitchen and use knife and pan. That's all, 2 burgers will be created" "\n" 
                "Write /help to get info about commands.")
        
        cls.Kitchen = Kitchen(**kitchen)
        cls.Storage = Room(**storage)
        cls.Pantry = Room(**pantry)

        cls.current_room = cls.Kitchen     
    
    def _describe_me(cls):
        if   cls.player.items ==[]:
            print(f"{cls.player.name}, you are in the {cls.current_room.name}, you dont have any tools")
        else:
            print(f"{cls.player.name}, you are in the {cls.current_room.name}, your tools are: ")
            for item in cls.player.items:
                print (f"{item}") 
            
        
    @classmethod
    def action(cls):
        command = input("Type your action or /help ").lower()
        match command:
            case "/help":
                print(HELP)
            case "/me":
                cls._describe_me(cls)
            case "/move":               
                cls.move(cls)
            case "/get":
                if len(cls.player.items) >3:
                    print ("Your inventory is already full")
                elif cls.current_room.items:                
                    cls.get((cls),input("Which item: ").lower())
                else: print("This room is empty")
            case "/drop":    
                if cls.player.items:           
                    cls.drop((cls),input("Which item: ").lower())
                else: print("You have nothing") 
            case "/use":
                if cls.current_room.name != "kitchen":    
                    print("You can use tools only in kitchen") 
                else:cls.use_tool((cls),input("Which item: ").lower())    
            case _:
                print("This commend is unknow, you can ask for /help")

    
    def move(cls):
        target = (input("Write '1' to move to kitchen \nWrite '2' to move to pantry \nWrite '3' to Move to storage \n "))
        match target:
            case "1":
                cls.current_room = cls.Kitchen 
            case "2":
                cls.current_room = cls.Pantry
            case "3":
                cls.current_room = cls.Storage 
            case _:
                print("Try again")      
                return True 
        print(f"You are now in {cls.current_room.name}. You can find here: {cls.current_room.items}")
        for item in cls.current_room.items:
                print (f"{item}") 

    
    def get(cls, item):
        found_item = None       
        for room_item in cls.current_room.items:
            if room_item.name == item:
                found_item = room_item
                break
        if found_item:
            cls.current_room.items.remove(found_item)
            cls.player.take_item(found_item)
            print (f"You have now {cls.player.items}.")
        else: print (f"You cannot find {item} here")


    def drop(cls, item):
        if item=="all":
            cls.current_room.items.extend(cls.player.items)
            cls.player.items=[]
            print(f"You've dropped all. You can find now here {cls.current_room.items}")
        else:
            for player_item in cls.player.items:   
                if player_item.name == item:           
                    cls.player.drop_item(player_item)
                    cls.current_room.items.append(player_item)
                    print(f"You've dropped {player_item}")
                    break
            else: print (f"You don't have {item} ")




    def use_tool(cls,tool):
        if cls.player.items:    
            for item in cls.player.items:
                    if item.name ==tool=="knife":
                        item.CutVegetables(cls.current_room)
                        return True
                    elif item.name ==tool =="pan":
                        item.cookMeat(cls.current_room)      
                        return True           
                    else: print(f"You cannot use {tool}")
        else: print(f"You cannot use{tool}")

    @classmethod
    def win_check(cls) -> bool:
        required_ingredients = [("burger bun", 2), ("burger meat", 2), ("vegetables", 2)]
        for ingredient, count in required_ingredients:
            # add to generator object 1 if item.name ==ingredient and then sum the generator value #using_generator not a list!
            ingredient_count = sum(1 for item in cls.Kitchen.items if item.name == ingredient) 
            if ingredient_count < count:
                return False
        return True