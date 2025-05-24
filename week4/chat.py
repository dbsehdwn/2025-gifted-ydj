import streamlit as st
from ollama import chat

def rerun():
    st.session_state["rerun_flag"] = not st.session_state.get("rerun_flag", False)

def main():
    st.set_page_config(page_title="💢 DP Master vs Greedy Rebel - The C++ Civil War", layout="centered")
    st.title("💢 DP Master vs Greedy Rebel - The C++ Civil War")

    # 세션 상태 초기화
    if "scene" not in st.session_state:
        st.session_state.scene = "intro"
    if "user_question" not in st.session_state:
        st.session_state.user_question = ""
    if "dp_claim" not in st.session_state:
        st.session_state.dp_claim = ""
    if "greedy_claim" not in st.session_state:
        st.session_state.greedy_claim = ""
    if "choices" not in st.session_state:
        st.session_state.choices = []

    # 시스템 메시지 (역할)
    system_dp = {
        "role": "system",
        "content": (
            "You are DP Master, a passionate C++ expert who strongly believes that Dynamic Programming (DP) "
            "is the ultimate way to solve complex problems efficiently. "
            "Give a confident and friendly claim sentence about the user's question."
        )
    }
    system_greedy = {
        "role": "system",
        "content": (
            "You are Greedy Rebel, a clever C++ veteran who thinks greedy algorithms are simpler and often better. "
            "Give a snarky but clever claim sentence responding to the user's question."
        )
    }
    system_choice = {
        "role": "system",
        "content": (
            "You create three dynamic and natural choices for the user to select from, based on the two claims. "
            "Make each choice a short sentence starting with either 'Call DP Master', 'Call Greedy Rebel', or 'Call both for debate'."
        )
    }

    if st.session_state.scene == "intro":
        st.markdown("👑 **Sortland 왕국에 새로운 도전이 왔다!**")
        if st.button("➡ 질문하기"):
            st.session_state.scene = "ask_question"
            rerun()
            return

    elif st.session_state.scene == "ask_question":
        question = st.chat_input("❓ 당신의 질문을 입력하세요:")
        if question:
            st.session_state.user_question = question
            st.session_state.scene = "generate_claims"
            rerun()
            return

    elif st.session_state.scene == "generate_claims":
        dp_messages = [
            system_dp,
            {"role": "user", "content": st.session_state.user_question},
        ]
        dp_claim = chat(model="llama3.2", messages=dp_messages, stream=False).message.content.strip()
        st.session_state.dp_claim = dp_claim

        greedy_messages = [
            system_greedy,
            {"role": "user", "content": st.session_state.user_question},
        ]
        greedy_claim = chat(model="llama3.2", messages=greedy_messages, stream=False).message.content.strip()
        st.session_state.greedy_claim = greedy_claim

        choice_messages = [
            system_choice,
            {"role": "user", "content": f"DP Master 주장: {dp_claim}\nGreedy Rebel 주장: {greedy_claim}"}
        ]
        choices_text = chat(model="llama3.2", messages=choice_messages, stream=False).message.content.strip()
        choices = [line.strip() for line in choices_text.split('\n') if line.strip()]
        st.session_state.choices = choices

        st.session_state.scene = "show_claims"
        rerun()
        return

    elif st.session_state.scene == "show_claims":
        st.markdown(f"👨‍🏫 **DP Master 주장:** {st.session_state.dp_claim}")
        st.markdown(f"🔥 **Greedy Rebel 주장:** {st.session_state.greedy_claim}")

        st.markdown("🤔 **누구를 부르시겠습니까?**")
        choice = st.radio("선택지:", st.session_state.choices)

        if st.button("✅ 결정"):
            st.session_state.selected_choice = choice
            st.session_state.scene = "result"
            rerun()
            return

    elif st.session_state.scene == "result":
        st.markdown(f"🎉 당신은 이렇게 선택했습니다:\n\n**{st.session_state.selected_choice}**")

        if st.button("⬅ 다시 시작"):
            st.session_state.scene = "intro"
            st.session_state.user_question = ""
            st.session_state.dp_claim = ""
            st.session_state.greedy_claim = ""
            st.session_state.choices = []
            rerun()
            return

if __name__ == "__main__":
    main()
