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

topics = [
    {'id':1, 'title':'html', 'view':100},
    {'id':2, 'title':'css', 'view':50},
    {'id':3, 'title':'js', 'view':140}
]
st.write('## raw data')
topics

st.write('## table')
st.table(topics)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)