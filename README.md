# Améliorez une application Web Python par des tests et du débogage

[**Projet 11** du parcours OpenClassrooms Développeur d'application en Python](https://openclassrooms.com/fr/paths/518/projects/839/assignment)
[![Tests Status](./reports/junit/tests-badge.svg?dummy=8484744)](./reports/junit/report.html)
[![Coverage Status](./reports/coverage/coverage-badge.svg?dummy=8484744)](reports/coverage/index.html)
[![Flake8 Status](./reports/flake8/flake8-badge.svg?dummy=8484744)](reports/flake8/index.html)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

## *Technologies*

<br>
<p>
<img src="https://skillicons.dev/icons?i=git,github,python,flask,&theme=dark">
</p> 

* [Flask](https://flask.palletsprojects.com/en/2.3.x/)

    Alors que Django fait beaucoup de choses pour nous, Flask nous permet d'ajouter uniquement ce dont nous avons besoin.
#
## *Présentation :*

<p align="center">
  <img src="./static/httpsuser.oc-static.comupload2020092216007798203635_P9.png" alt="Güdlft logo"/>
</p>

Nous sommes chargés par la société Güdlft d'améliorer leur application de gestion des reservation
pour que des clubs de liftings puissent réserver des places en compétitions.

Cette application est écrite avec **Python** accompagné du framework **Flask** et plusieurs librairies de tests
telles que **coverage**, **pytest**, **flake8** et **locust**

Nous devons donc débugger et tester l'application.

Le projet originel se trouve ici : https://github.com/OpenClassrooms-Student-Center/Python_Testing.
#
## *Installation:*
Vous devez tout d'abord vous doter de la dernière version de python, vous pouvez la télécharger ici :
* [Python v3.x+](https://www.python.org/downloads/)


     


Du fait que ce projet est un **fork** (nouveau logiciel créé à partir d'un logiciel existant), 
vous dever cloner mon **fork**, afin de pouvoir rester synchronisé avec mon Git repository, pour ce faire : 

1. Ouvrez un terminal de commande

2. Créer un dossier vide. Il contiendra le code complet du projet :<pre><code>mkdir myproject
cd myproject
</code></pre>

3. Puis créer un environnement virtuel, et activer le:<pre><code>python -m venv .env</code></pre>

    * Sous Linux/macOS :<pre><code>.env/bin/activate</code></pre>
    * Sous Windows :<pre><code>.env\Scripts\activate </code></pre>

4. Afin de cloner, entrez : <pre><code>git clone https://github.com/Nathom78/Ameliorez-une-application-Web-Python-par-des-tests-et-du-d-bogage.git <br></code></pre>
Ou utiliser [ce repository](https://github.com/Nathom78/Ameliorez-une-application-Web-Python-par-des-tests-et-du-d-bogage.git) en téléchargeant le zip.<br>

5. Installez les packages python prérequis, au bon fonctionnement du projet avec la commande suivante :
   - Version "normale" : `pip install -r requirements.txt`
   - Version "testing" : `pip install -r requirements_for_testing.txt`

#
## *Démarrage de l'application :*
Pour faire fonctionner l'application, vous aurez besoin de démarrer Flask, pour cela :
1. Ouvrez un terminal **externe** à votre IDE *(integrated development environment)*
dans le dossier du projet.
2. Démarrez avec la commande suivante :<pre><code>flask --app server run</code></pre>
3. Un fichier _config.py_ contient les éléments afin de démarrer l'application Flask, pour l'instant en mode "development".

#
## *Configuration actuelle :*
L'application est alimentée par des [fichiers JSON](https://www.tutorialspoint.com/json/json_quick_guide.htm). Il s'agit de contourner le fait d'avoir une base de données jusqu'à ce que nous en ayons réellement besoin. Les principaux sont :
* competitions.json : liste des compétitions
* clubs.json : liste des clubs avec des informations pertinentes. Vous pouvez regarder ici pour voir quelles adresses e-mail l'application acceptera pour la connexion.

#
## *La phase de tests :*
Pour ce projet, nous effectuons trois phases de tests, pour cela, nous utiliserons trois
outils différents, leur utilisation est expliquée ci-dessous :

#### Pytest :
Les tests qui ont étés rédigés pour ce projet se trouvent dans le répertoire **tests**
Pour lancer pytest, veuillez entrer la commande suivante dans votre terminal :

- `pytest .\tests\`

Cette commande exécutera tous les tests qui se trouvent dans le répertoire tests, vous pouvez
choisir vos tests en ajoutant directement le nom du fichier test ciblé, exemple :
- `pytest .\tests\tests unitaires\test_login.py`

Pour les tests fonctionnels une capture d'écran est créé dans le repertoire _static_.
Suivant le navigateur que vous utilisez, vous devez dans le fichier de test fonctionnel changer le pilote web pour Sélénium

#### Locust :

Concernant Locust, vous pouvez consulter les rapports générés avant et après, dans le dossier **reports/locust**, 
il s'ouvre dans un navigateur.

Cependant, si vous voulez lancer vous-même le test locust, entrez commandes suivantes dans votre terminal :

- `locust -f .\tests\performance_tests\locustfile.py --web-host localhost --web-port 4099`

Vous aurez alors l'Url suivante générée : 
 - http://localhost:4099/

Les tests sont avec 6 utilisateurs.
PS: Le serveur doit être lancé en parallel, à utiliser comme Host.




#### Coverage :

Nous aimons montrer à quel point, nous testons bien, il y a donc un module appelé
    [coverage](https://coverage.readthedocs.io/en/7.2.7/install.html)

Un rapport html, est créé dans le repertoire _/reports/coverage_ avec la commande :
`coverage html`

ou avec les tests:
`pytest --cov=. --cov-report html`

***
## *Conventions de nommage et de codes :*

**PEP 8** – Style Guide for Python Code <a href="https://peps.python.org/pep-0008/">ici</a>.</br>
Un rapport flake8 au format HTML est disponible dans le repertoire `\flake-report`, à la racine du projet.