import streamlit as st
import itertools

st.set_page_config(page_title="Логистика ИСАР", layout="wide")
st.title("🚛 ЈП ИСАР - ШТИП: Логистички систем")

# Иницијализација на сесијата
if 'kamioni' not in st.session_state: st.session_state['kamioni'] = []
if 'naselbi' not in st.session_state: st.session_state['naselbi'] = []

tab1, tab2, tab3 = st.tabs(["🚛 Камиони", "🏠 Населби", "⚙️ Оптимизација"])

with tab1:
    st.header("Управување со возен парк")
    br_tablici = st.text_input("Регистарски таблички")
    kapacitet = st.number_input("Капацитет (тони)", min_value=1.0)
    if st.button("Додај камион"):
        st.session_state['kamioni'].append({"tablici": br_tablici, "kapacitet": kapacitet})
        st.success(f"Камион {br_tablici} додаден!")

with tab2:
    st.header("Дефинирање на населби")
    ime = st.text_input("Име на населба")
    kanti_100 = st.number_input("Број на канти (100л)", min_value=0, value=0)
    kontejneri_500 = st.number_input("Број на контејнери (500л)", min_value=0, value=0)
    
    if st.button("Додај населба"):
        litri = (kanti_100 * 100) + (kontejneri_500 * 500)
        st.session_state['naselbi'].append({"ime": ime, "litri": litri})
        st.success(f"Населба {ime} додадена ({litri} литри)")
    st.write("Моментални населби:", st.session_state['naselbi'])

with tab3:
    st.header("⚙️ План за работа")
    if st.button("Пресметај рута и капацитет"):
        if not st.session_state['naselbi'] or not st.session_state['kamioni']:
            st.warning("Внесете камион и населба!")
        else:
            vkupen_kapacitet_litri = sum(k['kapacitet'] for k in st.session_state['kamioni']) * 1000
            vkupno_otpad_litri = sum(n['litri'] for n in st.session_state['naselbi'])
            
            st.write(f"Вкупно отпад: {vkupno_otpad_litri} литри")
            st.write(f"Капацитет на камиони: {vkupen_kapacitet_litri} литри")
            
            ruta = ["Baza"] + [n['ime'] for n in st.session_state['naselbi']] + ["Deponija"]
            st.success(f"Оптимална рута: {' -> '.join(ruta)}")
            
            if vkupen_kapacitet_litri >= vkupno_otpad_litri:
                st.balloons()
                st.write("✅ Капацитетот е доволен.")
            else:
                st.error("⚠️ Внимание: Потребен е дополнителен камион!")
