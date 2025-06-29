import streamlit as st
import openai

def format_context(batting, bowling):
    # Example: Summarize key stats, can expand for richer context
    context = f"Total matches: {batting['date'].nunique() if 'date' in batting else 'N/A'}\n"
    context += f"Top run scorer: {batting.groupby('player')['runs_scored'].sum().idxmax() if 'runs_scored' in batting else 'N/A'}\n"
    context += f"Top wicket taker: {bowling.groupby('player')['wickets'].sum().idxmax() if 'wickets' in bowling else 'N/A'}\n"
    return context

def cricket_chatbot_ui(batting, bowling):
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    for role, msg in st.session_state["chat_history"]:
        st.markdown(f"**{role.capitalize()}:** {msg}")
    user_input = st.text_input("Ask a cricket stats question", key="chat_input")
    if st.button("Send", key="send_btn"):
        context = format_context(batting, bowling)
        # Replace with your OpenAI key and model
        openai.api_key = st.secrets["OPENAI_API_KEY"]
        prompt = f"Cricket Stats Context:\n{context}\nUser Question: {user_input}\nAnswer concisely:"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}]
        )
        analyst_reply = response.choices[0].message.content
        st.session_state["chat_history"].append(("user", user_input))
        st.session_state["chat_history"].append(("analyst", analyst_reply))
        st.experimental_rerun()