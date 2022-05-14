import pandas as pd
import matplotlib.pyplot as plt

"""
PROJEKT ZALICZENIOWY PYTHON DEVELOPER WSB 2022 - ANALIZA DANYCH

Założenia projektu:
Stworzyć aplikacje, która wykona analize wypadków w Nowym Yorku w celu zindytyfikowania w których dzielnicach dochodzi 
do największej ilości wypadków motocyklowych oraz zaprezentowanie wyników w formie grafu.

Projekt ma na celu ukazać, które dzielnice NY są niebezpieczne dla fanów jednośladów.

Projekt wykorzystuje:
1)Biblioteke:
* PANDAS
2)Baza:
* nypd-motor-vehicle-collisions.csv
3)Wizualizacja:
* Matplotlib

Do wykonania:
zad 1. Załadowanie DF oraz sprawdzenie zawartości
zad 2. Sprawdzenie Nazw Column, wielkości sheet'u w DF
zad 3. Przefiltorwania danych
zad 4. Stworzenie nowego pliku roboczego
zad 5. Wskazanie top niebezpiecznych dzielnic
zad 6. Zaprezentowanie wynikow w postaci graficznej

"""

pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 100)
read_settings = {"name": str, "prep_time": int}

print('----------original data--------------')
nypd_collisions = pd.read_csv('../../theory/copy/nypd-motor-vehicle-collisions.csv',
                              dtype= read_settings)
                            # header = 4
                          # index_col=2)

print(nypd_collisions.head(5))
print('---------------------------------')
print('-----------INO---------------')
print(nypd_collisions.info())

print(nypd_collisions.shape)
print('---------------------------------')


nypd_collisions = nypd_collisions.dropna(subset=['BOROUGH'])
nypd_collisions_new = nypd_collisions[['BOROUGH',
                                       'ON STREET NAME',
                                       'NUMBER OF PERSONS INJURED',
                                       'NUMBER OF PERSONS KILLED',
                                       'NUMBER OF MOTORIST INJURED',
                                       'NUMBER OF MOTORIST KILLED']]

agg_nypd_collisions_new_max_min_mean = nypd_collisions_new.groupby('BOROUGH').sum('NUMBER OF PERSONS KILLED')
print(agg_nypd_collisions_new_max_min_mean)

nypd_collisions_new.to_csv('Moto_incidents_in_NY.csv', index=False)

agg_nypd_collisions_new_max_min_mean_procentage = agg_nypd_collisions_new_max_min_mean
agg_nypd_collisions_new_max_min_mean_procentage['% Killed to Injured PERSONS'] = (agg_nypd_collisions_new_max_min_mean['NUMBER OF PERSONS KILLED'] / agg_nypd_collisions_new_max_min_mean['NUMBER OF PERSONS INJURED']) * 100
agg_nypd_collisions_new_max_min_mean_procentage['% Killed to Injured MOTORIST'] = (agg_nypd_collisions_new_max_min_mean['NUMBER OF MOTORIST KILLED'] / agg_nypd_collisions_new_max_min_mean['NUMBER OF MOTORIST INJURED']) * 100
agg_nypd_collisions_new_max_min_mean_procentage = agg_nypd_collisions_new_max_min_mean_procentage[[
                                       '% Killed to Injured PERSONS',
                                       '% Killed to Injured MOTORIST']]


fig, axs = plt.subplots(nrows=1, ncols=2, squeeze=False)
fig = plt.figure(1)
fig.canvas.set_window_title("Incidents Dashboard")
fig.suptitle('Incidents in NY Dashboard', fontsize=16)
agg_nypd_collisions_new_max_min_mean.plot.bar(ax=axs[0][0], rot=1, grid=True)
agg_nypd_collisions_new_max_min_mean_procentage.plot.bar(ax=axs[0][1], rot=1, grid=True)
plt.grid(color='black')
plt.show()
