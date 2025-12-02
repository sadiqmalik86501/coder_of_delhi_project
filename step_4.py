import json 
def load_data(filename):
    with open(filename,"r")as f:
        data=json.load(f)
        return data
    
def find_page_you_might_like(user_id,data):
    user_pages={}
    for user in data["users"]:
        user_pages[user["id"]]=set(user["liked_pages"])
    if user_id not in user_pages:
        return []
    user_like_page=user_pages[user_id]
    page_suggection={}
    for other_user,pages in user_pages.items():
        if other_user!=user_id:
            shored_page=user_like_page.intersection(pages)
    for page in pages:
        if page not in user_like_page:
            page_suggection[page]=page_suggection.get(page, 0)+len(shored_page)
    shored_page=sorted(page_suggection.items(),key=lambda x:x[1],reverse=True)
    return [(page_id,scores) for page_id,scores in shored_page]

data=load_data("data.json")
user_id=1
page=find_page_you_might_like(user_id,data)
print(page)