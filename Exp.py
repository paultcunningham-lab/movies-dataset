import pandas as pd
import requests
import io
import os
import streamlit as st
# Setup authentication and repository details
GITHUB_TOKEN =   st.secrets["TARGET_API"] 
OWNER = "paultcunningham-lab"
REPO = "silver-lamp"
FILE_PATH = "data.csv"  # e.g., "data/sales.csv"
BRANCH = "main"  # or "master"

def returner():
# GitHub REST API URL for raw content
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{FILE_PATH}?ref={BRANCH}"

    headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3.raw",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Read directly into a pandas DataFrame
        df = pd.read_csv(io.StringIO(response.text), header=None)
        st.write("CSV successfully loaded!")
        print(df.iloc[20,4])
        return df
    else:
        print(f"Failed to fetch file. Status code: {response.status_code}")
        return None
