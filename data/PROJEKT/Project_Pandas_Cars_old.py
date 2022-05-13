import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
zad 3. Przefiltorwania danych na podstawie 
zad 4. Stworzenie nowego pliku roboczego
zad 5. Sprawdzenie skrajnych wartości(min/max) kolizji motocyklowych w Nowym Yorku
zad 6. Wskazanie top 3 niebezpiecznych i bezpiecznych dzielnic
zad 7. Zaprezentowanie wynikow w postaci graficznej

"""

pd.set_option('display.max_columns',50)
# szerokość DF (wyświetlanie)
pd.set_option('display.width',1000)
pd.set_option('display.max_colwidth', 100)
read_settings = {"name":str,"prep_time":int}

# zad 1. Załadowanie DF oraz sprawdzenie zawartości
# Wczytaj plik
# print('----------original data--------------')
nypd_collisions = pd.read_csv('../../theory/copy/nypd-motor-vehicle-collisions.csv',
                              dtype= read_settings)
                            # header = 4
                          # index_col=2)
# Ogolny przeglad danych - zapoznanie
# print(nypd_collisions.head(5))
# print('---------------------------------')

# zad 2. Sprawdzenie Nazw Column, wielkości sheet'u w DF
# Sprawdzenie nazw kolumn, ilości non-null, typu danych, wielkości bazy
# print(nypd_collisions.info())
# Sprawdzenie ilości wierszy i kolumn.
# print(nypd_collisions.shape)

#Printuje liste kolumn
# for col in nypd_cars.columns:
#     print(col)

# zad 3. Przefiltorwania danych na podstawie

nypd_collisions = nypd_collisions.dropna(subset=['BOROUGH'])
# # nypd_collisions = nypd_collisions[nypd_collisions['BOROUGH'] != 'NaN']
# print(nypd_collisions)
nypd_collisions_new = nypd_collisions[['BOROUGH',
                                       'ON STREET NAME',
                                       'NUMBER OF PERSONS INJURED',
                                       'NUMBER OF PERSONS KILLED',
                                       'NUMBER OF MOTORIST INJURED',
                                       'NUMBER OF MOTORIST KILLED']]
# funkcja
# dla kazdego unikalnego 'BOROUGH' w columnie 'BOROUGH' sumuj wyniki 'NUMBER OF PERSONS KILLED',
#                                        'NUMBER OF MOTORIST INJURED',
#                                        'NUMBER OF MOTORIST KILLED'
# A1 = list(pd.unique(nypd_collisions_new['BOROUGH']))
# print(A1)
# for A1 in nypd_collisions_new.sum([['NUMBER OF PERSONS INJURED',
#                                        'NUMBER OF PERSONS KILLED',
#                                        'NUMBER OF MOTORIST INJURED',
#                                        'NUMBER OF MOTORIST KILLED']]):
#     print(nypd_collisions_new)

# print(type(A1))

agg_nypd_collisions_new_max_min_mean = nypd_collisions_new.groupby('BOROUGH').sum('NUMBER OF PERSONS KILLED')#,
                                          # 'NUMBER OF PERSONS KILLED': 'min',
                                          # 'NUMBER OF PERSONS KILLED': 'mean'})
# agg_nypd_collisions_new_max_min_mean.columns = ['max_NUMBER OF PERSONS KILLED',
#                                        'min_NUMBER OF PERSONS KILLED',
#                                        'mean_NUMBER OF PERSONS KILLED']
print(agg_nypd_collisions_new_max_min_mean)

# nypd_collisions_new = nypd_collisions_new.sum
# print(nypd_collisions_new)
# zad 4. Stworzenie nowego pliku roboczego

# nypd_collisions_new.to_csv('Moto_incidents_in_NY.csv', index=False)

# def CheckNewFile():
#     dirct = '../'
#     file = '*.csv'
#     if file in dirct == True:
#         print(f" FILE NAME: {file}")

# zad 5. Sprawdzenie skrajnych wartości(min/max) kolizji motocyklowych w Nowym Yorku

# max_moto_injures_per_borough_df = agg_nypd_collisions_new_max_min_mean.groupby(['BOROUGH'], as_index=False)['NUMBER OF PERSONS INJURED'].max()
# min_moto_injures_per_borough_df = agg_nypd_collisions_new_max_min_mean.groupby(['BOROUGH'], as_index=False)['NUMBER OF PERSONS INJURED'].min()
#
# # zad 6. Wskazanie top 3 niebezpiecznych i bezpiecznych dzielnic
#
# print(max_moto_injures_per_borough_df.head(3))
# print(min_moto_injures_per_borough_df.head(3))

# agg_nypd_collisions_new_max_min_mean.plot.bar()
#
# plt.show()

# for data in agg_nypd_collisions_new_max_min_mean:
#     procentage = (data['NUMBER OF PERSONS KILLED'] / data['NUMBER OF PERSONS INJURED']) * 100
#     print(f"Killed to Injured rato: {procentage}%")
agg_nypd_collisions_new_max_min_mean_procentage = agg_nypd_collisions_new_max_min_mean
agg_nypd_collisions_new_max_min_mean_procentage['% Killed to Injured PERSONS'] = (agg_nypd_collisions_new_max_min_mean['NUMBER OF PERSONS KILLED'] / agg_nypd_collisions_new_max_min_mean['NUMBER OF PERSONS INJURED']) * 100
agg_nypd_collisions_new_max_min_mean_procentage['% Killed to Injured MOTORIST'] = (agg_nypd_collisions_new_max_min_mean['NUMBER OF MOTORIST KILLED'] / agg_nypd_collisions_new_max_min_mean['NUMBER OF MOTORIST INJURED']) * 100
agg_nypd_collisions_new_max_min_mean_procentage = agg_nypd_collisions_new_max_min_mean_procentage[[
                                       '% Killed to Injured PERSONS',
                                       '% Killed to Injured MOTORIST']]

# agg_nypd_collisions_new_max_min_mean['% Killed to Injured'] = str(round(agg_nypd_collisions_new_max_min_mean['% Killed to Injured'], 2))
# agg_nypd_collisions_new_max_min_mean.style.format({'NUMBER OF PERSONS INJURED': "{:.2f}",
#                                                    'NUMBER OF PERSONS KILLED': "{:.2f}",
#                                                    'UMBER OF MOTORIST INJURED': "{:.2f}",
#                                                    'NUMBER OF MOTORIST KILLED': "{:.2f}",
#                                                    '% Killed to Injured': "{:.2%}"})
# print(agg_nypd_collisions_new_max_min_mean)
# agg_nypd_collisions_new_max_min_mean.plot.bar()

# # plt.show()
# agg_nypd_collisions_new_max_min_mean_procentage.plot.bar()
#
# plt.show()
# fig, axs= plt.figure("Incidents Dashboard")
# axs= plt.figure("Deaths to Injured % ratio")
fig, axs = plt.subplots(nrows=1, ncols=2, squeeze=False)
fig = plt.figure(1)
fig.canvas.set_window_title("Incidents Dashboard")
# agg_nypd_collisions_new_max_min_mean.plot.bar(ax=ax[0][0], rot=1, grid=True)
# agg_nypd_collisions_new_max_min_mean_procentage.plot.bar(ax=ax[0][1], rot=1, grid=True)
# fig, (ax1,ax2) =plt.subplots(1, 2, constrained_layout=True, sharey=True)
fig.suptitle('Incidents in NY Dashboard', fontsize=16)
# ax1.plot(agg_nypd_collisions_new_max_min_mean)
# ax2.plot(agg_nypd_collisions_new_max_min_mean_procentage)
agg_nypd_collisions_new_max_min_mean.plot.bar(ax=axs[0][0], rot=1, grid=True)
agg_nypd_collisions_new_max_min_mean_procentage.plot.bar(ax=axs[0][1], rot=1, grid=True)
# ax1.set_title('Incidents Dashboard"')
# ax1.set_xlabel('Locations')
# ax1.set_ylabel('Person')
# ax2.set_title('Deaths to Injured % ratio')
# ax2.set_xlabel('Locations')
# ax2.set_ylabel('Procentage')
the_table = plt.table(cell_text= agg_nypd_collisions_new_max_min_mean_procentage,loc='bottom')
#TODO: sprawdzic jak działa zorder , - chcemy ustawic grid za bar
plt.grid(color='red' )#alpha:
plt.show()
# PROBLEM:
# mamy wykres ktory jest nieczytelny. Trzeba stworzyc 2 wykresy jeden calosc a drugi skala wypadkow smiertelnych, aby bylo to widoczne
# stowrzyc % wypadkow smiertelnych od wypadkow Injured
# max_moto_injures_per_borough_df = nypd_cars.groupby(['BOROUGH'], as_index=False)['NUMBER OF PERSONS INJURED'].max()
#
# print(max_moto_injures_per_borough_df.head(5))

# print(nypd_cars['BOROUGH'].unique())
# # df = nypd_cars.dropna['BOROUGH']
# df = nypd_cars.dropna(axis=1, how='all')
# print(df['BOROUGH'].unique())
# # for col in nypd_cars:
# #     print(nypd_cars[col].unique())