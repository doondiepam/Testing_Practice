# import requests
# def test_prac():
#     responce = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/3",headers=head)
#     head = {
#         'Accept':'plain/text'
#     }

#     result = responce.status_code
#     result1 = responce.json()
#     assert result == 200
#     assert isinstance(result1, dict)

import requests

def test_prac():
    head = {
        'Accept': 'plain/text'
    }

    response = requests.get(
        "https://fakerestapi.azurewebsites.net/api/v1/Activities/3",
        headers=head
    )

    result = response.status_code
    response_json = response.json()  

    assert result == 200
    assert isinstance(response_json, dict)  
    print(result)
    print(response_json)