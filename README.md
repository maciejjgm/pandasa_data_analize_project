# pandasa_data_analize_project
**ABY URUCHOMIĆ PROJEKT WYMAGANY JEST PLIK CSV UMIESZCZONY NA GOOGLE DRIVE!**
Projekt na zajecia z Analizy danych WSB.
Założenia projektu:
Stworzyć aplikacje, która wykona analize wypadków w Nowym Yorku w celu zindytyfikowania w których dzielnicach dochodzi 
do największej ilości wypadków motocyklowych oraz zaprezentowanie wyników w formie grafu.

# Analiza Danych 

### Konfiguracja środowiska - Ubuntu
````
sudo apt-get update
sudo apt-get install libpython3-dev
sudo apt-get install python3-venv
python3 -m venv venv
````
#### Aktywacja venv ubuntu
````
source venv/bin/activate
````
### Instalacja biblioteki pandas 

````
pip install pandas
````
w razie problemów podczas instalacji związanych z managerem paczek na Ubuntu:
````
sudo apt install python3-pip
python -m pip install --upgrade pip
````

### Instalacja biblioteki fuzzywuzzy

```
pip install fuzzywuzzy
pip install python-Levenshtein
```

### Dokumentacje oraz materiały ###

#### PANDAS
* https://pandas.pydata.org/docs/

#### CAMELOT
* https://readthedocs.org/projects/camelot-py/downloads/pdf/master/

#### MATPLOTLIB:
**Instalacja**
```
pip install matplotlib
```

* https://matplotlib.org/stable/users/installing/index.html

* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.bar.html

* https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots.html

* https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
