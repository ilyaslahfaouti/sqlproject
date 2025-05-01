import pymongo

# Connexion à la base de données
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["jeu_multijoueur"]

# Vérifier la connexion
print("Bases de données disponibles :", client.list_database_names())

# Création des collections
users = db["users"]
characters = db["characters"]
roles = db["roles"]
weapons = db["weapons"]
matches = db["matches"]

# Insertion des données de test
user_data = {
    "id": 1,
    "username": "joueur1",
    "characters": [
        {
            "id": 1,
            "name": "Guerrier",
            "skin": {"color": "rouge", "taille": 180},
            "health": 100,
            "role": {
                "class": "tank",
                "bonus": "Armour",
                "bonusValue": 20
            },
            "weapons": [
                {"id": 1, "name": "Épée", "damage": 30},
                {"id": 2, "name": "Bouclier", "damage": 10}
            ]
        },
        {
            "id": 2,
            "name": "Mage",
            "skin": {"color": "bleu", "taille": 160},
            "health": 80,
            "role": {
                "class": "mage",
                "bonus": "Damage",
                "bonusValue": 15
            },
            "weapons": [
                {"id": 3, "name": "Bâton de mage", "damage": 25}
            ]
        }
    ]
}

# Insertion de l'utilisateur
users.insert_one(user_data)

# Suppression des doublons dans la collection characters
characters.delete_many({"id": 3})  # Suppression de tous les personnages avec id 3

# Insertion ou mise à jour des personnages dans la collection characters
characters_data = [
    {
        "id": 1,
        "name": "Guerrier",
        "skin": {"color": "rouge", "taille": 180},
        "health": 100,
        "role": {
            "class": "tank",
            "bonus": "Armour",
            "bonusValue": 20
        },
        "weapons": [
            {"id": 1, "name": "Épée", "damage": 30},
            {"id": 2, "name": "Bouclier", "damage": 10}
        ]
    },
    {
        "id": 2,
        "name": "Mage",
        "skin": {"color": "bleu", "taille": 160},
        "health": 80,
        "role": {
            "class": "mage",
            "bonus": "Damage",
            "bonusValue": 15
        },
        "weapons": [
            {"id": 3, "name": "Bâton de mage", "damage": 25}
        ]
    },
    {
        "id": 3,
        "name": "Archer",
        "skin": {"color": "vert", "taille": 175},
        "health": 90,
        "role": {
            "class": "archer",
            "bonus": "Damage",
            "bonusValue": 18
        },
        "weapons": [
            {"id": 4, "name": "Arc", "damage": 35}
        ]
    }
]

# Insertion ou mise à jour des personnages
for char in characters_data:
    characters.update_one({"id": char["id"]}, {"$set": char}, upsert=True)

# Lecture d'un personnage
try:
    character = characters.find_one({"id": 1})
    if character:
        print("Personnage :", character)
    else:
        print("Aucun personnage trouvé avec l'ID 1.")
except Exception as e:
    print("Erreur lors de la lecture du personnage :", e)

# Mise à jour d'un personnage
characters.update_one(
    {"id": 1},
    {"$set": {"health": 120}}
)

# Suppression d'un personnage
characters.delete_one({"id": 2})

# Ajout d'une arme
characters.update_one(
    {"id": 1},
    {"$push": {"weapons": {"id": 5, "name": "Dague", "damage": 15}}}
)

# Modification du bonus d'un rôle
characters.update_many(
    {"role.class": "tank"},
    {"$set": {"role.bonusValue": 25}}
)

# Vérification finale des personnages
all_characters = characters.find()
print("Tous les personnages :")
for char in all_characters:
    print(char)
