import requests

# URL USUARIOS LOGIN
url = "http://localhost:5000/usuarios/login"

body = {
    "login": "usuario48",
    "senha": "12345"
}

bearer_token = ""

response = requests.post(url, json = body)

if response.status_code == 200:
    print("Sucesso: ", "\n", response.json())
    bearer_token = response.json().get("message")
    print(bearer_token)
else:
    print("Erro:  ", "\n", response.status_code, response.text)



# URL CATEGORIAS
url_categorias = "http://localhost:5000/categorias"

headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json"
}

categorias_response = requests.get(url_categorias, headers= headers)
print(categorias_response.json())
