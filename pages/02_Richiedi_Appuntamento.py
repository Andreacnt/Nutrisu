import streamlit as st
from datetime import datetime, date, time

st.markdown("# 📅 Richiedi un Appuntamento")
st.markdown(
    "Compila il form qui sotto e ti ricontatterò per confermare la data."
)

with st.form("appointment_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome *")
        email = st.text_input("Email *")
        telefono = st.text_input("Telefono")
    with col2:
        cognome = st.text_input("Cognome *")
        data = st.date_input("Data preferita *", min_value=date.today())
        ora = st.time_input("Orario preferito", value=time(10, 0))

    tipo_consulenza = st.selectbox(
        "Tipo di consulenza *",
        [
            "Prima visita",
            "Piano alimentare personalizzato",
            "Educazione alimentare",
            "Esame bioimpedenziometrico",
            "Plicometria e circonferenze corporee",
            "Consulenza online",
            "Altro",
        ],
    )
    messaggio = st.text_area("Messaggio", placeholder="Parlami dei tuoi obiettivi, eventuali allergie o intolleranze...")

    consenso = st.checkbox(
        "Acconsento al trattamento dei dati personali *",
    )

    submitted = st.form_submit_button("Invia Richiesta", type="primary", use_container_width=True)

    if submitted:
        if not nome or not cognome or not email or not consenso:
            st.error("Per favore compila tutti i campi obbligatori (*).")
        else:
            st.success(
                f"✅ Richiesta inviata con successo, {nome}! Ti ricontatterò "
                f"presto per confermare l'appuntamento del {data.strftime('%d/%m/%Y')}."
            )
            st.info(
                "📧 Riceverai una email di conferma. Se non la trovi, "
                "controlla la cartella spam."
            )

st.markdown("---")
st.info(
    "💬 Per informazioni sulle tariffe, contattami direttamente "
    "via email o telefono."
)
