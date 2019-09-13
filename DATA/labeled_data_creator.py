import pandas as pd 

df_legal = pd.read_csv('../DICTIONARY/LEGAL_DICT/complete_legal_terms.csv')
# print(df_legal.head())
df_common = pd.read_csv('../DICTIONARY/NON_LEGAL_DICT/most_common_words.csv')
# print(df_common.head())
# print(df_legal.columns)
set_legal = df_legal['TERMS']
set_common = df_common['COMMON WORDS']
# print(type(set_legal))
final_commons = []
common_legals = []
for word in set_common:
    if word not in list(set_legal):
        final_commons.append(word)
    else:
        common_legals.append(word)
        
# print(final_commons, len(final_commons))

# from 3000 most commonly used words 3000 - 2677 = 323 words we're found 
# to be legal terms, and we don't really want those words.
# we want a collection of words which are surely not legal,
# in the sense used really commonly
# print(list(set_legal))
# print(common_legals, len(common_legals))

# so we're going to assign a score of 1 to legal terms
# 0.5 to the common legals and 0 to common-words
"""
    TERM_TYPE       SCORE
    
    legals           1.0
    common-legals    0.5
    commons          0.0
    
"""

df_total_legals = pd.DataFrame(list(set_legal), columns=['LEGALS',])
df_total_legals['SCORE'] = 1.0
df_common_legals = pd.DataFrame(common_legals, columns=['COMMON-LEGALS',])
df_common_legals['SCORE'] = 0.5
df_final_commons = pd.DataFrame(final_commons, columns=['COMMONS',])
df_final_commons['SCORE'] = 0.0
# print(df_final_commons.head())

# now convert them to csv files
df_total_legals.to_csv('./labeled_legals.csv')
df_common_legals.to_csv('./labeled_common_legals.csv')
df_final_commons.to_csv('./labeled_commons.csv')

# we'll make a hypothesis function out of this dataset