from typing import Any

# GROUPS = ["priest", "rogue", "warrior", "mage"]

class Character: 
    def __init__(self, name, group, equipment, level, inventory): 
        self.name = name
        self.abilities = self.compute_abilities()
        self.max_inventory = 10 # TODO: make this dependent on group
        self.inventory = inventory
        self.current_level = level
        return 

    def compute_abilities(self): 
        # TODO: compute abilities using classes, equipment, and current level
        base_health = 10 + (self.current_level * 2)
        equipment_health = sum([v.health for k, v in self.equipment.items()])

        self.abilities = {
            "health": base_health + equipment_health,
            "attack": 10,
            "special_attack": 10,
            "defense": 10,
            "special_defense": 10, 
            "speed": 10 # - 5 if encumbered
        }

    def get_equipment(self): 
        # e.g. {"head": "Helmet", "torso": "Armour", "legs": "Leggings", "feet": "Boots"}
        return self.equipment
    
    def equip(self, item): 
        body_part = item.body_part
        self.equipment[body_part] = item
        self.compute_abilities

    def pickup(self, item): 
        self.inventory.append(item)
        if len(self.inventory) > self.max_inventory: 
            self.encumbered = True
        return
    
    def drop(self, item):
        self.inventory.remove(item)
        if len(self.inventory) <= self.max_inventory: 
            self.encumbered = False
        return
    
    def level_up(self): 
        self.current_level += 1
        self.compute_abilities()
        return
    
    def __repr__(self, *args: Any, **kwds): 
        return f"Character(name={self.name}, level={self.current_level}, group={self.group})"
    
