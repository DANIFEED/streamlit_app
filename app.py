# app.py
import streamlit as st

st.set_page_config(page_title="ML Projects", layout="wide")

# Данные проектов
PROJECTS = {
    "video_rag": {
        "title": "🎬 Multimodal Video RAG",
        "subtitle": "Умный поиск по образовательным видео",
        "input": ["🔗 Ссылка на YouTube", "❓ Вопрос"],
        "output": ["💬 Ответ", "⏱️ Таймкод", "🔗 Ссылка", "📄 Контекст"],
        "architecture": ["Frontend: Streamlit", "Backend: FastAPI", "STT: Whisper", "Vector DB: FAISS", "CV: YOLOv8"],
        "examples": ["'Когда градиентный спуск?' → 12:43", "'Где автомобиль?' → 03:21"],
        "sources": ["YouTube: MIT, Coursera", "10-20 видео"]
    },
    "meeting_assistant": {
        "title": "🎙️ AI Meeting Assistant",
        "subtitle": "Аналитика собеседований",
        "input": ["🎵 Аудио/видео", "❓ Вопрос"],
        "output": ["📝 Транскрипция", "📊 Summary", "✅ Action items"],
        "architecture": ["Frontend: Streamlit", "Backend: FastAPI", "STT: Whisper", "NLP: RAG", "Storage: FAISS"],
        "examples": ["'Сильные стороны?' → ML & stats", "'Что улучшить?' → SQL"],
        "sources": ["YouTube interviews", "10-15 интервью"]
    }
}

def render_project(project):
    # Белая подложка с отступами
    with st.container():
        st.markdown(f"""
        <div style="background: white; padding: 30px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
            <h2 style="color: black; margin: 0 0 5px 0; font-size: 28px;">{project["title"]}</h2>
            <p style="color: #666; margin: 0 0 25px 0; font-size: 18px;">{project["subtitle"]}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Секции с белой подложкой
        for section_title, items in [
            ("📥 Входные данные", project["input"]),
            ("📤 Результат", project["output"]),
            ("🏗️ Архитектура", project["architecture"]),
            ("💡 Примеры", project["examples"]),
            ("📚 Источники", project["sources"])
        ]:
            with st.container():
                st.markdown(f"""
                <div style="background: white; padding: 20px; border-radius: 12px; margin: 15px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.05); border-left: 4px solid #667eea;">
                    <h4 style="color: black; margin: 0 0 10px 0; font-size: 18px;">{section_title}</h4>
                    {''.join([f'<div style="color: black; padding: 5px 0; font-size: 15px;">• {item}</div>' for item in items])}
                </div>
                """, unsafe_allow_html=True)

def main():
    # Заголовок страницы
    st.markdown("""
    <style>
        .stApp { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        h1 { color: white; text-align: center; font-size: 36px; margin: 30px 0 10px; }
        .subtitle { color: rgba(255,255,255,0.9); text-align: center; font-size: 18px; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1>🧠 ML Project Ideas</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Выберите проект для просмотра</p>', unsafe_allow_html=True)
    
    # Вкладки
    tab1, tab2 = st.tabs(["🎬 Video RAG", "🎙️ Meeting Assistant"])
    
    with tab1:
        render_project(PROJECTS["video_rag"])
    
    with tab2:
        render_project(PROJECTS["meeting_assistant"])

if __name__ == "__main__":
    main()