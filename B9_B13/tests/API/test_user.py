from API.userAPI import UserAPI
import string

def get_path_safe(payload, path):
    cur = payload
    for p in path.split("."):
        if p.endswith("]"):
            key, idx = p[:-1].split("{")
            cur= cur[key][int(idx)]
        else:
            cur = cur[p]
    return cur   

def test_get_all_users(api_context):
    user = UserAPI(api_context)
    response = user.get_user()
    data = response.json()
    print(data["list"][0]["createdAt"])
    assert response.status == 200
   
    