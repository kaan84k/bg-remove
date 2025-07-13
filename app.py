import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Background Remover", page_icon="🪄")
st.title("🪄 Background Remover App")
st.markdown("Upload an image, and we'll remove its background for you!")

# Initialize session state
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None
if "output_bytes" not in st.session_state:
    st.session_state.output_bytes = None

# File uploader
uploaded = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded:
    st.session_state.uploaded_file = uploaded
    input_bytes = uploaded.read()

    with st.spinner("Removing background..."):
        st.session_state.output_bytes = remove(input_bytes)

# Display results
if st.session_state.uploaded_file and st.session_state.output_bytes:
    col1, col2 = st.columns(2)
    with col1:
        st.image(st.session_state.uploaded_file, caption="Original", use_container_width=True)
    with col2:
        st.image(st.session_state.output_bytes, caption="Background Removed", use_container_width=True)

    # Download button
    st.download_button(
        label="📥 Download Transparent Image",
        data=st.session_state.output_bytes,
        file_name="no_background.png",
        mime="image/png"
    )

    # Clear button
    if st.button("❌ Clear Image"):
        st.session_state.uploaded_file = None
        st.session_state.output_bytes = None
        st.rerun() 
        
