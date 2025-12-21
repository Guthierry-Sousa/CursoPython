import requests

def verificar_conexao_internet(url = 'https://www.pudim.com.br', timeout = 5):

    try:

        response = requests.get(url, timeout=timeout)

        if response.status_code == 200:

            return True
        
        else:

            return False
        
    except requests.ConnectionError:

        return False
    
    except requests.Timeout:

        return False
    
if verificar_conexao_internet():

    print("Foi possível acessar o site pudim.")

else:

    print("Não foi possível acessar o site pudim.")
