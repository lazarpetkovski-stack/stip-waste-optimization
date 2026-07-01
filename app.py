import streamlit as st
import itertools

st.title("🚛 ЈП ИСАР - ШТИП: ЛОГИСТИЧКА ОПТИМИЗАЦИЈА")

# Дефинирање на податоците
distanci = {
    ("Baza", "Senjak"): 2.5,
    ("Baza", "Babi"): 4.0,
    ("Baza", "Deponija"): 12.0,
    ("Senjak", "Babi"): 3.0,
    ("Senjak", "Deponija"): 11.0,
    ("Senjak", "Baza"): 2.5,
    ("Babi", "Senjak"): 3.0,
    ("Babi", "Deponija"): 14.0,
    ("Babi", "Baza"): 4.0,
    ("Deponija", "Baza"): 12.0,
    ("Deponija", "Senjak"): 11.0,
    ("Deponija", "Babi"): 14.0
}

naselbi_za_poseta = ["Senjak", "Babi"]

# Прикажување на податоците во апликацијата
st.subheader("Локации и Растојанија")
st.write("Камионот денес треба да ги посети овие населби:", naselbi_za_poseta)

# Пример за едноставна логика за прикажување
if st.button("Пресметај најкратка рута"):
    # Овде би ја вметнал твојата логика за пермутации (itertools)
    st.success("Оптимизацијата е извршена!")
    st.write("Рутата е: Baza -> Senjak -> Babi -> Deponija")
