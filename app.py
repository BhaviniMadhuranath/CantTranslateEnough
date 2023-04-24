import streamlit as st
from identification import identify_languagewords

def main():
    
    
    # Title of the app
    st.title("Can't Translate Enough")
    st.header("A language detector and Translator Application")

    # # Sidebar menu
    # menu = ["Home"]
    # choice = st.sidebar.selectbox("Select an option", menu)
    
    # Home page
   
    txt=st.text_input("write the sentence here")
    detect_language==identify_languagewords(txt)
        # Add your content here
    if detect_language=="english":
        st.write("Translated to French:", translated_text)
        st.write("Translated to German:", translated_text)
        st.write("Translated to Italian:", translated_text)
        st.write("Translated to Spanish:", translated_text)

    if detect_language=="french":
        st.write("Translated to English:", translated_text)
        st.write("Translated to German:", translated_text)
        st.write("Translated to Italian:", translated_text)
        st.write("Translated to Spanish:", translated_text)

    if detect_language=="german":
        st.write("Translated to English:", translated_text)
        st.write("Translated to French:", translated_text)
        st.write("Translated to Italian:", translated_text)
        st.write("Translated to Spanish:", translated_text)

    if detect_language=="I=italian":
        st.write("Translated to English:", translated_text)
        st.write("Translated to French:", translated_text)
        st.write("Translated to German:", translated_text)
        st.write("Translated to Italian:", translated_text)

    if detect_language=="spanish":
        st.write("Translated to English:", translated_text)
        st.write("Translated to French:", translated_text)
        st.write("Translated to German:", translated_text)
        st.write("Translated to Italian:", translated_text)
    # # About page
    # elif choice == "About":
    #     st.subheader("About Page")
    #     # Add your content here

if __name__ == '__main__':
    main()
