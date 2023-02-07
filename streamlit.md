import streamlit as st

@st.cache()

def load_data():

src_file = Path.cwd() / 'notebooks' / 'data' / 'raw' / 'fuel_summary.csv'

raw_df = pd.read_csv(src_file)

return raw_df


##### Displaying Text                              
- st.text()
- st.markdown()
- st.latext()
- st.write()
- st.title()
- st.header()
- st.subheader()
- st.code()
- st.metric()


#### Widgets
- st.button()
- st.checkbox()
- st.radio()
- st.selectbox()
- st.slider()
- st.select_slider()
- st.text_input()
- st.number_input()
- st.text_area()
- st.date_input()
- st.timeinput()
- st.file_uploader()
- st.color_picker()


#### Layout
- st.sidebar()
- st.columns()
- st.expander()
- st.container()



## Pros:
- Using existing plotting libraries
- Simple API
- Professional display out of the box
- Open source & Commercial

## Cons:
- Young project rapidly evolving
- Integration into organizations may require commercial project


## Recommendation:
- Good place to start for adding interactivity
- Somewhat limited widgets and layout customizations, may need other
alternatives for more complex scenarios

