import streamlit as st
import itertools

st.title("🚛 ЈП ИСАР - ШТИП: ЛОГИСТИЧКА ОПТИМИЗАЦИЈА")

distanci = {
    ("Baza", "Senjak"): 2.5, ("Baza", "Babi"): 4.0, ("Baza", "Deponija"): 12.0,
    ("Senjak", "Babi"): 3.0, ("Senjak", "Deponija"): 11.0, ("Senjak", "Baza"): 2.5,
    ("Babi", "Senjak"): 3.0, ("Babi", "Deponija"): 14.0, ("Babi", "Baza"): 4.0,
    ("Deponija", "Baza"): 12.0, ("Deponija", "Senjak"): 11.0, ("Deponija", "Babi"): 14.0
}

naselbi = ["Senjak", "Babi"]

if st.button("Пресметај најкратка рута"):
    najkratka_ruta = None
    min_rastojanie = float('inf')
    
    # Сите комбинации за посета на населбите
    for p in itertools.permutations(naselbi):
        ruta = ["Baza"] + list(p) + ["Deponija"]
        tekovno_rastojanie = 0
        for i in range(len(ruta) - 1):
            tekovno_rastojanie += distanci.get((ruta[i], ruta[i+1]), 0)
            
        if tekovno_rastojanie < min_rastojanie:
            min_rastojanie = tekovno_rastojanie
            najkratka_ruta = ruta

    st.success(f"Најкратката рута е: {' -> '.join(najkratka_ruta)}")
    st.write(f"Вкупно растојание: {min_rastojanie} км")
