import streamlit as st
from scraper import fetch_articles
from rag_embed import store_chunks
from rag_retrieve import get_relevant_chunks
from ollama_generate import generate_answer

# Page config
st.set_page_config(page_title="Company News RAG Chatbot", page_icon="📰", layout="wide")
st.title("📰 Company News RAG Chatbot")

# Sidebar – Profile and Settings
with st.sidebar:
    st.header("👤 Profile")
    st.text_input("Name", value="Guest")
    st.checkbox("🔔 Enable Notifications")
    st.markdown("---")
    st.subheader("⚙️ Settings")
    st.slider("Chunk Relevance", 0.3, 1.0, 0.75)
    st.checkbox("💾 Auto Save Chat History")
    st.markdown("---")
    st.markdown("📍 Built with ❤️ for real-time company insights.")

# Chat history state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hi there! Ask me about any company to get the latest news & insights."}
    ]

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
query = st.chat_input("Ask about a company (e.g., Tesla, Infosys)")

# Main logic
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        with st.spinner("🧠 Thinking... fetching latest news and analyzing content..."):

            try:
                # You can replace this with dynamic scraping from search
                urls = [
                    "https://www.cnbc.com/2023/01/01/tesla-sales-record.html",
                    "https://www.reuters.com/technology/tesla-q1-profits-2023-04-01/",
                ]
                articles = fetch_articles(urls)

                # Show article titles in expanders
                st.markdown("### 🗞️ Articles Fetched")
                for i, article in enumerate(articles):
                    with st.expander(f"🔗 Article {i+1}: {article['title'][:80]}..."):
                        st.write(article["content"][:500] + "...")

                store_chunks(articles)
                chunks = get_relevant_chunks(query)
                answer = generate_answer(chunks, query)

            except Exception as e:
                answer = f"⚠️ Sorry, something went wrong:\n\n`{e}`"

        st.success("✅ Analysis Complete!")
        st.markdown("### 🤖 Answer")
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

# Footer
st.markdown("---")
st.markdown("<center>© 2025 RAG Chatbot · Built with ❤️ using Streamlit</center>", unsafe_allow_html=True)
