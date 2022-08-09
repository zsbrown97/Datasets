import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import numpy as np

mcu = pd.DataFrame(pd.read_csv('./mcu_box_office.csv'))
mcu.columns = ['Film', 'Phase', 'Release Date', 'Critical Reception', 'Audience Reception', 'Length', 'Budget', 'Opening Weekend Gross', 'Domestic Gross', 'Worldwide Gross']

def reception(x):
    phaseDf = mcu.loc[mcu['Phase'] == x]
    film = phaseDf.index.values
    crit = phaseDf['Critical Reception']
    aud = phaseDf['Audience Reception']
    x_axis = np.arange(len(film))
    title = 'Reception of Phase '+str(x)
    plotWidth = film.size * 3

    plt.figure(figsize=(plotWidth,10))
    plt.bar(x_axis-0.2, crit, 0.4, label = 'Critical')
    plt.bar(x_axis+0.2, aud, 0.4, label = 'Audience')

    plt.xticks(x_axis, film)
    plt.xlabel('Films')
    plt.ylabel('Reception')
    plt.yticks(range(0, 100, 10))
    plt.title(title)
    plt.legend()
    plt.show()