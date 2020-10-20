from datetime import date
import requests
import math

username = 'fill this in with your username'
lvl_99_exp = 13034431
skills = ["Overall", "Attack", "Defence", "Strength", "Hitpoints", "Ranged", "Prayer", "Magic", "Cooking",
          "Woodcutting", "Fletching", "Fishing", "Firemaking", "Crafting", "Smithing", "Mining", "Herblore",
          "Agility", "Thieving", "Slayer", "Farming", "Runecrafting", "Hunter", "Construction"]
days_until_eoy = (date(2021, 1, 1) - date.today()).days

print(f"Querying OSRS hiscores API for player \'{username}\'... Please wait...")
response = requests.get(f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={username}")
print(f"OSRS hiscores API returned status code: \'{response.status_code}\'")
content_list = response.content.splitlines()
print(f"Days until EOY : {days_until_eoy}")
for i in range(0,len(skills)):
    entry = content_list[i].decode('UTF-8').split(',')
    level = entry[1]
    exper = entry[2]
    if level == '99' or i == 0:  # Don't bother with 99s or Overall
        continue
    print(f"{skills[i]}\n"
          f"  Level: {level}\n"
          f"  Exper: {int(exper):,}\n"
          f"Exp/day: {math.trunc((lvl_99_exp - int(exper)) / days_until_eoy):,}")

