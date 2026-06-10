import pandas as pd
import chromadb
import streamlit as st
import os
from groq import Groq

from dotenv import load_dotenv
load_dotenv()
client_groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

@st.cache_resource
def load_db():
    client = chromadb.Client()
    collection = client.create_collection("prompts")
    df = pd.read_excel("data.xlsx")
    for _, row in df.iterrows():
        collection.add(
            documents=[str(row["prompt"])],
            metadatas=[{"status": str(row["status"]), "id": int(row["id"])}],
            ids=[str(row["id"])]
        )
    return collection

collection = load_db()
st.set_page_config(page_title="CG Prompt Agent", layout="wide")
st.title("🎨 UE5 Cinematic Prompt Optimizer")
st.caption("RAG-powered prompt engineering based on 116 real generation experiments")

user_query = st.text_area("Describe your visual intent:", placeholder="e.g. A giant skeleton blending into a jungle environment...")

if st.button("Generate Optimized Prompt"):
    with st.spinner("Retrieving knowledge base..."):
        results = collection.query(query_texts=[user_query], n_results=3)

    docs = results["documents"][0]
    metadatas = results["metadatas"][0]

    context = ""
    for i, (doc, meta) in enumerate(zip(docs, metadatas)):
        context += "[Case " + str(i+1) + " | ID: " + str(meta['id']) + " | Status: " + meta['status'].upper() + "]\n" + doc + "\n"

    system_prompt = "You are a UE5 Cinematic Prompt Engineering Expert.\n\nA user wants to generate an image with this intent:\n\"" + user_query + "\"\n\nHere are the most relevant cases from a real experiment knowledge base:\n" + context + "\nYour task:\n1. Analyze why the FAILURE cases failed for this intent\n2. Extract what made the SUCCESS cases work\n3. Generate an optimized prompt for this CG style\n4. Explain your reasoning\n\nRespond in this exact format:\n**Optimized Prompt:**\n[your optimized prompt here]\n\n**Reasoning:**\n[explain what you learned from the success/failure cases and why you wrote the prompt this way]\n\n**Referenced Cases:**\n[list the case IDs and their status]"
    with st.spinner("Agent is thinking..."):
        response = client_groq.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": system_prompt}],
            max_tokens=1000
        )
        output = response.choices[0].message.content

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚀 Optimized Prompt")
        optimized = output.split("**Reasoning:**")[0].replace("**Optimized Prompt:**", "").strip()
        st.code(optimized, language="text")

    with col2:
        st.subheader("💡 Reasoning & Lessons Learned")
        if "**Reasoning:**" in output and "**Referenced Cases:**" in output:
            reasoning = output.split("**Reasoning:**")[1].split("**Referenced Cases:**")[0].strip()
            st.write(reasoning)

    st.divider()
    st.subheader("📚 Referenced Cases from Knowledge Base")
    for meta, doc in zip(metadatas, docs):
        status_emoji = "✅" if meta["status"] == "success" else "❌"
        img_path = "images/" + str(meta['id']) + ".jpg"
        col_img, col_text = st.columns([1, 3])
        with col_img:
            if os.path.exists(img_path):
                st.image(img_path, width=150)
        with col_text:
            st.write(status_emoji + " **Case ID: " + str(meta['id']) + " | " + meta['status'].upper() + "**")
            st.caption(doc[:200] + "...")