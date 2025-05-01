class Bonus:
    def __init__(self, bonus_type, value):
        self.type = bonus_type
        self.value = value

class Role:
    def __init__(self, class_name, bonus, bonus_value):
        self.class_name = class_name
        self.bonus = Bonus(bonus, bonus_value)

class Weapon:
    def __init__(self, id, name, damage):
        self.id = id
        self.name = name
        self.damage = damage

class Character:
    def __init__(self, id, name, skin, health, role, weapons):
        self.id = id
        self.name = name
        self.skin = skin
        self.health = health
        self.role = Role(**role)
        self.weapons = [Weapon(**weapon) for weapon in weapons]

class User:
    def __init__(self, id, username, characters):
        self.id = id
        self.username = username
        self.characters = [Character(**character) for character in characters]

class Match:
    def __init__(self, id, name, characters):
        self.id = id
        self.name = name
        self.characters = [Character(**character) for character in characters]
