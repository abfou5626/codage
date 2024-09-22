import streamlit as st

# Fonctions pour chiffrer et déchiffrer
def chiffrer(message_a_code, clef):
    message = []
    message_codé = []
    
    for i in message_a_code:
        message.append(ord(i) + clef)  # Décale le code ASCII avec la clé
    
    for i in message:
        message_codé.append(chr(i))  # Convertit les codes ASCII décalés en caractères
    final = "".join(message_codé)  # Assemble les caractères en une chaîne
    return final

def dechiffrer(message_a_decoder, clef):
    message = []
    message_decodé = []
    
    for i in message_a_decoder:
        message.append(ord(i) - clef)  # Décale le code ASCII à l'inverse avec la clé
    
    for i in message:
        message_decodé.append(chr(i))  # Convertit les codes ASCII en caractères
    final = "".join(message_decodé)  # Assemble les caractères en une chaîne
    return final

# Interface Streamlit
st.title("Chiffrement et Déchiffrement de Texte")

# Choix entre chiffrer et déchiffrer
choix = st.radio("Voulez-vous chiffrer ou déchiffrer un message ?", ('Chiffrer', 'Déchiffrer'))

if choix == 'Chiffrer':
    message_a_code = st.text_input("Entrez votre texte à chiffrer :")
    clef = st.number_input("Tapez votre clé de chiffrage :", min_value=0, step=1)
    
    if st.button('Chiffrer'):
        if message_a_code and clef:
            message_final = chiffrer(message_a_code, clef)
            st.success(f"Message chiffré : {message_final}")
        else:
            st.error("Veuillez entrer un texte et une clé valide.")

elif choix == 'Déchiffrer':
    message_a_decoder = st.text_input("Entrez votre texte à déchiffrer :")
    clef = st.number_input("Tapez votre clé de déchiffrage :", min_value=0, step=1)
    
    if st.button('Déchiffrer'):
        if message_a_decoder and clef:
            message_final = dechiffrer(message_a_decoder, clef)
            st.success(f"Message déchiffré : {message_final}")
        else:
            st.error("Veuillez entrer un texte et une clé valide.")
