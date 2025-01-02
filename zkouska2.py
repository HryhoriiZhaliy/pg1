import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
user_names = {
    1: "Leanne Graham",
    2: "Ervin Howell",
    3: "Clementine Bauch",
    4: "Patricia Lebsack",
    5: "Chelsey Dietrich",
    6: "Mrs. Dennis Schulist",
    7: "Kurtis Weissnat",
    8: "Nicholas Runolfsdottir V",
    9: "Glenna Reichert",
    10: "Clementina DuBuque"
}

def fetch_and_save_data():
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        
        for post in data:
            user_id = post.get('userId')
            post['userName'] = user_names.get(user_id, "Unknown User")
        
        
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        return True
    else:
        return False


from unittest.mock import patch, MagicMock, mock_open

def test_fetch_and_save_data():
    mock_data = [
        {"userId": 1, "id": 1, "title": "Test post", "body": "This is a test."}
    ]
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, json=MagicMock(return_value=mock_data), text=json.dumps(mock_data), content=json.dumps(mock_data))

        with patch("builtins.open", mock_open()) as mock_file:
            assert fetch_and_save_data() == True
            mock_file().write.call_args[0][0] == json.dumps([{
                "userId": 1,
                "id": 1,
                "title": "Test post",
                "body": "This is a test.",
                "userName": "Leanne Graham"
            }], indent=4)
