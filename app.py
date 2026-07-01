import streamlit as st
import itertools

st.set_page_config(page_title="Логистика ИСАР", layout="wide")
st.title("🚛 ЈП ИСАР - ШТИП: Логистички систем")

# Иницијализација на меморијата
if 'kamioni' not in st.session_state: st.session_state['kamioni'] = []
if 'naselbi' not in st.session_state: st.session_state['naselbi'] = []

tab1, tab2, tab3 = st.tabs(["🚛 Камиони", "🏠 Населби", "⚙️ Оптимизација"])

# ТАБ 1: Камиони
with tab1:
    st.header("Управување со возен парк")
    br_tablici = st.text_input("Регистарски таблички")
    kapacitet = st.number_input("Капацитет (тони)", min_value=1)
    if st.button("Додај камион"):
        st.session_state['kamioni'].append({"tablici": br_tablici, "kapacitet": kapacitet})
        st.success(f"Камион {br_tablici} додаден!")

# ТАБ 2: Населби
with tab2:
    st.header("Дефинирање на населби")
    nova_naselba = st.text_input("Име на населба")
    if st.button("Додај населба"):
        st.session_state['naselbi'].append(nova_naselba)
        st.success(f"Населба {nova_naselba} е додадена!")
    st.write("Моментални населби:", st.session_state['naselbi'])

# ТАБ 3: Оптимизација
with tab3:
    st.header("⚙️ План за работа")
    if st.button("Пресметај рута и капацитет"):
        if not st.session_state['naselbi'] or not st.session_state['kamioni']:
            st.warning("Ве молам внесете барем еден камион и една населба!")
        else:
            vkupen_kapacitet = sum(k['kapacitet'] for k in st.session_state['kamioni'])
            st.write(f"Вкупен капацитет: {vkupen_kapacitet} тони")
            
            naselbi = st.session_state['naselbi']
            ruta = ["Baza"] + naselbi + ["Deponija"]
            
            st.success(f"Рута: {' -> '.join(ruta)}")
            
            # Логика за проверка (пр. по 2 тони отпад од населба)
            if vkupen_kapacitet >= len(naselbi) * 2:
                st.balloons()
                st.write("✅ Капацитетот е доволен за денешната рута.")
            else:
                st.error("⚠️ Внимание: Потребен е дополнителен камион!")
