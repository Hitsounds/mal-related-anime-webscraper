import bs4
import requests
import json
import html

def _get_cors():
    name = input("Mal username: ")
    url = f"https://myanimelist.net/animelist/{name}"
    soup = bs4.BeautifulSoup(requests.get(url).text, features="html.parser")
    ani_ids = []
    unwatched = open(f"{name}.txt", "w")
    for i in json.loads(html.unescape(soup.find("table")["data-items"])):
        ani_ids.append(int(i["anime_id"]))
    for j in ani_ids:
        url = f"https://myanimelist.net/anime/{j}"
        soup = bs4.BeautifulSoup(requests.get(url).text, features="html.parser").find("table", {"class": "anime_detail_related_anime"})
        try:
            for i in soup.find_all("a"):
                prco = str(i).split("/")
                if prco[1] == "anime":
                    if int(prco[2]) not in ani_ids:
                        print(f"https://myanimelist.net/anime/{prco[2]}")
						unwatched.write(f"https://myanimelist.net/anime/{prco[2]}")
        except AttributeError:
            pass
    unwatched.close()

_get_cors()
