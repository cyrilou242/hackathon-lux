"""Script to transform affinity keys to level 2 info
to be used by functional team"""

import pandas as pd
filename = 'clusters-examples.csv'
df = pd.read_csv(filename, sep=';')
taxonomy_filename = 'DataServices_StatSocial_Taxonomy.csv'
taxdf = pd.read_csv(taxonomy_filename)

affinities = df['dataservices_statsocial_raw_affinities']

affinities_proc =[]
for element in affinities:
    affinities_proc.append(element.split(','))

print("debug")


def lookup(aff_id):
    try:
        result= (taxdf.loc[taxdf['dataservices_statsocial_taxonomy.affinity'] == aff_id]['dataservices_statsocial_taxonomy.level2'].values)[0]
    except IndexError:
        result = "No equivalence"
    return result

for i in range(0,len(affinities_proc)):
    for j in range(len(affinities_proc[i])):
        affinities_proc[i][j] = lookup(affinities_proc[i][j])

print(affinities_proc)