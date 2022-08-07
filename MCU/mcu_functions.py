import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import numpy as np

mcu = pd.DataFrame(pd.read_csv('./mcu_box_office.csv'))

def rec(phase):
    x = mcu.loc[phase].set_index('Film')
    film = x.index.values
    crit = x['Critical Reception']
    aud = x['Audience Reception']
    x_axis = np.arange(len(film))
    title = 'Reception of Phase '+str(phase)
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