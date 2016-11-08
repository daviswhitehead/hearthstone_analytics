#!/usr/bin/env python

import sys
import ujson as json
import pandas as pd
import pdb
from collections import defaultdict
from collections import Counter
import pprint


def


def recursive_finder(d, k, v):
	"""
	Recursively handles adding unique values to unique keys.
	"""

	if type(v) == dict:
		d[k] = defaultdict(set)
		for kk, vv in d[k].iteritems():
			d[k] = recursive_finder(d[k], kk, vv)
	elif type(v) == list:
		for i in v:
			d = recursive_finder(d, k, i)
	else:
		v = data_formatter(v)
		d[k].add(v)

	return d


def find_uniques(data):
	"""
	Takes in a list of dictionaries and gets all possible unique
	key value pairs.
	"""

	d = defaultdict(set)
	for i in data:
		for k, v in i.iteritems():
			d = recursive_finder(d, k, v)

	return d


def data_formatter(v):
	if type(v) == str or type(v) == unicode:
		return v.lower().replace(' ', '_')
	else:
		return v


def create_dataframe(data, unique_mechanics):
	"""
	Organize data by rows. Top level keys are the row index.
	The values of top level keys are a nested dictionary containing
	row data.
	"""
	words = Counter()
	bigrams = Counter()
	trigrams = Counter()
	quadgrams = Counter()

	d = defaultdict(dict)
	for idx, row_data in enumerate(data):
		d[idx]['id'] = data_formatter(row_data.get('id', ''))
		d[idx]['name'] = data_formatter(row_data.get('name', ''))
		d[idx]['type'] = data_formatter(row_data.get('type', ''))
		d[idx]['playerClass'] = data_formatter(row_data.get('playerClass', ''))
		d[idx]['race'] = data_formatter(row_data.get('race', ''))
		d[idx]['rarity'] = data_formatter(row_data.get('rarity', ''))
		d[idx]['set'] = data_formatter(row_data.get('set', ''))
		d[idx]['artist'] = data_formatter(row_data.get('artist', ''))
		d[idx]['cost'] = data_formatter(row_data.get('cost', ''))
		d[idx]['attack'] = data_formatter(row_data.get('attack', ''))
		d[idx]['health'] = data_formatter(row_data.get('health', ''))
		d[idx]['text'] = data_formatter(row_data.get('text', ''))
		d[idx]['collectible'] = data_formatter(row_data.get('collectible', ''))
		d[idx]['durability'] = data_formatter(row_data.get('durability', 0))
		d[idx]['spellDamage'] = data_formatter(row_data.get('spellDamage', 0))
		d[idx]['overload'] = data_formatter(row_data.get('overload', 0))
		row_mechanics = [
			data_formatter(x) for x in row_data.get('mechanics', [])
		]
		for mechanic in unique_mechanics:
			d[idx][data_formatter(mechanic)] = 1 if mechanic in row_mechanics else 0

		text = row_data.get('text', '').split(' ')
		words = list_item_frequencies(words, text)
		bigrams = list_item_frequencies(bigrams, find_ngrams(text, 2))
		trigrams = list_item_frequencies(trigrams, find_ngrams(text, 3))
		quadgrams = list_item_frequencies(quadgrams, find_ngrams(text, 4))
	print words.most_common(100)
	print bigrams.most_common(100)
	print trigrams.most_common(100)
	print quadgrams.most_common(100)

	return pd.DataFrame.from_dict(d, orient='index')


def find_ngrams(input_list, n):
	return zip(*[input_list[i:] for i in range(n)])


def list_item_frequencies(counter, items):
	for item in items:
		counter[item] += 1

	return counter


def main():
	# load cards data
	# cards = json.loads(open('data/cards.collectible.txt', 'r').read())
	cards_collectible = json.loads(open('data/cards.collectible.txt', 'r').read())

	# uniqueify cards data
	cards_uniqued = find_uniques(cards_collectible)
	unique_mechanics = dict(cards_uniqued)['mechanics']
	print unique_mechanics

	# create dataframes
	df_cards = create_dataframe(cards_collectible, unique_mechanics)
	df_cards.to_csv('clean_cards.csv', sep='\t', encoding='utf-8')

if __name__ == '__main__':
	main()

# to do
	# how to use targeting arrow text
