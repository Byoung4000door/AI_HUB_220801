import streamlit as st

view = [100, 78, 4, 30]

st.write('# View List')

show = st.checkbox('show raw data')
if show == True:
    st.write('## raw data')
    view

st.write('## bar chart')
st.bar_chart(view)

st.write('## line chart')
st.line_chart(view)
