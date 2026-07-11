import streamlit as st
from agent import generate_report

st.set_page_config(
    page_title="Company Research Agent",
    page_icon="📊",
    layout="wide"
)

# -------------------- Header --------------------

st.title("📊 Company Research Agent")
st.caption("AI Powered Company Analysis")

st.divider()

# -------------------- Sidebar --------------------

with st.sidebar:

    st.header("About")

    st.info("""
### Features

✅ Company Overview

✅ CEO

✅ Industry

✅ Products & Services

✅ Competitors

✅ Strengths

✅ Weaknesses

✅ Future Outlook

✅ Download Report
""")

# -------------------- Input --------------------

company = st.text_input(
    "Enter Company Name",
    placeholder="Example: Tesla"
)

# -------------------- Button --------------------

if st.button("🚀 Generate Report", use_container_width=True):

    if company.strip() == "":

        st.warning("Please enter a company name.")

    else:

        with st.spinner("Generating Report..."):

            report, sources = generate_report(company)

        st.success("Report Generated Successfully!")

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Company", company)

        with col2:
            st.metric("Status", "Research Completed")

        st.markdown("---")

        st.subheader("📄 Company Report")

        sections = report.split("## ")

        for section in sections:

            if section.strip() == "":
                continue

            lines = section.split("\n", 1)

            title = lines[0]

            content = lines[1] if len(lines) > 1 else ""

            with st.expander(title, expanded=True):
                st.markdown(content)

        st.download_button(
            label="📥 Download Report",
            data=report,
            file_name=f"{company}.txt",
            mime="text/plain"
        )

st.markdown("---")
st.caption("Built using Python • Streamlit • LangChain • Groq AI")