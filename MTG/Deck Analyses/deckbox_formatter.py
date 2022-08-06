import pandas as pd


def read(x):
    df = pd.DataFrame(pd.read_csv(x))
    return df[df['Section'].str.contains('scratchpad|sideboard') == False]


def dropColumns(x):
    return x.reset_index(drop=True).set_index(x['Name']).drop(['Name', 'Section', 'Image URL', 'Card Number', 'Condition', 'Language', 'Foil', 'Signed', 'Artist Proof', 'Altered Art', 'Misprint'], axis=1)
    # Dropped Image URL until I can find a way to display images

def creatures(x):
    x = x[x['Type'].str.contains('Creature')].drop(['Count'], axis=1)
    x.replace('(?:Creature - )','', regex=True, inplace=True)
    return x

def lands(x):
    return x[x['Type'].str.contains('Land')].drop(['Cost'], axis=1)

def splitTables(x, y):
    return x[x['Type'].str.contains(y)].drop(['Count', 'Type'], axis=1)

