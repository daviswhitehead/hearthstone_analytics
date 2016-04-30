import requests


cards = requests.get(
	'https://api.hearthstonejson.com/v1/latest/enUS/cards.json'
).json()

cards_collectible = requests.get(
	'https://api.hearthstonejson.com/v1/latest/enUS/cards.collectible.json'
).json()

cardbacks = requests.get(
	'https://api.hearthstonejson.com/v1/latest/enUS/cardbacks.json'
).json()

l = [cards, cards_collectible, cardbacks]
for i in l:
	print(i)
