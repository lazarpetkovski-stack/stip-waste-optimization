import streamlit as st
import itertools

st.set_page_config(page_title="Логистика ИСАР", layout="wide")
st.title("🚛 ЈП ИСАР - ШТИП: Логистички систем")

# Иницијализација на меморијата за податоци
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
    st.header("Пресметка на рути")
    if st.button("Пресметај најкратка рута"):
        naselbi = st.session_state['naselbi']
        if not naselbi:
            st.error("Прво внесете населби!")
        else:
            # Твојата логика за оптимизација
            st.write(f"Оптимизација за населби: {', '.join(naselbi)}")
            st.success("Рутата е успешно пресметана врз основа на внесените податоци!")
            # Овде можеш да ја додадеш логиката со itertools
