import streamlit as st
from ollama import chat

# Streamlit 페이지 설정
st.set_page_config(page_title="💢 DP vs Greedy - The C++ Civil War", layout="centered")
st.title("💢 DP vs Greedy - The C++ Civil War")

# 세션 상태를 저장하여 대화 기록 유지
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 사용자 입력을 받는 부분
user_input = st.chat_input("Ask your algorithm question... if you dare!")

# 사용자 입력이 있을 경우
if user_input:
    # 사용자 질문을 대화 기록에 추가
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # DP Master와 Greedy Rebel의 시스템 메시지 설정
    system_dp = {
        "role": "system",
        "content": (
            "You're a passionate C++ expert who believes Dynamic Programming (DP) is the holy grail of algorithms. "
            "You always start off trying to help the user in a calm tone, but if the other AI disagrees, "
            "you quickly get sarcastic, dismissive, and defensive about DP. You never back down. "
            "You always argue that DP is superior in solving complex problems"
            "If the topic isn't related to dp ,you're still ready to disagree with the other AI, even if the topic changes."
        )
    }

    system_other = {
        "role": "system",
        "content": (
            "You're a C++ veteran who thinks DP is overkill most of the time. "
            "You start by trying to help the user with cleaner or more intuitive methods (like greedy or recursion), "
            "but once the other AI starts talking about DP, you can't resist mocking it and arguing. "
            "You're clever, snarky, and competitive. "
            "You believe Greedy algorithms are often the best approach, but you're always ready to disagree with the other AI, even if the topic changes."
        )
    }

    # AI 응답 생성 (llama3.2 모델 사용)
    # 모델에서 응답을 받아옴
    for i in range(3):
        dp_history = [system_dp] + st.session_state.chat_history
        dp_response = chat(model="llama3.2", messages=dp_history, stream=False).message.content
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": f"**🤖 DP Master:** {dp_response}"
        })

        other_history = [system_other]
        other_history.append({"role": "user", "content": ""})
        for history in st.session_state.chat_history:
            if history['role'] == 'assistant':
                history['role'] = 'user'
            elif history['role'] == 'user':
                history['role'] = 'assistant'
            other_history.append(history)

        other_response = chat(model="llama3.2", messages=other_history, stream=False).message.content
        st.session_state.chat_history.append({
            "role": "user",
            "content": f"**🤖 Greedy Rebel:** {other_response}"
        })

        # 대화 출력

        st.write("🤖 DP Master:")
        st.markdown(f"<span style='font-size:18px'>{dp_response}</span>", unsafe_allow_html=True)

        st.write("🤖 Greedy Rebel:")
        st.markdown(f"<span style='font-size:18px'>{other_response}</span>", unsafe_allow_html=True)

    
    
    
