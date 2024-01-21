import streamlit as st
st.title("Introduction")

tab1,tab2 = st.tabs(["⬇️Installation","🚀Lancement" ])

with tab1 : 
    st.markdown("""
                Pour installer streamlit, il vous faut avoir Python installés sur votre machine. 
                
                En suite, allez dans l'invite de commade et lacez la commade : 
                """)
    code_install = """pip install streamlit
                    """
    st.code(code_install, language="bash")
    st.markdown("""
                Bravo, vous venez d'installer **Streamlit** ! 
                """)
    
with tab2 : 
    st.markdown("""
                Une application démo est fournie lors de l'installation du package streamlit. 
                
                Pour la lancer, il suffit d'entrer dans l'invite de commande : """)
    code_install_ = """streamlit hello"""
    st.code(code_install_, language="bash")