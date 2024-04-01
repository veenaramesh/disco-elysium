from typing import Any 

class Item: 
    def __init__(self, name, description, properties=[]): 
        self.name = name
        self.description = description

    def __eq__(self, other): 
        if isinstance(other, Item): 
            return self.name == other.name
        else: 
            return NotImplemented  

    def __repr__(self, *args: Any, **kwds):
        return f"Item(name={self.name}, description={self.description}, properties={self.properties})"

