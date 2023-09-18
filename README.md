### Configuration

Ouvrez le fichier `app.py` dans un éditeur de texte et configurez votre clé API OpenAI en modifiant la ligne suivante :

```python
openai.api_key = "YOUR_OPENAI_API_KEY_HERE"
```

### Utilisation

#### Extraction de texte depuis des fichiers Word
Placez votre fichier `.docx` dans le répertoire approprié.  
Ouvrez le fichier `app.py` et ajustez le chemin d'accès au fichier Word (variable `word_file_path`).  
Exécutez le script pour extraire le texte et le sauvegarder dans un fichier `.txt`.

#### Tokenisation du texte
Assurez-vous que le texte est bien extrait dans un fichier `.txt`.  
Exécutez le script pour tokeniser le texte et diviser celui-ci en fragments respectant la limite de tokens imposée par GPT-3.5.

#### Création des fiches Anki
Copiez le texte que vous souhaitez transformer en fiches Anki dans votre presse-papiers.  
Exécutez le script pour générer automatiquement les fiches Anki et les sauvegarder dans un fichier `flashcards.txt`.

### Contribution
Nous accueillons les contributions, n'hésitez pas à ouvrir une issue ou à proposer une pull request.

### Licence
Ce projet est distribué sous licence MIT. Pour plus d'informations, consultez le fichier `LICENSE`.

---

### Prérequis

#### Configuration de Python et de l'environnement virtuel

1. **Installation de Python**
   
   Assurez-vous d'avoir installé **Python 3.8** ou une version ultérieure. Vous pouvez télécharger Python depuis [le site officiel de Python](https://www.python.org/).

2. **Création d'un environnement virtuel** (Facultatif mais recommandé)
   
   Pour isoler les dépendances du projet, il est recommandé de créer un environnement virtuel. Ouvrez un terminal et naviguez vers le dossier où vous souhaitez créer l'environnement virtuel, puis exécutez la commande suivante :

   ```bash
   python3 -m venv env
   ```

3. **Activation de l'environnement virtuel**
   
   Une fois l'environnement virtuel créé, activez-le. La commande pour activer l'environnement virtuel dépend de votre système d'exploitation :

   - **Windows** :
     
     ```bash
     .\env\Scripts\activate
     ```

   - **macOS et Linux** :

     ```bash
     source env/bin/activate
     ```

#### Installation des dépendances

Avec l'environnement virtuel activé, installez les dépendances requises à l'aide du fichier `requirements.txt` qui doit être présent dans le répertoire de votre projet. Exécutez la commande suivante :

```bash
pip install -r requirements.txt
```

### Autres prérequis

- **Compte OpenAI (clé API)**
   
   Vous aurez besoin d'un compte OpenAI avec une clé API. Si vous n'en avez pas, [inscrivez-vous sur le site d'OpenAI](https://platform.openai.com/docs/api-reference) pour en obtenir une.
   Voici un tutoriel YouTube sur comment obtenir une clé API OpenAI [Tuto Clé API](https://www.youtube.com/watch?v=EQQjdwdVQ-M).

### Lancement de l'application avec Streamlit

Pour lancer l'application, suivez les étapes ci-dessous :

1. Assurez-vous d'avoir satisfait à tous les prérequis et installé toutes les dépendances comme mentionné dans les sections précédentes.
   
2. Ouvrez un terminal et naviguez vers le répertoire contenant le fichier `app.py`.

3. Tapez la commande suivante pour lancer l'application Streamlit :

   ```bash
   streamlit run main.py
   
Streamlit lancera automatiquement l'application dans votre navigateur web par défaut. Vous devriez voir l'interface utilisateur de l'application. Si le navigateur ne s'ouvre pas automatiquement, ouvrez votre navigateur web et accédez à l'URL affichée dans votre terminal (généralement http://localhost:8501).

Utilisez l'interface utilisateur Streamlit pour interagir avec l'application selon les instructions fournies dans la section Utilisation de ce document.

Nous espérons que vous trouverez cette application utile et facile à utiliser. N'hésitez pas à contribuer au projet en ouvrant des issues ou en proposant des pull requests pour améliorer l'application.

### Ressources supplémentaires

Si vous êtes nouveau dans le monde de Python ou Streamlit, ces ressources peuvent vous être utiles :

- [Documentation officielle de Python](https://docs.python.org/3/)
- [Tutoriels Streamlit](https://docs.streamlit.io/0.88.0/library/get-started)
