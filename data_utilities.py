import json
import shutil
import os

users_inventory = {}

def load_users_inventory_data():
    users_inventory = json.loads(open("data/users_inventory.json", 'r').readlines()[0])
    print(users_inventory)

def save_users_inventory_data():
    tmp = open("data/users_inventory.json.tmp", 'x')
    tmp.write(json.dumps(users_inventory))
    tmp.close()
    shutil.copy2("data/users_inventory.json.tmp", "data/users_inventory.json")
    os.remove("data/users_inventory.json.tmp")

def update_balance(user_id, new_balance):
    users_inventory[user_id]["money"] = new_balance
    save_users_inventory_data()
    load_users_inventory_data()

def get_balance(user_id):
    if(user_id in users_inventory.keys()):
        return users_inventory[user_id]["money"]
    else:
        print(f"Creating entry for user with id {user_id}")
        create_entry(user_id)
        save_users_inventory_data()
        return 0

def create_entry(user_id):
    users_inventory[user_id] = {"money":0}
    save_users_inventory_data()
    load_users_inventory_data()