import requests
from bs4 import BeautifulSoup
import pandas as pd


df = pd.DataFrame([], columns=["id","name","difficulty","tags"])
for page in range(1,61):
    resp = requests.get("https://codeforces.com/problemset/page/{}".format(page));
    prob_page = BeautifulSoup(resp.text, features="html.parser")
    prob_tab = prob_page.find("table", class_="problems")
    probs = prob_tab.find_all("tr")
    for prob in probs:
        table_data = prob.find_all("td")
        if len(table_data)>0:
            prob_id = table_data[0]
            prob_name = table_data[1].find_all("div")[0]
            prob_tags = table_data[1].find_all("div")[1]
            submit = table_data[2]
            difficulty = table_data[3]
            submissions = table_data[4]
            tags = " ".join(prob_tags.get_text().split());
            tg = ""
            for idx, item in enumerate(tags.split(",")):
                tg = tg + "tag{}={},".format(idx, item.strip())
            df= df.append({"id":  prob_id.get_text().strip(), "name": prob_name.get_text().strip(), "difficulty": difficulty.get_text().strip(), "tags": tg}, ignore_index=True)

df.to_csv("my_txt.csv",index=False)


