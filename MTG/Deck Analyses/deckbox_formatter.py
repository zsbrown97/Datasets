import pandas as pd

# Reads csv and drops anything included from the scratchpad list
def read(x):
    df = pd.DataFrame(pd.read_csv(x))
    return df[df['Section'].str.contains('scratchpad') == False]

# Sets the sideboard aside
def sideboard(x):
    return x[x['Section'] == 'sideboard'].drop(['Count'], axis=1)

# Drops irrelevant columns
def dropColumns(x):
    return x.reset_index(drop=True).set_index(x['Name']).drop(['Name', 'Section', 'Image URL', 'Card Number', 'Condition', 'Language', 'Foil', 'Signed', 'Artist Proof', 'Altered Art', 'Misprint'], axis=1)
    # Dropped Image URL until I can find a way to display images

# Creates creature dataframe
def creatures(x):
    x = x[x['Type'].str.contains('Creature')].drop(['Count'], axis=1)
    x.replace('(?:Creature - )','', regex=True, inplace=True)
    return x

# Creates instants dataframe
def instants(x):
    return x[x['Type'].str.contains('Instant')].drop(['Count', 'Type'], axis=1)

# Creates sorcery dataframe
def sorceries(x):
    return x[x['Type'].str.contains('Sorcery')].drop(['Count', 'Type'], axis=1)

# Creates artifact dataframe
def artifacts(x):
    return x[x['Type'].str.contains('Artifact')].drop(['Count', 'Type'], axis=1)

# Creates enchantment dataframe
def enchantments(x):
    return x[x['Type'].str.contains('Enchantment')].drop(['Count', 'Type'], axis=1)

# Creates planeswalker dataframe
def planeswalkers(x):
    return x[x['Type'].str.contains('Planeswalker')].drop(['Count', 'Type'], axis=1)

# Creates land dataframe
def lands(x):
    return x[x['Type'].str.contains('Land')].drop(['Cost'], axis=1)


