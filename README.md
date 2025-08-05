# 🧠 Company News & Stock Chatbot (RAG + Mistral + Streamlit)

## 📌 Summary

This is an AI-powered chatbot that helps users find the **latest news and current stock prices** of one or more companies. It uses open-source tools and runs **completely offline**. You can ask it questions like:

> "What’s the latest about Tesla and Apple?"

It will fetch real-time data from the web, get stock values from Yahoo Finance, and generate simple, human-like answers using a powerful AI model.

---

## ❓ Problem Statement

In today’s fast-moving world, investors, researchers, and curious users often need quick updates on companies — including their **latest news**, **stock movements**, and **overall market sentiment**.

However, doing this manually by:

- Searching for news,
- Checking stock websites,
- Summarizing everything…

…takes **too much time and effort**.

---

## ✅ Solution

We built a smart, lightweight chatbot that:

- 📰 Scrapes and summarizes real-time company news
- 📈 Gets stock prices instantly
- 🧠 Uses RAG (Retrieval-Augmented Generation) to answer questions
- ⚡ Works locally using open-source models
- 💬 Runs in a web-based UI (Streamlit)

All you have to do is **ask your question**, and the bot will:

> ✅ Search → ✅ Fetch → ✅ Embed → ✅ Generate → ✅ Answer

---

## 🧰 Tech Stack

| Purpose           | Tool / Library                        |
|-------------------|----------------------------------------|
| Frontend UI       | Streamlit                              |
| LLM Model         | Mistral-7B via Ollama (offline)        |
| Web Scraping      | `newspaper3k`, `requests`, `bs4`       |
| Stock Price Fetch | `yfinance`                             |
| Embeddings        | `sentence-transformers` (all-MiniLM)   |
| Vector Storage    | Qdrant (lightweight, fast)             |
| Backend Language  | Python                                 |

---

## ⚙️ How It Works

1. User asks a question like:  
   **"Give me news and stock price of Google and Amazon"**

2. System:
   - Extracts company names
   - Fetches news articles for each company
   - Summarizes and stores them using Qdrant (vector DB)
   - Embeds the user query and finds relevant content
   - Uses **Mistral-7B** to generate a natural answer

3. Finally, it returns:
   - A **short summary**
   - The **current stock prices**
   - The **sources** (URLs)

---

## ❗ Challenges Faced

During development, we ran into several issues:

| Challenge                         | How We Solved It                                      |
|----------------------------------|--------------------------------------------------------|
| ❌ Some websites blocked scraping | Switched to multiple sources using `newspaper3k`      |
| ❌ LLM too slow on weak hardware  | Chose **Mistral-7B**, optimized via **Ollama**         |
| ❌ Chunking unstructured data     | Used cleaner chunking logic and stopped word limits    |
| ❌ Typos or vague questions       | Added fallback responses and fuzzy matching            |
| ❌ Streamlit slow with big models | Offloaded model loading with multiprocessing           |
| ❌ Local memory issue             | Limited context, optimized embeddings and summarizing  |

---

## 🚀 How to Run It Locally

### 1. Clone this Repository

```bash
git clone https://github.com/your-username/company-news-rag-chatbot.git
cd company-news-rag-chatbot
