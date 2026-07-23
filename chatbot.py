from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

st.markdown("<h1 style='text-align: center;'>ChatBot</h1>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:

    if isinstance(msg, HumanMessage):
        st.markdown(
            f"""
            <div style="display:flex; justify-content:flex-end; margin-bottom:12px;">
                <div style="
                    background-color:#262730;
                    color:white;
                    padding:12px 16px;
                    border-radius:15px;
                    max-width:70%;
                ">
                  {msg.content} 👨‍💻 
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    else:
        with st.chat_message("assistant"):
            st.write(msg.content)


st.markdown(
    """
    <div style="
        text-align:center;
        color:#9ca3af;
        font-size:14px;
        margin-top:10px;
        margin-bottom:8px;
    ">
        ChatBot can make mistakes. Please verify important information. <br>
        <span style="font-size:13px;">
            Knowledge cutoff: <b>June 2024</b>. Events and information after June 2024 may be incomplete.
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

user_input = st.chat_input("Type your message")



if user_input:
    if user_input.strip().lower() == 'exit':
        st.stop()

    st.session_state.chat_history.append(HumanMessage(content=user_input))
    
    st.markdown(
    f"""
    <div style="display:flex; justify-content:flex-end; margin-bottom:12px;">
        <div style="
            background-color:#262730;
            color:white;
            padding:12px 16px;
            border-radius:15px;
            max-width:70%;
        ">
           {user_input} 👨‍💻
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

    result = model.invoke(st.session_state.chat_history)

    st.session_state.chat_history.append(AIMessage(content=result.content))

    with st.chat_message("assistant"):
        st.write(result.content)