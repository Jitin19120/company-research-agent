import re
import streamlit as st
from agent import generate_report

st.set_page_config(
    page_title="AI Investment Research Agent",
    page_icon="📈",
    layout="wide"
)

# -------------------- Header --------------------

st.title("📈 AI Investment Research Agent")
st.caption("AI Powered Investment Decision System")

st.divider()

# -------------------- Sidebar --------------------

with st.sidebar:

    st.header("About")

    st.info("""
### Features

✅ Company Overview

✅ Financial Health

✅ Growth Potential

✅ Competitive Position

✅ Risk Analysis

✅ Latest News

✅ Investment Recommendation

✅ Download Report
""")

# -------------------- Helpers --------------------

def extract_verdict(report):
    match = re.search(
        r"##\s*Final Verdict\s*\n+\s*(INVEST|WAIT|PASS)",
        report,
        re.IGNORECASE
    )
    if match:
        return match.group(1).upper()
    return "N/A"


def extract_confidence(report):
    match = re.search(
        r"##\s*Confidence Score\s*\n+\s*(\d{1,3})\s*%",
        report
    )
    if match:
        return f"{match.group(1)}%"
    return "N/A"


VERDICT_COLORS = {
    "INVEST": "#1DB954",
    "WAIT": "#FFC107",
    "PASS": "#E63946",
    "N/A": "#888888"
}

VERDICT_LABELS = {
    "INVEST": "✅ INVEST",
    "WAIT": "🟡 WAIT",
    "PASS": "❌ PASS",
    "N/A": "N/A"
}

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

        with st.spinner("Analyzing Company..."):

            report, sources = generate_report(company)

        verdict = extract_verdict(report)
        confidence = extract_confidence(report)
        color = VERDICT_COLORS.get(verdict, "#888888")
        label = VERDICT_LABELS.get(verdict, verdict)

        st.success("Report Generated Successfully!")

        st.markdown("---")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Company", company)

        with col2:
            st.markdown(
                f"""
                <div style="background-color:{color};padding:16px;border-radius:10px;text-align:center;color:white;">
                    <h3 style="margin:0;">{label}</h3>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:
            st.metric("Confidence Score", confidence)

        st.markdown("---")

        st.subheader("📄 Investment Research Report")

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
            file_name=f"{company}_investment_report.txt",
            mime="text/plain"
        )

st.markdown("---")
st.caption("Built using Python • Streamlit • LangChain • Groq AI")