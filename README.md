Analiza sladic
==============

Analiziral bom recepte sladic iz virov:
* [allrecipes](https://www.allrecipes.com/recipes/79/desserts/),
* [Jamie Oliver](https://www.jamieoliver.com/recipes/category/course/desserts/).

Za vsak recept bom zajel:
* sestavine,
* način in čas priprave,
* količino,
* hranilno vrednost,
* oceno,
* morda še kaj.

Delovne hipoteze:
1. Večina sladic vsebuje čokolado.
2. Sladice imajo veliko sladkorja/kalorij.
3. Čas priprave je neodvisen od prisotnosti določenih sestavin.

Vsebina CSV datotek:
1. datoteke oblike `ar_*.csv` vsebujejo podatke strani allrecipes.com
2. datoteke oblike `jo_*.csv` vsebujejo podatke strani jamieoliver.com
3. datoteke oblike `*_recipes.csv` vsebujejo podatke o receptih
4. datoteke oblike `*_tags.csv` vsebujejo vrste receptov
5. datoteke oblike `*_ingredients.csv` vsebujejo sestavine za recepte
6. datoteke oblike `*_steps.csv` vsebujejo korake receptov

# Navodila za uporabnike
```
Usage
  python analiza.py [options] <command>
Options:
  -h, --help                    Print help and exit
Commands:
  test [args]                   Run tests passing [args] to nose
  scrape <mode>                 Save pages locally
  parse <mode>                  Extract relevant data from local pages
  tocsv                         Convert json data to csv
Modes:
  catalogues
  recipes
```