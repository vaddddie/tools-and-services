import requests

url = 'https://randomuser.me/api/'

def get_random_users(count: int):
    params = {
        'results': count
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()['results']
            return data
    
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при выполнении запроса: {e}")

