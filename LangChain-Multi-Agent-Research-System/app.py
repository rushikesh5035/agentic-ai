import time

import streamlit as st

from src.agents.agents import (
    build_reader_agent,
    build_search_agent,
    critic_chain,
    writer_chain,
)


st.set_page_config(
    page_title="Research Desk",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    :root {
        --paper: #08111f;
        --surface: #0f1b2d;
        --surface-raised: #132238;
        --ink: #edf4ff;
        --muted: #94a6bf;
        --line: #22344d;
        --blue: #4bb8ff;
        --blue-soft: #153653;
        --orange: #f5a15b;
        --green: #43d19a;
    }

    html, body, [class*="css"] {
        font-family: "DM Sans", sans-serif;
        color: var(--ink);
    }

    .stMarkdown, .stMarkdown p, .stMarkdown li {
        color: var(--ink);
        font-size: 0.94rem;
        line-height: 1.65;
    }

    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
    .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: var(--ink);
    }

    .stApp {
        background:
            radial-gradient(circle at 90% 0%, rgba(48, 128, 190, 0.14), transparent 27rem),
            var(--paper);
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }

    .block-container {
        max-width: 1220px;
        padding: 2rem 3rem 3.5rem;
    }

    .topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-bottom: 1.1rem;
        border-bottom: 1px solid var(--line);
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 0.7rem;
        font-family: "Space Grotesk", sans-serif;
        font-weight: 700;
        letter-spacing: -0.03em;
        color: var(--ink);
    }

    .brand-mark {
        display: grid;
        place-items: center;
        width: 1.85rem;
        height: 1.85rem;
        border-radius: 7px;
        background: var(--blue);
        color: white;
        font-size: 1.15rem;
    }

    .topbar-note {
        color: var(--muted);
        font-size: 0.78rem;
    }

    .hero {
        display: grid;
        grid-template-columns: minmax(0, 1.15fr) minmax(280px, 0.85fr);
        gap: 4rem;
        align-items: end;
        padding: 3.2rem 0 2.8rem;
    }

    .eyebrow {
        margin-bottom: 1rem;
        color: var(--blue);
        font-size: 0.76rem;
        font-weight: 700;
        letter-spacing: 0.02em;
    }

    .hero h1 {
        max-width: 700px;
        margin: 0;
        font-family: "Space Grotesk", sans-serif;
        font-size: clamp(2.2rem, 4.5vw, 4rem);
        line-height: 1;
        letter-spacing: -0.06em;
        color: var(--ink);
    }

    .hero h1 span {
        color: var(--blue);
    }

    .hero-copy {
        max-width: 370px;
        margin: 0 0 0.25rem;
        color: var(--muted);
        font-size: 0.98rem;
        line-height: 1.6;
    }

    .workspace {
        display: grid;
        grid-template-columns: minmax(0, 1.25fr) minmax(300px, 0.75fr);
        gap: 1.5rem;
        align-items: start;
    }

    .prompt-card, .pipeline-card, .report-card, .feedback-card {
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: 16px;
        box-shadow: 0 14px 32px rgba(0, 0, 0, 0.2);
    }

    .prompt-card {
        padding: 1.5rem;
    }

    .card-kicker {
        margin-bottom: 0.4rem;
        color: var(--muted);
        font-size: 0.78rem;
        font-weight: 700;
    }

    .card-title {
        margin: 0 0 1.4rem;
        font-family: "Space Grotesk", sans-serif;
        font-size: 1.2rem;
        letter-spacing: -0.04em;
    }

    .stTextInput > label {
        color: var(--ink) !important;
        font-size: 0.88rem !important;
        font-weight: 600 !important;
    }

    .stTextInput > div > div > input {
        min-height: 3.1rem;
        padding: 0.75rem 1rem !important;
        background: #0a1627 !important;
        border: 1px solid #2a405d !important;
        border-radius: 9px !important;
        color: var(--ink) !important;
        font-size: 0.98rem !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: var(--blue) !important;
        box-shadow: 0 0 0 3px rgba(75, 184, 255, 0.14) !important;
    }

    .stButton > button, .stDownloadButton > button {
        min-height: 2.7rem;
        border: 0 !important;
        border-radius: 9px !important;
        font-weight: 700 !important;
        transition: transform 160ms ease, box-shadow 160ms ease !important;
    }

    .stButton > button {
        background: var(--blue) !important;
        color: white !important;
        box-shadow: 0 8px 18px rgba(75, 184, 255, 0.18) !important;
    }

    .stButton > button:hover, .stDownloadButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 10px 22px rgba(75, 184, 255, 0.24) !important;
    }

    .stDownloadButton > button {
        background: var(--blue-soft) !important;
        color: var(--blue) !important;
    }

    .suggestions {
        display: flex;
        flex-wrap: wrap;
        gap: 0.45rem;
        margin-top: 1.15rem;
    }

    .suggestion {
        padding: 0.4rem 0.65rem;
        border: 1px solid var(--line);
        border-radius: 999px;
        color: var(--muted);
        font-size: 0.75rem;
    }

    .pipeline-card {
        padding: 1.5rem;
    }

    .pipeline-heading {
        display: flex;
        align-items: baseline;
        justify-content: space-between;
        margin-bottom: 1.2rem;
    }

    .pipeline-heading h2 {
        margin: 0;
        font-family: "Space Grotesk", sans-serif;
        font-size: 1.15rem;
        letter-spacing: -0.03em;
    }

    .pipeline-heading span {
        color: var(--muted);
        font-size: 0.75rem;
    }

    .step {
        display: grid;
        grid-template-columns: 2.1rem 1fr auto;
        gap: 0.7rem;
        align-items: center;
        min-height: 4rem;
        border-top: 1px solid var(--line);
    }

    .step-number {
        display: grid;
        place-items: center;
        width: 1.8rem;
        height: 1.8rem;
        border-radius: 50%;
        background: #1a2a41;
        color: var(--muted);
        font-size: 0.75rem;
        font-weight: 700;
    }

    .step.done .step-number {
        background: #123d35;
        color: var(--green);
    }

    .step.active .step-number {
        background: var(--blue-soft);
        color: var(--blue);
    }

    .step-title {
        font-weight: 700;
        font-size: 0.9rem;
    }

    .step-description {
        margin-top: 0.1rem;
        color: var(--muted);
        font-size: 0.75rem;
    }

    .step-status {
        color: #71829a;
        font-size: 0.7rem;
        font-weight: 700;
    }

    .step.done .step-status { color: var(--green); }
    .step.active .step-status { color: var(--blue); }

    .results-heading {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        margin: 2.7rem 0 1rem;
    }

    .results-heading h2 {
        margin: 0;
        font-family: "Space Grotesk", sans-serif;
        font-size: 1.35rem;
        letter-spacing: -0.05em;
    }

    .results-heading .rule {
        flex: 1;
        height: 1px;
        background: var(--line);
    }

    .report-card, .feedback-card {
        padding: 1.7rem 2rem;
    }

    .report-card {
        border-top: 3px solid var(--blue);
    }

    .feedback-card {
        margin-top: 1rem;
        border-top: 3px solid var(--orange);
    }

    .result-label {
        margin-bottom: 1.2rem;
        color: var(--blue);
        font-size: 0.76rem;
        font-weight: 700;
        letter-spacing: 0.02em;
    }

    .feedback-card .result-label { color: var(--orange); }

    .raw-output {
        margin-top: 1rem;
    }

    .raw-output pre {
        max-height: 360px;
        overflow: auto;
        white-space: pre-wrap;
        word-break: break-word;
        padding: 1rem;
        background: #0a1627;
        border: 1px solid var(--line);
        border-radius: 9px;
        color: #b8c7da;
        font-family: "DM Sans", sans-serif;
        font-size: 0.82rem;
        line-height: 1.6;
    }

    .footer {
        margin-top: 3.5rem;
        color: #71829a;
        font-size: 0.75rem;
        text-align: center;
    }

    @media (max-width: 800px) {
        .block-container { padding: 1.5rem 1rem 3rem; }
        .hero, .workspace { grid-template-columns: 1fr; }
        .hero { gap: 1.5rem; padding: 3rem 0 2.5rem; }
        .hero h1 { font-size: clamp(2.25rem, 12vw, 3.4rem); }
        .topbar-note { display: none; }
        .report-card, .feedback-card { padding: 1.4rem; }
    }

    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after { transition: none !important; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def step_state(results: dict, running: bool, step: str) -> str:
    if step in results:
        return "done"
    if running:
        sequence = ["search", "reader", "writer", "critic"]
        first_pending = next(
            (name for name in sequence if name not in results),
            None,
        )
        if step == first_pending:
            return "active"
    return "waiting"


def render_step(number: str, title: str, description: str, state: str) -> None:
    labels = {"done": "Complete", "active": "Working", "waiting": "Waiting"}
    icon = "✓" if state == "done" else number
    st.markdown(
        f"""
        <div class="step {state}">
            <div class="step-number">{icon}</div>
            <div>
                <div class="step-title">{title}</div>
                <div class="step-description">{description}</div>
            </div>
            <div class="step-status">{labels[state]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


for key, default in (("results", {}), ("running", False), ("done", False)):
    if key not in st.session_state:
        st.session_state[key] = default


st.markdown(
    """
    <div class="topbar">
        <div class="brand"><span class="brand-mark">◈</span> Research desk</div>
        <div class="topbar-note">A focused workspace for thoughtful research</div>
    </div>
    <section class="hero">
        <div>
            <div class="eyebrow">Multi-agent research system</div>
            <h1>Turn a question into a <span>clear point of view.</span></h1>
        </div>
        <p class="hero-copy">
            Four LangChain agents search, read, write, and review so you can
            move from a blank page to a grounded report.
        </p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="workspace">', unsafe_allow_html=True)
input_column, pipeline_column = st.columns([1.25, 0.75], gap="large")

with input_column:
    st.markdown(
        """
        <div class="prompt-card">
            <div class="card-kicker">Start with a question</div>
            <h2 class="card-title">What should we investigate?</h2>
        """,
        unsafe_allow_html=True,
    )

    topic = st.text_input(
        "Research topic",
        placeholder="e.g. How will AI change software engineering?",
        key="topic_input",
        label_visibility="visible",
    )
    run_btn = st.button(
        "Run research",
        use_container_width=True,
        type="primary",
    )

    st.markdown(
        """
        <div class="suggestions">
            <span class="suggestion">Future of AI agents</span>
            <span class="suggestion">AI and the job market</span>
            <span class="suggestion">Roadmap for AGI</span>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with pipeline_column:
    results = st.session_state.results
    st.markdown(
        """
        <div class="pipeline-card">
            <div class="pipeline-heading">
                <h2>Research pipeline</h2>
                <span>4 stages</span>
            </div>
        """,
        unsafe_allow_html=True,
    )
    render_step("01", "Search", "Find relevant sources", step_state(results, st.session_state.running, "search"))
    render_step("02", "Read", "Extract useful context", step_state(results, st.session_state.running, "reader"))
    render_step("03", "Write", "Draft the report", step_state(results, st.session_state.running, "writer"))
    render_step("04", "Review", "Check quality and gaps", step_state(results, st.session_state.running, "critic"))
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


if run_btn:
    if not topic.strip():
        st.warning("Add a research topic to get started.")
    else:
        st.session_state.results = {}
        st.session_state.running = True
        st.session_state.done = False
        st.rerun()


if st.session_state.running and not st.session_state.done:
    results = {}
    topic_value = st.session_state.topic_input

    with st.spinner("Searching for reliable sources..."):
        search_agent = build_search_agent()
        search_result = search_agent.invoke(
            {
                "messages": [
                    (
                        "user",
                        f"Find recent, reliable and detailed information about: {topic_value}",
                    )
                ]
            }
        )
        results["search"] = search_result["messages"][-1].content
        st.session_state.results = dict(results)

    with st.spinner("Reading the most useful source..."):
        reader_agent = build_reader_agent()
        reader_result = reader_agent.invoke(
            {
                "messages": [
                    (
                        "user",
                        f"Based on the following search results about '{topic_value}', "
                        "pick the most relevant URL and scrape it for deeper content.\n\n"
                        f"Search Results:\n{results['search'][:800]}",
                    )
                ]
            }
        )
        results["reader"] = reader_result["messages"][-1].content
        st.session_state.results = dict(results)

    with st.spinner("Writing the research report..."):
        research = (
            f"SEARCH RESULTS:\n{results['search']}\n\n"
            f"DETAILED SCRAPED CONTENT:\n{results['reader']}"
        )
        results["writer"] = writer_chain.invoke(
            {"topic": topic_value, "research": research}
        )
        st.session_state.results = dict(results)

    with st.spinner("Reviewing the report..."):
        results["critic"] = critic_chain.invoke({"report": results["writer"]})
        st.session_state.results = dict(results)

    st.session_state.running = False
    st.session_state.done = True
    st.rerun()


results = st.session_state.results
if results:
    st.markdown(
        """
        <div class="results-heading">
            <h2>Research output</h2>
            <div class="rule"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if "writer" in results:
        st.markdown(
            '<div class="report-card"><div class="result-label">Final report</div>',
            unsafe_allow_html=True,
        )
        st.markdown(results["writer"])
        st.markdown("</div>", unsafe_allow_html=True)
        st.download_button(
            "Download report",
            data=results["writer"],
            file_name=f"research_report_{int(time.time())}.md",
            mime="text/markdown",
        )

    if "critic" in results:
        st.markdown(
            '<div class="feedback-card"><div class="result-label">Review</div>',
            unsafe_allow_html=True,
        )
        st.markdown(results["critic"])
        st.markdown("</div>", unsafe_allow_html=True)

    with st.expander("View source material"):
        if "search" in results:
            st.markdown("**Search results**")
            st.code(results["search"], language="text")
        if "reader" in results:
            st.markdown("**Extracted content**")
            st.code(results["reader"], language="text")

st.markdown(
    """
    <div class="footer">
        Research desk · Powered by LangChain and Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
