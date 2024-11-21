import random

# Define race and class options
race_classes = {
    'Human': ['Mage', 'Warlock', 'Warrior', 'Priest', 'Paladin', 'Rogue'],
    'Orc': ['Warrior', 'Warlock', 'Shaman', 'Hunter', 'Rogue'],
    'Night Elf': ['Warrior', 'Priest', 'Rogue', 'Hunter', 'Druid'],
    'Undead': ['Mage', 'Warlock', 'Priest', 'Rogue', 'Warrior'],
    'Dwarf' : ['Warrior', 'Priest', 'Paladin', 'Hunter', 'Rogue'],
    'Gnome': ['Mage', 'Warlock', 'Rogue', 'Warrior'],
    'Tauren': ['Warrior', 'Shaman', 'Druid', 'Hunter'],
    'Troll': ['Warrior', 'Priest', 'Shaman', 'Hunter', 'Mage', 'Warlock']
}

def roll_race(faction: str):
    if faction.lower() == 'horde':
        return random.choice(['Orc', 'Undead', 'Troll', 'Tauren'])
    elif faction.lower() == 'alliance':
        return random.choice(['Human', 'Dwarf', 'Night Elf', 'Gnome'])
    else:
        return random.choice(list(race_classes.keys()))

def roll_class(race):
    return random.choice(race_classes[race])

def get_image(hero_class: str):
    if hero_class in ["Priest", "Mage"]:
        return "data/imgs/mage.webp"
    elif hero_class in ["Paladin", "Warrior"]:
        return "data/imgs/warrior.webp"
    elif hero_class in ["Rogue"]:
        return "data/imgs/rogue.webp"
    else:
        return ""

def generate_character(faction: str):
    hero_race = roll_race(faction)
    hero_class = roll_class(hero_race)
    hero = f'{hero_race} {hero_class}'
    return hero, get_image(hero_class)