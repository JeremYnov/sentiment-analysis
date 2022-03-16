import requests
import csv
import os
import pandas as pd
import time
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root


class Cryptopanic:
    def __init__(
        self,
        path_to_login=os.path.join(ROOT_DIR, "data", "cryptopanic_login.csv"),
        filters=["BTC"],
        regions=["en"],
    ):
        self.path_to_login = path_to_login
        self.filters = filters
        self.regions = regions

    def getTokens(self):
        credentials = []
        with open(self.path_to_login, "r") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                credentials.append(row)
        # Don't return headers
        return credentials[1]

    def getDataCryptopanic(self):
        news_processed = []
        url = "https://cryptopanic.com/api/v1/posts/?auth_token={token}&currencies={filters}&regions={regions}".format(
                token=self.getTokens()[0],
                filters=",".join(self.filters),
                regions=",".join(self.regions),
            )
        while True:
            page = requests.get(url)
            data = page.json()
            news = data["results"]
            next = data["next"]
            
            for element in news:
                news_processed.append(
                    {
                        "ID": element["id"],
                        "Text": element["title"],
                        "URL": element["url"],
                        "Created_at": element["created_at"],
                    }
                )
                print(type(element["created_at"]))
            url = next
            time.sleep(1)
            
            if not next:
                break

        df = pd.DataFrame(news_processed)
        print(f"news= {df}")
        return df
