import streamlit as st
import pandas as pd

# --- load spaCy (auto download model if not present) ---
import importlib, subprocess, sys
def ensure_model(model_name="en_core_web_sm"):
    try:
        importlib.import_module(model_name)
    except ImportError:
        subprocess.run([sys.executable, "-m", "spacy", "download", model_name], check=True)
    return model_name

MODEL = ensure_model()
import spacy
nlp = spacy.load(MODEL)
from spacy import displacy

st.set_page_config(page_title="Text Analysis Tool", layout="wide")
st.title("Text Analysis Tool (spaCy + Streamlit)")

# --- input ---
default_text = (
    "Apple is looking at buying a U.K. startup for $1 billion. "
    "Tim Cook met investors in London on Tuesday."
)
text = st.text_area("Paste a paragraph of text:", default_text, height=180)

if st.button("Analyze") or text.strip():
    doc = nlp(text)

    # --- Tokens table ---
    tok_rows = []
    for t in doc:
        tok_rows.append(
            {
                "token": t.text,
                "lemma": t.lemma_,
                "pos": t.pos_,
                "tag": t.tag_,
                "dep": t.dep_,
                "is_stop": t.is_stop,
            }
        )
    df_tokens = pd.DataFrame(tok_rows)

    # --- POS quick view (token → POS) ---
    pos_pairs = [(t.text, t.pos_) for t in doc if not t.is_space]
    df_pos = pd.DataFrame(pos_pairs, columns=["token", "POS"])

    # --- NER render ---
    ents_html = displacy.render(doc, style="ent", options={"distance": 90}, page=True)

    # --- Custom CSS for styling NER text to white, non-entity text to light gray ---
    custom_css = """
        <style>
            .token {
                color: #B0B0B0 !important;  /* Light gray for non-entities */
            }
            .entity {
                color: white !important;
                background-color: #0078d4;
                padding: 2px 4px;
                border-radius: 4px;
                border: 1px solid #0078d4;
            }
        </style>
    """

    # --- layout ---
    c1, c2 = st.columns([1, 1])
    with c1:
        st.subheader("Tokens (full info)")
        st.dataframe(df_tokens.style.applymap(lambda v: 'color: white; background-color: #0078d4', subset=['token']), use_container_width=True)

    with c2:
        st.subheader("POS tags (compact)")
        st.dataframe(df_pos, use_container_width=True)

    st.subheader("Named Entities (NER)")

    # Inject custom CSS for styling NER entities and non-entity tokens
    st.markdown(custom_css, unsafe_allow_html=True)

    # Display the NER visualization with white text and light gray non-entity text
    st.components.v1.html(ents_html, height=320, scrolling=True)

    # --- export ---
    st.download_button(
        "Download tokens CSV",
        df_tokens.to_csv(index=False).encode("utf-8"),
        file_name="tokens_pos.csv",
        mime="text/csv",
    )
