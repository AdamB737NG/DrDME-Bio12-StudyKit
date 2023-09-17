# DrDME-Bio12-StudyKit

## Description

Bienvenue sur le projet "DrDME-Bio12-StudyKit". Cette suite d'outils Python a été conçue pour faciliter la création de fiches d'étude Anki à partir des supports de cours du Dr. DME pour le cours IB Bio 12. 

## Fonctionnalités

- Extraction du texte depuis des fichiers Word (docx)
- Découpage du texte en morceaux qui respectent une limite de tokens définie
- Création automatique de fiches Anki à l'aide de GPT-3.5

## Prérequis

- Python 3.8 ou supérieur
- Bibliothèques Python : `openai`, `clipboard`, `python-docx`, `transformers`
- Un compte OpenAI avec une clé API

## Installation

Clonez le dépôt GitHub et naviguez jusqu'au dossier du projet via votre terminal. Installez ensuite les dépendances en utilisant la commande suivante :

```bash
pip install -r requirements.txt

```

## Configuration

Ouvrez le fichier `main.py` dans un éditeur de texte et configurez votre clé API OpenAI en modifiant la ligne suivante :

```python
openai.api_key = "YOUR_OPENAI_API_KEY_HERE"
```

## Utilisation

### Extraction de texte depuis des fichiers Word

1. Placez votre fichier `.docx` dans le répertoire approprié.
2. Ouvrez le fichier `main.py` et ajustez le chemin d'accès au fichier Word (variable `word_file_path`).
3. Exécutez le script pour extraire le texte et le sauvegarder dans un fichier `.txt`.

### Tokenisation du texte

1. Assurez-vous que le texte est bien extrait dans un fichier `.txt`.
2. Exécutez le script pour tokeniser le texte et diviser celui-ci en fragments respectant la limite de tokens imposée par GPT-3.5.

### Création des fiches Anki

1. Copiez le texte que vous souhaitez transformer en fiches Anki dans votre presse-papiers.
2. Exécutez le script pour générer automatiquement les fiches Anki et les sauvegarder dans un fichier `flashcards.txt`.

## Contribution

Nous accueillons les contributions, n'hésitez pas à ouvrir une issue ou à proposer une pull request.

## Licence

Ce projet est distribué sous licence MIT. Pour plus d'informations, consultez le fichier `LICENSE`.


