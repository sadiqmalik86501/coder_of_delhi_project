import json
def load_data(filename):
    with open(filename,"r") as f:
        data=json.load(f)
        return data
def find_know(user_id,data):
    user_friends={}
    for user in data["users"]:
        user_friends[user["id"]]=set(user["friends"])
    if user_id not in user_friends:
        return data
    direct_friends=user_friends[user["id"]]
    suggection={}
    for friend in direct_friends:
        for mutual in user_friends.get(friend,[]):
            if mutual!=user_id and mutual not in direct_friends:
                suggection[mutual]=suggection.get(mutual, 0)+1
    sorted_suggection=sorted(suggection.items(),key=lambda x:x[1], reverse=True)
    return [suggection_id for suggection_id,_ in sorted_suggection]
data=load_data("data.json")
user=20
rce=find_know(user,data)
print(rce)