import streamlit as st
import json
from main import get_structured_output

# ----------------------------
# 🖼️ Branding and Page Setup
# ----------------------------
st.set_page_config(
    page_title="ClarifAI – Prompt Clarity Engine",
    layout="centered",
    page_icon="🤖"
)



# ---------------
# 💡 Title + Tagline
# ---------------
st.markdown("""
    <div style='text-align: center; padding-top: 1rem; padding-bottom: 1rem'>
        <h1 style='font-size: 3rem; margin-bottom: 0;'>🤖 ClarifAI</h1>
        <p style='font-size: 1.2rem; color: grey;'>From Vague Commands to Expert AI Prompts</p>
    </div>
""", unsafe_allow_html=True)

# ---------------
# 🧠 Prompt Input
# ---------------
with st.form("clarifai_form"):
    st.markdown("### 🗣️ Enter Your Vague Instruction")
    user_input = st.text_area("", height=150, placeholder="e.g. write a readme for a project that tracks rainfall data in real time...")
    submitted = st.form_submit_button("🔍 Generate Expert Prompt")

# ---------------
# ⚙️ Process Input
# ---------------
if submitted and user_input:
    with st.spinner("🧠 Interpreting and Structuring Your Prompt..."):
        result = get_structured_output(user_input)

    if result:
        st.success("✅ Structured Output Ready!")

        # Card UI style
        st.markdown("### 📦 Structured JSON")
        with st.expander("View JSON Output"):
            st.json(result)

        if "refined_prompt" in result:
            st.markdown("### 🎯 Refined Prompt (Copy-Paste Ready)")
            st.code(result["refined_prompt"], language="markdown")

        if "markdown_output" in result:
            st.markdown("### 📄 Markdown / Documentation")
            st.markdown(result["markdown_output"])

        st.download_button(
            label="📥 Download JSON",
            data=json.dumps(result, indent=2),
            file_name="structured_prompt.json",
            mime="application/json"
        )
    else:
        st.error("❌ Could not parse your instruction. Try rephrasing it.")

# ---------------
# 🚀 Footer
# ---------------
st.markdown("""<hr style="margin-top: 3rem;"/>""", unsafe_allow_html=True)

st.markdown("""
    <hr style='margin-top: 3rem; margin-bottom: 1rem; border: none; border-top: 1px solid #ccc;' />

    <div style='text-align: center; font-size: 0.9rem; color: #555; padding: 1rem 0 2rem 0;'>
        <p style='font-style: italic; color: #777;'>“We make sense of what you <em>think</em> you meant.”</p>
        <p>Built with 🤍 by <strong>Shashwat Kashyap</strong></p>
        <p>
            <a href='mailto:kashyapshashwat77@gmail.com' style='color: #1f77b4; text-decoration: none;'>📧 Email</a> · 
            <a href='https://github.com/Shashwat-k-9114' target='_blank' style='color: #1f77b4; text-decoration: none;'>💻 GitHub</a>
        </p>
    </div>
""", unsafe_allow_html=True)

