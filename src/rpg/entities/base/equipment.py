from typing import Any
from rpg.entities.base import Item

class Equipment(Item):
    def __init__(self, name, description, properties, body_part): 
        super().__init__(name, description, properties)
        self.body_part = body_part
    
    def health(self): 
        return self.properties['health']
    
    def attack(self): 
        return self.properties['attack']
    
    def defense(self):
        return self.properties['defense']
    
    def special_attack(self):
        return self.properties['special_attack']
    
    def special_defense(self):
        return self.properties['special_defense']
    
    def speed(self):
        return self.properties['speed']

    def __repr__(self, *args: Any, **kwds):
        return super().__repr__(*args, **kwds)