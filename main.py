from dotenv import load_dotenv

import os
import requests
import yaml

BASE_AUTH_URL = "https://auth.apps.paloaltonetworks.com/auth/v1/oauth2/access_token"

HEADERS = {
    "Accept": "application/json",
}

BASE_URL = "https://api.strata.paloaltonetworks.com/config/deployment/v1/"

AUTH_HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
}

load_dotenv()
TSG_ID = os.environ.get("TSG_ID")
CLIENT_ID = os.environ.get("CLIENT_ID")
SECRET_ID = os.environ.get("SECRET_ID")


def create_token():
    auth_url = f"{BASE_AUTH_URL}?grant_type=client_credentials&scope:tsg_id:{TSG_ID}"

    token = requests.request(
        method="POST",
        url=auth_url,
        headers=AUTH_HEADERS,
        auth=(CLIENT_ID, SECRET_ID),
    ).json()
    HEADERS.update({"Authorization": f'Bearer {token["access_token"]}'})


def read_yaml_file():
    with open('dns.yaml', 'r') as f:
        dns_list = yaml.safe_load(f)
    return(dns_list)

def create_dns_server(dns_config):
    url = f"{BASE_URL}internal-dns-servers"
    payload = {
        "name": dns_config["name"],
        "domain_name": dns_config["domain_name"],
        "primary": dns_config["primary"],
        "secondary": dns_config["secondary"],
    }
    print(payload)
    requests.request(method="POST", url=url, headers=HEADERS, data=payload).json()


if __name__ == "__main__":
    create_token()
    dns_list = read_yaml_file()
    for dns_config in dns_list:
        create_dns_server(dns_config=dns_config)
