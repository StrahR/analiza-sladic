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

Zajem podatkov je razdeljen na 5 korakov:
1. `python analiza.py scrape catalogues`
1. `pyhton analiza.py parse catalogues`
1. `python analiza.py scrape recipes`
1. `python analiza.py parse recipes`
1. `python analiza.py tocsv`

Prvi in tretji korak vzameta več kot eno uro, so pa končne cvs datoteke priložene v mapi `data`.

Opozoril bi le, da sem malce ročno spremenil te datoteke, ker mi je program `\n` pretvoril v nove vrstice.
Se mi zdi da je to popravljeno, vendar nisem ponovno želel čakati 6+ ur za zajem.

Analiza podatkov se nahaja v `analiza-sladic.ipynb`.

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
