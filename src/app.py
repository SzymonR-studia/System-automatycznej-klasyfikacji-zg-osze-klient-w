from pathlib import Path
import joblib
import streamlit as st

from selected_intents import INTENT_DISPLAY_NAMES

project_dir = Path(__file__).resolve().parent.parent
model_path = f"{project_dir}/models/banking77_model.joblib"

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
        display_name = INTENT_DISPLAY_NAMES.get(str(prediction))

        if display_name is None:
            st.error(
                "Zapisany model nie używa etykiet wybranych dla projektu. "
                "Uruchom ponownie trening modelu."
            )
        else:
            st.success(f"Przewidywana kategoria: {display_name}")

    else:
        st.warning("Wpisz treść zgłoszenia.")
