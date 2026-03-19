import json
import shutil
import os

class Data_utilities:
    users_inventory = {}

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def load_users_inventory_data(self):
        self.users_inventory = json.loads(open("data/users_inventory.json", 'r').readlines()[0])
        print(f"after load {self.users_inventory}")

    def save_users_inventory_data(self):
        tmp = open("data/users_inventory.json.tmp", 'x')
        print(f"Dump ->  {json.dumps(self.users_inventory)}")
        tmp.write(json.dumps(self.users_inventory))
        tmp.close()
        shutil.copy2("data/users_inventory.json.tmp", "data/users_inventory.json")
        os.remove("data/users_inventory.json.tmp")

    def update_balance(self, user_id, new_balance):
        self.users_inventory[user_id]["money"] = new_balance
        self.save_users_inventory_data()
        self.load_users_inventory_data()

    def get_balance(self, user_id):
        print(f"before bal {self.users_inventory}")
        if(user_id in self.users_inventory.keys()):
            return self.users_inventory[user_id]["money"]
        else:
            print(f"Creating entry for user with id {user_id}")
            self.create_entry(user_id)
            self.save_users_inventory_data()
            return 0

    def create_entry(self, user_id):
        self.users_inventory[user_id] = {"money":0}
        print(f"CREATING ENTRY -> {self.users_inventory}")
        self.save_users_inventory_data()
        self.load_users_inventory_data()


    def get_users_inventory(self):
        return str(self.users_inventory)

data_utilities = Data_utilities()