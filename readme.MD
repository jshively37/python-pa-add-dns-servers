# Overview
This Python script adds Internal DNS servers to Strata Cloud Manager Prisma Access from a YAML file.

## Requirements
```
black              26.1.0
certifi            2026.1.4
charset-normalizer 3.4.4
click              8.3.1
idna               3.11
mypy_extensions    1.1.0
packaging          25.0
pathspec           1.0.3
pip                25.3
platformdirs       4.5.1
python-dotenv      1.2.1
pytokens           0.4.0
PyYAML             6.0.3
requests           2.32.5
urllib3            2.6.3
```

## Creating a service account in Prisma Access

You will need to create a service account in Prisma Access to generate the access token.

The Client ID, Secret ID, and TSG ID will be saved in the .env file.

To create a service account: https://pan.dev/sase/docs/service-accounts/


## Installing and running

Clone down this repo and cd into the directory.

Create a Python virtual environment: python -m venv venv

Activate the virtual environment: \
Windows: .\venv\Scripts\activate \
OSX: source venv/bin/activate \

Install the dependencies using `pip install -r requirements.txt`

Rename `.env.example` to `.env` and populate your variables in this file generated while creating the service account. The .env is included in the .gitignore to ensure it does not accidentally get checked into a git repo.

Modify the `dns.yaml` to reflect your desired state.

Run: `python main.py`

The output will be displayed to the screen.
