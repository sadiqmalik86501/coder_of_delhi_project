import json 

def cleaned_data(data):
    data["users"]=[user for user in data["users"] if user["name"].strip()]
    for user in data["users"]:
        user["friends"]=list(set(user["friends"]))
    data["users"]=[user for user in data["users"] if user["friends"] or user["liked_pages"]]
    unique_pages={}
    for page in data["pages"]:
        unique_pages[page["id"]]=page
        data["pages"]=list(unique_pages.values())
        return data
data=json.load(open("data.json"))
data=cleaned_data(data)
data_1=json.dump(data,open("cleaned_file.txt","w"),indent=4)
print(data_1)
print("Your Code is Successfully Run:")