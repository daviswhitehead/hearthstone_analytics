#!/usr/bin/env python

import sys
import ujson as json
import pandas as pd
import pdb
from collections import defaultdict
import pprint


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

	print 'finding uniques...'
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
		d[idx]['durability'] = data_formatter(row_data.get('durability', 0))
		d[idx]['spellDamage'] = data_formatter(row_data.get('spellDamage', 0))
		d[idx]['overload'] = data_formatter(row_data.get('overload', 0))
		for mechanic in unique_mechanics:
			d[idx][data_formatter(mechanic)] = data_formatter(row_data.get(mechanic, 0))

	return pd.DataFrame.from_dict(d, orient='index')


def main():
	# load cards data
	cards = json.loads(open('data/cards.txt', 'r').read())

	# uniqueify cards data
	cards_uniqued = find_uniques(cards)
	print 'unique_mechanics'
	unique_mechanics = dict(cards_uniqued)['mechanics']
	print unique_mechanics
	# set([u'enraged', u'ai_must_play', u'inspire', u'freeze', u'divine_shield', u'immunetospellpower', u'adjacent_buff', u'choose_one', u'poisonous', u'charge', u'secret', u'invisibledeathrattle', u'combo', u'taunt', u'topdeck', u'forgetful', u'deathrattle', u'stealth', u'morph', u'ritual', u'windfury', u'tag_one_turn_effect', u'evil_glow', u'aura', u'battlecry', u'silence'])
	print 'unique types:'
	print dict(cards_uniqued)['type']
	# set([u'hero_power', u'hero', u'minion', u'weapon', u'spell', u'enchantment'])

	# create dataframes
	df_cards = create_dataframe(cards, unique_mechanics)
	df_minions = df_cards[df_cards['type'] == 'minion']
	pdb.set_trace()
	print 'cards'
	print df_cards[['type']].sample(10)
	print 'minions'
	print df_minions.sample(10)


if __name__ == '__main__':
	main()

# to do
	# how to use targeting arrow text
