# Application Flask de Gestion de Connexion

## Description
Cette application Flask est un système de gestion de connexion avec des fonctionnalités de sécurité. Elle permet aux utilisateurs de se connecter avec des identifiants, de simuler une attaque par force brute, de récupérer un mot de passe oublié via une question de sécurité, et de réinitialiser le mot de passe.

## Fonctionnalités
- **Connexion** : Permet aux utilisateurs de se connecter avec un nom d'utilisateur et un mot de passe.
- **Attaque par Force Brute** : Simule une attaque par force brute sur un compte utilisateur.
- **Mot de Passe Oublié** : Propose une fonction de récupération de mot de passe via une question de sécurité.
- **Réinitialisation du Mot de Passe** : Permet aux utilisateurs de réinitialiser leur mot de passe.

## Installation

Pour exécuter cette application, suivez ces étapes :

1. **Clonez le dépôt** : Clonez ce dépôt sur votre machine locale.
2. **Environnement Virtuel** : Créez un environnement virtuel en exécutant `python -m venv venv`.
3. **Activez l'Environnement Virtuel** : Activez l'environnement avec `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Windows).
4. **Installez les Dépendances** : Installez les dépendances nécessaires avec `pip install -r requirements.txt`.
5. **Exécutez l'Application** : Lancez l'application avec `python app.py`.

## Utilisation

Après avoir lancé l'application :

- Accédez à `http://localhost:5000/` pour voir la page d'accueil.
- Utilisez les liens pour naviguer vers les différentes fonctionnalités (Connexion, Attaque par Force Brute, etc.).

## Sécurité
Cette application est à des fins démonstratives et ne doit pas être utilisée dans un environnement de production. Elle contient des éléments de base de la sécurité des applications web mais n'est pas sécurisée pour un déploiement réel.

## Licence
[MIT License](LICENSE)

---

Vous pouvez ajuster ce contenu selon vos besoins spécifiques. Assurez-vous d'inclure un fichier `LICENSE` et `requirements.txt` dans votre dépôt pour compléter le `README.md`.
