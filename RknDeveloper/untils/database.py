from pymongo import MongoClient
from configs import rkn1

client = MongoClient(rkn1.MONGO_URI)

users = client['main']['users']
groups = client['main']['groups']

def already_db(user_id):
        user = users.find_one({"user_id" : str(user_id)})
        if not user:
            return False
        return True

def already_dbg(chat_id):
        group = groups.find_one({"chat_id" : str(chat_id)})
        if not group:
            return False
        return True

#async def add_user(self, b, m):
     #   u = m.from_user
       # if not await self.is_user_exist(u.id):
          #  user = self.new_user(u.id)
            #await self.col.insert_one(user)            
           # await send_log(b, u)
                
def add_user(user_id):
    in_db = already_db(user_id)
    if in_db:
        return
    return users.insert_one({"user_id": str(user_id)}) 

def is_user_exist(user_id):
    user = users.find_one({"user_id": str(user_id)})
    return bool(user)
        
def remove_user(user_id):
    in_db = already_db(user_id)
    if not in_db:
        return 
    return users.delete_one({"user_id": str(user_id)})
    
def add_group(chat_id):
    in_db = already_dbg(chat_id)
    if in_db:
        return
    return groups.insert_one({"chat_id": str(chat_id)})

def all_users():
    user = users.find({})
    usrs = len(list(user))
    return usrs

def all_groups():
    group = groups.find({})
    grps = len(list(group))
    return grps
