#!/usr/bin/env python

import sys
import pdb
import hearthstone_cards
import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
import sklearn as sk


def main():
	df_cards = pd.DataFrame.from_csv('clean_cards.csv', sep='\t', encoding='utf-8')
	df_cards = df_cards[df_cards['type'].isin(['minion'])]
	print df_cards.sample(10)


if __name__ == '__main__':
	hearthstone_cards.main()
	main()


"""
Notes:
print 'unique_mechanics'
unique_mechanics = dict(cards_uniqued)['mechanics']
print unique_mechanics
# set([u'enraged', u'ai_must_play', u'inspire', u'freeze', u'divine_shield', u'immunetospellpower', u'adjacent_buff', u'choose_one', u'poisonous', u'charge', u'secret', u'invisibledeathrattle', u'combo', u'taunt', u'topdeck', u'forgetful', u'deathrattle', u'stealth', u'morph', u'ritual', u'windfury', u'tag_one_turn_effect', u'evil_glow', u'aura', u'battlecry', u'silence'])
print 'unique types:'
print dict(cards_uniqued)['type']
# set([u'hero_power', u'hero', u'minion', u'weapon', u'spell', u'enchantment'])
"""
