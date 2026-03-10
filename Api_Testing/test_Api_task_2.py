import requests
import pytest


@pytest.fixture
def baseurl():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def resource():
    return ["posts", "comments", "albums", "photos", "todos", "users"]


# def test_nub_resource(baseurl,resource):
#     for r in resource:
#         responce = requests.get(f"{baseurl}/{r}")
#         data = responce.json()
#         print(f"{r}:",len(data))

#         assert responce.status_code == 200

# def test_get_resource(baseurl,resource):
#     for r in resource:
#         responce = requests.get(f"{baseurl}/{r}/1")
#         print(f"{r}:",responce.status_code)
#         assert responce.status_code == 200
#         assert "id" in responce.json()
#         print(responce.json())

# def test_update_resource(baseurl,resource):
#     update_data = {"title" : "Api testing"}
#     for r in resource:
#         responce = requests.put(f"{baseurl}/{r}/1",json=update_data)
#         print(f"{r}",responce.status_code)
        
#         assert responce.status_code == 200
#         assert "title" in responce.json()
#         print(responce.json())


# def test_delete_resource(baseurl,resource):
#     for r in resource:
#         responce = requests.delete(f"{baseurl}/{r}/1")
#         print(f"{r}",responce.status_code)
#         assert responce.status_code == 200

# def test_new_resource(baseurl,resource):

    
#     pass
        

def test_num_resourses(baseurl,resource):
    for r in resource:
        responce = requests.get(f"{baseurl}/{r}")
        data = responce.json()
        print(f"{r}:",len(data))

        assert responce.status_code == 200


def test_spicfic_data(baseurl,resource):
    for r in resource:
        responce = requests.get(f"{baseurl}/{r}/1")
        print(f"{r} statues",responce.status_code)
        assert responce.status_code == 200
        assert "id" in responce.json()
        # print(responce.json())

def test_modify_data(baseurl,resource):
    update_data = {"title" : "Api testing"}
    for r in resource:
        responce = requests.put(f"{baseurl}/{r}/1",json=update_data)
        print("{r} updated ststues:",responce.json)
        assert responce.status_code == 200
        assert "title" in responce.json()
        print(responce.json())

def test_delete_data(baseurl,resource):
    for r in resource:
        responce = requests.get(f"{baseurl}/{r}/1")
        print(f"{r}-delete staues:",responce.status_code)
        assert responce.status_code == 200
        print(responce.json())