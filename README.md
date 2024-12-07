ce projet Flask Admin: représente une version avancée d'une application CRUD, intégrant des fonctionnalités et des techniques améliorées pour la gestion des données et d'affichages des données.Pour faire fonctionner , veuillez suivre les étapes suivantes :

Créer un environnement virtuel Exécutez la commande suivante pour créer un environnement virtuel Python : python -m venv venv
Activer l'environnement virtuel Une fois l'environnement créé, activez-le avec la commande suivante : .venv\Scripts\activate
Installer les bibliothèques suivantes : pip install pymysql pip install Flask pip install flask_migrate pip install passlib pip install jinja2 pip install flask-bootstrap pip install bcrypt pip install flask-restful pip install flask_sqlAllchemy pip install flask_admin pip install flask_babel pip install wtfforms pip install werkzeug 
 Remarque : -Si l'une des bibliothèques rencontre un problème d'installation, essayez d'abord de la désinstaller puis de la réinstaller :
pip uninstall monenvapp3 python -m venv venv

-Si vous rencontrez une erreur de permission lors de l'installation de la bibliothèque " pip install flask-bootstrap ", suivez les étapes ci-dessous :
Purgez le cache de pip avec la commande : pip cache purge
Ensuite, réinstallez la bibliothèque en spécifiant le répertoire du cache : pip install Flask-Bootstrap --cache-dir <chemin_vers_votre_répertoire_de_cache-flask_bootstrap>
Pour démarrer le projet, utilisez l'une des commandes suivantes : flask run ou bien app.py
