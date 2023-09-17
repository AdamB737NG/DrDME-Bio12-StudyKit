import streamlit as st
from docx import Document
import os
from transformers import GPT2Tokenizer
import openai

# Configuration OpenAI
openai.api_key = "ENTER_YOUR_OPENAI_KEY_HERE"

# Fonction pour lire le fichier .docx
def read_word_file(word_file_path):
    doc = Document(word_file_path)
    full_text = []
    for para in doc.paragraphs:
        if para.text.strip():
            full_text.append(para.text)
    return '\n'.join(full_text)

# Fonction pour sauvegarder le texte dans un fichier .txt
def save_text_to_txt(text, txt_file_path):
    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

# Fonction pour tokeniser le fichier
def tokenize_file(input_file_path, output_directory):
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    with open(input_file_path, 'r', encoding='utf-8') as f:
        text_content = f.read()
    tokens = tokenizer(text_content)['input_ids']
    max_tokens = 4097
    chunks = [tokens[i:i + max_tokens] for i in range(0, len(tokens), max_tokens)]
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    for i, chunk in enumerate(chunks):
        chunk_text = tokenizer.decode(chunk)
        with open(f"{output_directory}/morceau_{i + 1}.txt", 'w', encoding='utf-8') as f:
            f.write(chunk_text)

# Fonction pour créer les fiches Anki
def create_anki_flashcards(text_content):
    messages = [
        {"role": "system", "content": "Vous êtes un assistant serviable."},
    ]

    text_segments = [text_content[i:i + 3000] for i in range(0, len(text_content), 3000)]
    flashcards_for_anki = ""

    for segment in text_segments:
        messages.append(
            {"role": "user",
             "content": f"Créez des fiches Anki avec le texte suivant en utilisant un format comme question;réponse, ligne suivante question;réponse etc...{segment}."}
        )
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.3,
        )
        generated_flashcards = response["choices"][0]["message"]["content"]

        for fc in generated_flashcards.split("\n"):
            if fc:
                parts = fc.split(";")
                if len(parts) == 2:
                    q, a = parts
                    flashcards_for_anki += f"{q.strip()};{a.strip()}\n"
                else:
                    flashcards_for_anki += f"{fc.strip()};\n"
        messages = [messages[0]]

    flashcards_filepath = "flashcards.txt"
    with open(flashcards_filepath, "w") as f:
        f.write(flashcards_for_anki)
    return flashcards_for_anki, flashcards_filepath

# Interface Streamlit
st.title('Kit d’étude DrDME-Bio12')

uploaded_file = st.file_uploader("Téléchargez un fichier DOCX", type="docx")

if uploaded_file:
    with open("fichier_telecharge.docx", "wb") as f:
        f.write(uploaded_file.getbuffer())

    text_content = read_word_file("fichier_telecharge.docx")
    save_text_to_txt(text_content, "sortie.txt")
    tokenize_file("sortie.txt", "./morceaux")

    generated_flashcards, flashcards_filepath = create_anki_flashcards(text_content)

    st.text("Les fiches ont été enregistrées sous 'flashcards.txt'")
    st.text("Voici vos fiches :")
    st.text(generated_flashcards)

    st.download_button(
        label="Télécharger les fiches",
        data=open(flashcards_filepath, "rb"),
        file_name="fiches_anki.txt",
    )
