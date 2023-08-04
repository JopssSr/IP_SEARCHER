import socket
import requests
import time

def buscar_info_ip_socket(ip):
    try:
        host = socket.gethostbyaddr(ip)
        print(f"Host associated with IP  {ip}: {host[0]}")
    except socket.herror:
        print(f"Unable to find host associated with IP {ip}")

def buscar_info_ipinfo(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"IP INFORMATIONS  {ip} (via ipinfo.io):")
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print("Unable to fetch information for this IP.")

def buscar_info_ipapi(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"IP INFORMATIONS {ip} (via ip-api.com):")
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print("Unable to find host associated with IP.")
        
def main():
    # Impressão do banner e informações de contato
    print("\033[31m_____________IP SEARCHER_______________\033[31m")
    print("\033[31m©️Copyright by 𝚅𝟷𝙽𝙶𝟺𝙳𝟶\033[31m𝚁")
    print("\033[36mContatos:\033[36m")
    print("Discord: 𝚅𝟷𝙽𝙶𝟺𝙳𝟶𝚁_𝐶𝑟𝑦#0942")
    print("Email: vingadorbps@gmail.com")
    print("Versão: 1.0 beta")
    print("───────────────────")
    
    ip = input("DESIRED IP: ")
    print("looking for informations...")
    time.sleep(5)
    
    buscar_info_ip_socket(ip)
    print()  # Adiciona uma linha em branco para separar as informações
    buscar_info_ipinfo(ip)
    print()  # Adiciona uma linha em branco para separar as informações
    buscar_info_ipapi(ip)
    print()  # Adiciona uma linha em branco para separar as informações

if __name__ == "__main__":
    main()