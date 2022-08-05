import pandas as pd


def bring(nburl):
    df = pd.DataFrame(pd.read_csv(nburl))
    df = df[df['Section'].str.contains('scratchpad|sideboard') == False]
    return df


def dropCols(df):
    x = df[df['Section'].str.contains('scratchpad|sideboard') == False]
    x.reset_index(drop=True) \
        .set_index(x['Name']) \
        .drop(['Name', 'Section', 'Image URL', 'Card Number', 'Condition', 'Language', 'Foil', 'Signed', 'Artist Proof',
               'Altered Art', 'Misprint'], axis=1)
    return x


def formatCreatures(df):
    creatures = df[df['Type'].str.contains('Creature')].drop(['Count'], axis=1)
    creatures.replace('(?:Creature - )', '', regex=True, inplace=True)
    return creatures


def format(df, cardType):
    formattedDf = df[df['Type'].str.contains(cardType)]

    if (cardType == 'Creature'):
        formattedDf.drop(['Count'], axis=1)
    elif (cardType == 'Land'):
        formattedDf.drop(['Cost'], axis=1)
    else:
        formattedDf.drop(['Count', 'Type'], axis=1)

    return formattedDf
