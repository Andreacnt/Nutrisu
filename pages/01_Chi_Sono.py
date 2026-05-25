import streamlit as st

st.markdown("# 👩‍⚕️ Chi Sono")
st.markdown("---")

col1, col2 = st.columns([1, 2])
with col1:
    st.image(
        "https://img.icons8.com/color/240/doctor-male--v1.png", width=200
    )
with col2:
    st.markdown(
        """
        ### Dott.ssa [Nome]
        **Biologa Nutrizionista** | Iscritta all'Ordine dei Biologi n. [X]

        Laureata in Scienze della Nutrizione presso l'Università di [Nome],
        con master in [Specializzazione].

        ### 📋 Cosa offro:
        - Piani alimentari personalizzati
        - Educazione alimentare
        - Supporto nel raggiungimento dei tuoi obiettivi
        - Percorsi di dimagrimento e benessere
        """
    )

st.markdown("---")
st.markdown("## 📍 Dove Trovarmi")

col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
        ### Studio [Nome]
        📪 Via Roma, 123 - 00100 Roma
        📞 +39 123 456 7890
        ✉️ email@nutrizionista.it

        **Orari:**
        - Lun-Ven: 9:00 - 13:00 / 15:00 - 19:00
        - Sab: 9:00 - 13:00 (solo su appuntamento)
        """
    )
with col2:
    st.markdown(
        """
        ### Social
        - 📸 Instagram: @nutrizionista
        - 📘 Facebook: /nutrizionista
        - 🔗 LinkedIn: /in/nutrizionista
        """
    )

st.markdown("### 🗺️ Mappa")
st.markdown("Sostituisci il placeholder con l'indirizzo del tuo studio:")
st.code(
    '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!..." width="100%" height="300" style="border:0;" allowfullscreen></iframe>',
    language="html",
)
st.info("Vai su maps.google.com, cerca il tuo indirizzo, clicca 'Condividi' → 'Incorpora una mappa' e copia il codice qui sopra.")
