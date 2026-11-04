from pathlib import Path
import joblib
import streamlit as st

project_dir = Path(__file__).resolve().parent.parent
model_path = project_dir / "models" / "banking77_model.joblib"

model = joblib.load(model_path)

st.title("Klasyfikacja zgłoszeń bankowych")

st.write(
    "Wpisz wiadomość, aby przewidzieć kategorię zgłoszenia."
)

message = st.text_area(
    "Treść zgłoszenia:",
    placeholder="Np. I cannot access my account"
)

if st.button("Klasyfikuj zgłoszenie"):

    if message.strip():

        prediction = model.predict([message])[0]

        st.success(
            f"Przewidywana kategoria: {prediction}"
        )

    else:
        st.warning("Wpisz treść zgłoszenia.")
