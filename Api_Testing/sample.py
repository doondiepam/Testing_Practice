# import requests
# print(requests.__version__)


# --------------------- Basic Commands ---------------------------------
# # response = requests.get("https://api.github.com")
# # print(response.status_code)
# # print(response.text)
# # print(response.headers)
# # print(response.json())


# -------------------------------------individual---------------------------------------
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.text)
# print(response.status_code)
# print(response.json()["title"])
# print(response.json().keys())
# print(response.json()["id"])
# print(len(response.json()))



 # ----------------------------------get by id-------------------------------
# import requests
# url = "https://jsonplaceholder.typicode.com/posts"
# response  = requests.get(url)

# find = response.json()

# for finds in find:
#     if finds['userId'] == 1:
#         print(finds['title'])

#--------------------------------check the time------------------------

# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# responce = requests.get(url)

# print(responce.elapsed.total_seconds())



#---------------------Validate header (Content-Type)-----------------------------------
# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.get(url)

# print(response.headers['Content-Type'])



# import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": "my post",
#     "body": "hello API",
#     "userId": 10
# }

# response = requests.post(url, json=data)

# print(response.json()['id'])
# print(response.json().keys())
# print(response.json())

import requests

base_url = "https://jsonplaceholder.typicode.com"

resources = [
    "posts",
    "comments",
    "albums",
    "photos",
    "todos",
    "users"
]

print("----- Verify number of resources -----")

for r in resources:
    response = requests.get(f"{base_url}/{r}")
    data = response.json()

    print(r,len(data))
    assert response.status_code == 200  


print("\n----- Get specific resource -----")

for r in resources:
    response = requests.get(f"{base_url}/{r}/1")

    print(r, response.status_code)
    print("Body:", response.json())
    assert response.status_code == 200
    assert "id" in response.json()

print("\n----- Modify resource (PUT) -----")

update_data = {
    "title": "Updated Title"
}

for r in resources:
    response = requests.put(f"{base_url}/{r}/1", json=update_data)

    print(f"{r} PUT status:", response.status_code)
    print("Body:", response.json())

    assert response.status_code == 200


print("\n----- Delete resource -----")

for r in resources:
    response = requests.delete(f"{base_url}/{r}/1")

    print(f"{r} DELETE status:", response.status_code)
    print("Body:", response.json())

    assert response.status_code == 200


print("\n----- Create resource -----")

new_data = {
    "title": "My Title",
    "body": "My Body",
    "userId": 1
}

for r in resources:
    response = requests.post(f"{base_url}/{r}", json=new_data)

    print(f"{r} POST status:", response.status_code)
    print("Body:", response.json())

    assert response.status_code == 201