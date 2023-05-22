import get_source
from bs4 import BeautifulSoup

update_source = input("Would you like to update the source html file for more accurate data? y/n")
if update_source.lower() == "y":
    get_source.update_html()

def get_stats():
    data = []

    with open("website.html") as file:
        html = file.read()

    soup = BeautifulSoup(html, "html.parser")

    for tr in soup.find_all("tr"):
        #Collect data if playerCol exists
        player_col = tr.find("td", class_="playerCol")
        if player_col:
            player_name = player_col.find("a").text
            kd_diff = tr.find("td", "kdDiffCol").text
            rating = tr.find("td", "ratingCol").text
            stats_details = tr.find_all("td", class_="statsDetail")
            maps = stats_details[0].text
            rounds = stats_details[1].text
            kd = stats_details[2].text

            entry = {
                "player_name": player_name,
                "kd_diff": kd_diff,
                "rating": rating,
                "maps": maps,
                "rounds": rounds,
                "kd": kd
            }
            # Append the entry to the data list
            data.append(entry)
    return data





