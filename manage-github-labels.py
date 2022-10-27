# =========================================================================================
# manage-github-labels.py
# =========================================================================================
# Script to check manage GitHub labels.
# =========================================================================================
import argparse
import requests
from github import Github
from pprint import pprint

# =========================================================================================
# Get parameters
# =========================================================================================
parser = argparse.ArgumentParser()
parser.add_argument("-o", type=str, dest="OWNER", help="This is the GitHub owner of the repository", required=True)
parser.add_argument("-r", type=str, dest="REPOSITORY", help="This is the name of the repository", required=True)
args = parser.parse_args()

# =========================================================================================
# GitHub object
# =========================================================================================
ourGithub = Github()

# github username
username = args.owner
# url to request
url = f"https://api.github.com/users/{username}"
# make the request and return the json
user_data = requests.get(url).json()
# pretty print JSON data
pprint(user_data)