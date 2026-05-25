import streamlit as st

st.markdown("# 📖 Mini Guide")
st.markdown("Consigli e curiosità sulla nutrizione per il tuo benessere quotidiano.")
st.markdown("---")

guide = [
    {
        "titolo": "🥑 I grassi sani: quali sono e perché assumerli",
        "anteprima": (
            "Non tutti i grassi sono nemici! Scopri le fonti di grassi buoni "
            "(omega-3, omega-6) e come inserirli nella tua dieta quotidiana."
        ),
        "testo": (
            "I grassi insaturi (presenti in avocado, olio d'oliva, frutta secca, "
            "pesce azzurro) sono essenziali per il cuore e il cervello. "
            "Consuma 2-3 porzioni al giorno di grassi sani. "
            "Evita i grassi trans (cibi processati, fritti industriali)."
        ),
    },
    {
        "titolo": "🥗 Colazione equilibrata: le regole d'oro",
        "anteprima": (
            "La colazione è il pasto più importante? Sì, se fatta bene! "
            "Ecco come bilanciare carboidrati, proteine e grassi."
        ),
        "testo": (
            "Una colazione ideale include:\n"
            "- **Carboidrati complessi**: pane integrale, avena, fiocchi di cereali\n"
            "- **Proteine**: yogurt greco, uova, latte\n"
            "- **Grassi sani**: frutta secca, semi chia, avocado\n"
            "- **Fibre e vitamine**: frutta fresca di stagione\n\n"
            "Esempio: yogurt greco + fiocchi d'avena + mirtilli + noci."
        ),
    },
    {
        "titolo": "💧 Quanta acqua bere al giorno?",
        "anteprima": (
            "L'idratazione è fondamentale. Ma quanta acqua serve davvero? "
            "Sfatiamo i miti e scopriamo le linee guida."
        ),
        "testo": (
            "Il fabbisogno idrico è di circa 1.5-2 litri al giorno (6-8 bicchieri). "
            "Aumenta con:\n"
            "- Attività fisica\n"
            "- Clima caldo\n"
            "- Allattamento\n\n"
            "Consigli: tieni una borraccia sempre con te, "
            "bevi prima di avere sete, "
            "alterna con tè non zuccherati e tisane."
        ),
    },
    {
        "titolo": "🏃‍♂️ Alimentazione pre e post allenamento",
        "anteprima": (
            "Cosa mangiare prima e dopo lo sport per massimizzare i risultati "
            "e recuperare al meglio."
        ),
        "testo": (
            "**PRE-allenamento (1-2 ore prima):**\n"
            "- Carboidrati a lento rilascio (banana, pane integrale)\n"
            "- Proteine magre (yogurt, pollo)\n"
            "- Evita cibi grassi e pesanti\n\n"
            "**POST-allenamento (entro 30 min):**\n"
            "- Proteine per riparare i muscoli\n"
            "- Carboidrati per ricaricare le energie\n"
            "- Esempio: frullato proteico + frutta"
        ),
    },
    {
        "titolo": "🧠 Mindful Eating: mangiare con consapevolezza",
        "anteprima": (
            "Impara a riconoscere i segnali di fame e sazietà "
            "per migliorare il rapporto con il cibo."
        ),
        "testo": (
            "La mindful eating è una pratica che aiuta a:\n"
            "- Riconoscere la fame fisica da quella emotiva\n"
            "- Mangiare lentamente e gustare ogni boccone\n"
            "- Fermarsi quando si è sazi (non pieni)\n\n"
            "Prova: metti giù la forchetta tra un boccone e l'altro, "
            "mastica lentamente, spegni la TV mentre mangi."
        ),
    },
]

for guida in guide:
    with st.expander(guida["titolo"]):
        st.markdown(guida["testo"])

st.markdown("---")
st.info(
    "📌 *Le informazioni fornite hanno scopo puramente informativo "
    "e non sostituiscono il parere del medico o del nutrizionista. "
    "Per un piano alimentare personalizzato, prenota una consulenza.*"
)
