#Import the required libraries
import streamlit as st
from PIL import Image

from AT import AT_misc

Image.MAX_IMAGE_PIXELS = 1e14


st.set_page_config(layout="wide")




AT_misc.build_heading(head=     'Aesthetics Toolbox',
                      notes=    'This is a toolbox for aesthetics research. \
                                  The features of this toolbox can be selected from the sidebar and are briefly explained below. \
                                  The toolbox is designed as an open source project and we hereby encourage any feedback \
                                  or extensions to the toolbox (see contacts below). '
                      )

st.divider() 



### Define custom markdowns
st.markdown(""" <style> .font1 {
font-size:20px ; font-family: 'Cooper Black'; color: black;} 
</style> """, unsafe_allow_html=True)


st.markdown(""" <style> .contr {
font-size:16px ; font-family: 'Cooper Black'; color: black;} 
</style> """, unsafe_allow_html=True)

st.markdown(""" <style> .greenL {
font-size:28px ; font-family: 'Cooper Black'; color: green;} 
</style> """, unsafe_allow_html=True)

st.markdown(""" <style> .subhead {
font-size:28px ;  font-family: 'Cooper Black'; color: #FF9633;}
</style> """, unsafe_allow_html=True)


st.markdown('<p class="subhead">Toolbox Features</p>', unsafe_allow_html=True)

    
left, cen, right = st.columns( [ 0.45, 0.1 , 0.45])  
with left:
        
    ### QIP Machine
    st.markdown('<p class="greenL">QIP Machine</p>', unsafe_allow_html=True)
    st.markdown('<p class="font1">The QIP Machine is an interface for calculating commonly \
                studied quantitative image properties (QIPs).</p>', unsafe_allow_html=True)
    st.page_link("pages/1_📊_QIP_Machine.py", label='Go to the QIP Machine', icon="▶️")
    
with right:
    ### QIP Documentation
    st.markdown('<p class="greenL">QIP Documentation</p>', unsafe_allow_html=True)
    st.markdown('<p class="font1">The QIP Documentation provides the user with detailed information for each of the \
                quantitative image properties (QIPs) that can be calculated with the QIP Machine.</p>', unsafe_allow_html=True)
    st.page_link("pages/3_📒_QIP_Documentation.py", label='Go to the QIP Documentation', icon="▶️")
    
# st.write(' ')
# left, cen, right = st.columns( [ 0.45, 0.1 , 0.45])  

# with left:
#     ### Aesthetics datasets
#     st.markdown('<p class="greenL">Aesthetics Datasets</p>', unsafe_allow_html=True)
#     st.markdown('<p class="font1">This feature lists an extensive collection of image datasets \
#                 used in aesthetics research, along with important metrics for each dataset. \
#                 It allows you to search and filter for specific datasets. A download link is provided for each dataset.</p>', unsafe_allow_html=True)
# with right:
#     ### Datasets Documentation
#     st.markdown('<p class="greenL">Datasets Documentation</p>', unsafe_allow_html=True)
#     st.markdown('<p class="font1">Addition information for each aesthetics dataset can be found in the Dataset Documentation.</p>', unsafe_allow_html=True)
    
    
st.write(' ')
left, cen, right = st.columns( [ 0.45, 0.1 , 0.45])  
    

with left:
    ### Resizing and Cropping
    st.markdown('<p class="greenL">Image Preprocessing</p>', unsafe_allow_html=True)
    st.markdown('<p class="font1">This feature allows you to preprocess images. \
                A variety of resizing, cropping, padding and other options are implemented here. </p>', unsafe_allow_html=True)
    st.page_link("pages/2_🔧_Image_preprocessing.py", label='Go to the Image preprocessing', icon="▶️")
                
with right:
    ### References
    st.markdown('<p class="greenL">References</p>', unsafe_allow_html=True)
    st.markdown('<p class="font1">Lists all references cited in this toolbox. </p>', unsafe_allow_html=True)
    st.page_link("pages/4_📚_References.py", label='Go to the References', icon="▶️")
    
st.divider()

st.markdown('<p class="contr">Contributers</p>', unsafe_allow_html=True)
st.markdown('Ralf Bartho: Toolbox concept, code development, maintenance, bugfixes', unsafe_allow_html=True)
st.markdown('Christoph Redies: Toolbox concept, supervision of the project, QIP documentation', unsafe_allow_html=True)
st.markdown('Gregor Hayn-Leichsenring: Toolbox concept', unsafe_allow_html=True)
st.markdown('Lisa Kossmann, Johan Wagemanns: Development of the dataset feature', unsafe_allow_html=True)
st.markdown('Branka Spehar, Ronald Hübner, George Mather: Provided code to compute image properties', unsafe_allow_html=True)

        
st.write('')

st.markdown('<p class="contr">Contact and GitHub</p>', unsafe_allow_html=True)
st.markdown('Questions, suggestions, bugs: ralf.bartho@gmail.com', unsafe_allow_html=True)
st.markdown('GitHub repository: https://github.com/RBartho/Aesthetics-Toolbox', unsafe_allow_html=True)


# st.markdown('<p class="contr">check out this [link](%s)/p>' % url, unsafe_allow_html=True)

# st.markdown('<p class="contr">check out this [link](%s) </p>' % url, unsafe_allow_html=True)

# ### Define custom markdowns
# st.markdown(""" <style> .font0 {
# font-size:28px ; font-family: 'Cooper Black'; color: black;} 
# </style> """, unsafe_allow_html=True)

# st.markdown(""" <style> .font1 {
# font-size:20px ; font-family: 'Cooper Black'; color: black;} 
# </style> """, unsafe_allow_html=True)

# st.markdown(""" <style> .head {
# font-size:35px ;  font-family: 'Cooper Black'; color: #FF9633;}
# </style> """, unsafe_allow_html=True)

# st.markdown(""" <style> .subhead {
# font-size:28px ;  font-family: 'Cooper Black'; color: #FF9633;}
# </style> """, unsafe_allow_html=True)


# st.markdown(""" <style> .font2 {
# font-size:20px ; font-family: 'Cooper Black'; color: green;} 
# </style> """, unsafe_allow_html=True)

# st.markdown(""" <style> .greenL {
# font-size:28px ; font-family: 'Cooper Black'; color: green;} 
# </style> """, unsafe_allow_html=True)

# st.markdown(""" <style> .font3 {
# font-size:18px ; font-family: 'Cooper Black'; color: black;} 
# </style> """, unsafe_allow_html=True)

# st.markdown(""" <style> .font4 {
# font-size:16px ; font-family: 'Cooper Black'; color: black;} 
# </style> """, unsafe_allow_html=True)















# ############################################################
# ################ define sidebar ############################
# ############################################################

# ### set width of the sidebar
# st.markdown(
#     """
#     <style>
#         section[data-testid="stSidebar"] {
#             width: 100px !important; # Set the width to your desired value
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.sidebar.header("Sidebar")

# ### define order and names of sidebar menu
 
# # app_mode = st.sidebar.selectbox('Select mode',['Home' , 'QIP Machine',  'Aesthetics Datasets',  'Resizing and Cropping', 'Docs QIPs', 'Docs Datasets', 'References', ] ) #three pages

# app_mode = st.sidebar.selectbox('Select mode',['Home' , 'QIP Machine',   'Image preprocessing', 'Documentation QIPs',  'References', ] ) #three pages


# if app_mode == 'Home':
#     Frontpage.show_frontpage()

# if app_mode == 'QIP Machine':
#     QIPmachine.run_QIP_machine()
 
# # if app_mode == 'Aesthetics Datasets':
# #     Datasets.show_list()

# if app_mode == 'Image preprocessing':
#     Resizing.run_resizing()
    
# if app_mode == 'Documentation QIPs':
#     QIP_Documentation.show_docs()
    
# # if app_mode == 'Documentation Datasets':
# #     Datasets_documentation.show_data_docs()
    
# if app_mode == 'References':
#     References.show_references()
    


    