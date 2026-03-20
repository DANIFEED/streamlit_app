# app.py
import streamlit as st

st.set_page_config(page_title="ML Project Ideas", layout="wide", page_icon="🧠")

# =============================================================================
# 📦 ДАННЫЕ ВСЕХ ПРОЕКТОВ (13 идей)
# =============================================================================
PROJECTS = {
    "second_brain": {
        "title": "🧠 Personal Second Brain",
        "subtitle": "Визуальный граф знаний",
        "description": "Система превращает разрозненные заметки в связанную сеть знаний, где информация сама находит связи.",
        "input": ["📝 Текст заметки", "🔗 Ссылка", "💡 Идея"],
        "output": ["🔗 Связанные заметки", "🏷️ Авто-теги", "💭 Инсайты и связи"],
        "architecture": ["Embeddings + Qdrant", "LLM для авто-тегов", "Similarity Search", "RAG для вопросов"],
        "examples": ["Новая заметка → найти похожие → показать связи", "Ты сохранял рецепт → связанные покупки → список"],
        "sources": ["Личные заметки", "Notion/Obsidian интеграция"],
        "wow": "⭐⭐⭐⭐",
        "complexity": "⭐⭐⭐⭐",
        "risk": "⚠️ Высокий"
    },
    "video_rag": {
        "title": "🎬 Multimodal Video RAG",
        "subtitle": "Умный поиск по образовательным видео",
        "description": "Система анализирует видео с лекциями и отвечает на вопросы, возвращая точные таймкоды.",
        "input": ["🔗 Ссылка на YouTube", "❓ Вопрос на естественном языке"],
        "output": ["💬 Текстовый ответ", "⏱️ Точный таймкод (12:43)", "🔗 Ссылка с переходом", "📄 Контекстный фрагмент"],
        "architecture": ["Frontend: Streamlit", "Backend: FastAPI", "STT: Whisper", "Vector DB: FAISS", "CV: YOLOv8 (опционально)"],
        "examples": ["'Когда градиентный спуск?' → 12:43", "'Где автомобиль?' → 03:21 (YOLO)", "'Что про overfitting?' → 18:05"],
        "sources": ["YouTube: MIT, Coursera, ML-каналы", "10-20 размеченных видео"],
        "wow": "⭐⭐⭐⭐⭐",
        "complexity": "⭐⭐⭐⭐",
        "risk": "⚠️ Средний"
    },
    "meeting_assistant": {
        "title": "🎙️ AI Meeting Assistant",
        "subtitle": "Аналитика технических собеседований",
        "description": "Автоматическая транскрипция, саммари и извлечение инсайтов из записей интервью.",
        "input": ["🎵 Аудио/видео файл (.mp3, .wav, .mp4)", "❓ Опциональный вопрос для поиска"],
        "output": ["📝 Транскрипция с таймкодами", "📊 Auto-summary", "✅ Action items", "🔍 Семантический поиск"],
        "architecture": ["Frontend: Streamlit", "Backend: FastAPI", "STT: Whisper", "NLP: RAG", "Storage: FAISS"],
        "examples": ["'Сильные стороны?' → ML & stats", "'Где нейросети?' → 07:15", "'Что улучшить?' → SQL"],
        "sources": ["YouTube interviews", "Подкасты", "10-15 интервью"],
        "wow": "⭐⭐⭐",
        "complexity": "⭐⭐",
        "risk": "✅ Низкий"
    },
    "shopping_agent": {
        "title": "🛍️ Personal Shopping Agent",
        "subtitle": "Персональный AI-стилист",
        "description": "Система понимает стиль пользователя и помогает подбирать одежду, как персональный стилист.",
        "input": ["📷 Фото вещи", "👤 Профиль пользователя", "💰 Бюджет"],
        "output": ["👔 Похожие вещи", "✅ Подходит ли тебе", "🎨 С чем носить"],
        "architecture": ["CLIP Embeddings", "Поиск похожих", "LLM для объяснений", "Recommendation System"],
        "examples": ["'Покажи похожие куртки' → 5 вариантов", "'С чем носить эту рубашку?' → 3 образа"],
        "sources": ["E-commerce датасеты", "Fashion изображения"],
        "wow": "⭐⭐⭐⭐",
        "complexity": "⭐⭐⭐⭐",
        "risk": "⚠️ Средний"
    },
    "resume_analyzer": {
        "title": "📄 AI Resume & Interview Prep",
        "subtitle": "Умный анализ резюме и подготовка к интервью",
        "description": "Система анализирует резюме и вакансию, находит пробелы и проводит mock-интервью с оценкой.",
        "input": ["📄 Резюме (PDF/DOCX)", "📋 Текст вакансии", "🎓 Учебные материалы"],
        "output": ["🧠 Анализ навыков", "📊 Match Score", "🎤 5-7 вопросов", "📚 Рекомендации"],
        "architecture": ["PyMuPDF + python-docx", "Whisper (для видео)", "Vector DB: Chroma/FAISS", "LLM: GPT/Claude"],
        "examples": ["'Объясни переобучение' → вопрос из ML лекции", "'Как анализировать отток?' → кейс под вакансию"],
        "sources": ["Учебные лекции (PDF/transcripts)", "3-10 видео", "ML, SQL, Data Analysis темы"],
        "wow": "⭐⭐⭐⭐",
        "complexity": "⭐⭐⭐",
        "risk": "⚠️ Средний"
    },
    "policy_generator": {
        "title": "📑 AI Policy Generator",
        "subtitle": "Генерация документов для компании в РФ",
        "description": "Генерация минимально необходимых документов для новой компании в России на основе законодательства.",
        "input": ["🏢 Профиль компании", "📋 Тип бизнеса", "👥 Наличие сотрудников", "🌐 Сайт/форма сбора данных"],
        "output": ["📄 Список необходимых документов", "📑 Черновики документов", "🧠 Обоснование", "⚠️ Предупреждения"],
        "architecture": ["Streamlit + FastAPI", "Vector DB: FAISS/pgvector", "LLM: GPT/Claude", "Rules Engine (Python)"],
        "examples": ["IT-компания, 5 сотрудников, есть сайт → 6 документов", "Интернет-магазин без сотрудников → 3 документа"],
        "sources": ["Федеральные законы РФ", "Подзаконные акты", "Разъяснения регуляторов"],
        "wow": "⭐⭐⭐⭐",
        "complexity": "⭐⭐⭐",
        "risk": "⚠️ Средний"
    },
    "career_analyzer": {
        "title": "💼 AI Career Market Analyzer",
        "subtitle": "Анализ рынка вакансий и рекомендации",
        "description": "Анализ рынка вакансий с персональными рекомендациями по профессии на основе реальных данных.",
        "input": ["👤 Профессия", "📊 Уровень (Junior/Middle/Senior)", "🛠️ Навыки", "🌍 Предпочтения (регион, remote)"],
        "output": ["🌍 Анализ рынка", "💰 Зарплаты (min/median/max)", "🧠 Top Required Skills", "📚 Персональные рекомендации"],
        "architecture": ["Streamlit + PostgreSQL", "O*NET + Adzuna API", "spaCy + embeddings", "Scoring система"],
        "examples": ["'Data Analyst, Python+SQL, Канада' → спрос + зарплаты", "'QA → Data Science' → skill gap + план"],
        "sources": ["O*NET database", "NOC (Canada)", "Adzuna API", "Job Bank"],
        "wow": "⭐⭐⭐⭐",
        "complexity": "⭐⭐⭐",
        "risk": "⚠️ Средний"
    },
    "fake_news": {
        "title": "📰 AI Fake News Analyzer",
        "subtitle": "Анализ новостей и оценка вероятности фейка",
        "description": "Анализ новостей и оценка вероятности фейка на основе текста и проверенных примеров.",
        "input": ["📰 Заголовок новости", "📄 Полный текст", "🔗 Источник (опционально)"],
        "output": ["🧠 Вердикт (true/fake/evidence)", "📊 Confidence Score", "📎 Похожие проверенные материалы", "🧾 Объяснение"],
        "architecture": ["Streamlit + FastAPI", "LIAR/FEVER datasets", "BERT/DistilBERT classifier", "FAISS для semantic search"],
        "examples": ["'Вставить текст новости' → likely fake (78%)", "'Проверить утверждение' → insufficient evidence"],
        "sources": ["LIAR / LIAR-2", "FEVER", "FakeNewsNet", "Fact-check datasets"],
        "wow": "⭐⭐⭐⭐",
        "complexity": "⭐⭐⭐",
        "risk": "⚠️ Средний"
    },
    "veritas_ai": {
        "title": "⚖️ Veritas AI — Цифровой Прокурор",
        "subtitle": "Guardrails для корпоративных ИИ-решений",
        "description": "Умный фильтр, который проверяет ответы ИИ на факты перед показом пользователю (Zero-Trust AI).",
        "input": ["🤖 Ответы LLM", "📊 Финансовые отчёты (PDF/XLSX)", "💻 Программный код", "🖼️ Генеративные изображения"],
        "output": ["📊 Confidence Score (0-100%)", "✅ Verified / ❌ Rejected", "📑 Сертификат доверия", "⚠️ Предупреждения о рисках"],
        "architecture": ["FastAPI + Streamlit", "LangGraph (Multi-Agent Jury)", "DeBERTa (NLI)", "pgvector + PostgreSQL"],
        "examples": ["'Прибыль +10%' → проверка в Excel → ✅ Verified", "'6 пальцев на фото' → ❌ Rejected"],
        "sources": ["Корпоративные регламенты", "Законодательство", "База паттернов галлюцинаций"],
        "wow": "⭐⭐⭐⭐⭐",
        "complexity": "⭐⭐⭐⭐⭐",
        "risk": "⚠️ Высокий"
    },
    "scam_sentinel": {
        "title": "🛡️ ScamSentinel AI",
        "subtitle": "Детекция мошенничества в реальном времени",
        "description": "Мультимодальный щит для выявления цифрового мошенничества (голос, текст, изображения).",
        "input": ["🎵 Аудио звонка", "📷 Скриншоты/фото документов", "🔗 URL", "📄 Текст сообщения"],
        "output": ["📊 Scam Score (0-100%)", "🎯 Тип атаки (Deepfake/Phishing)", "📑 Транскрипт с разметкой", "⚠️ Риски"],
        "architecture": ["FastAPI + Streamlit", "LangGraph (Cross-Check Agent)", "Whisper + Wav2Vec2", "ViT (Image ELA)"],
        "examples": ["'Звонок от родственника' → Voice Deepfake detected", "'Скриншот чека' → ретушь обнаружена"],
        "sources": ["ASVspoof", "PhishTank", "Ручная разметка экспертов"],
        "wow": "⭐⭐⭐⭐⭐",
        "complexity": "⭐⭐⭐⭐⭐",
        "risk": "⚠️ Высокий"
    },
    "avatar_factory": {
        "title": "🎭 Avatar Factory",
        "subtitle": "Мастерская цифровых личностей",
        "description": "Высокореалистичный видеоконтент на основе одной фотографии и текста (AI-аватары).",
        "input": ["📷 Портрет (Hi-Res)", "📝 Сценарий", "🎵 Аудио (MP3/WAV)"],
        "output": ["🎬 Видео (MP4, 1080p+)", "📝 Субтитры (SRT)", "📊 Confidence Score", "⚠️ Риски (детектор дипфейков)"],
        "architecture": ["FastAPI + Streamlit", "LangGraph (QA Loop)", "ElevenLabs (TTS)", "LivePortrait/SadTalker"],
        "examples": ["'Фото + текст' → 3 мин видео с lip-sync", "'Грустный голос + весёлая мимика' → авто-коррекция"],
        "sources": ["HDTF", "VoxCeleb 2", "Студийные записи (Ground Truth)"],
        "wow": "⭐⭐⭐⭐⭐",
        "complexity": "⭐⭐⭐⭐⭐",
        "risk": "⚠️ Высокий"
    },
    "infinite_oracle": {
        "title": "🎮 Infinite Oracle",
        "subtitle": "Консистентный мир для игр",
        "description": "Вечный сюжетный движок, который превращает видеоигру в живую экосистему с абсолютной памятью.",
        "input": ["📊 JSON-графы World State", "📝 Логи действий игрока", "👤 Профили NPC"],
        "output": ["📊 Quest Graph", "💬 Контекстные диалоги NPC", "📍 Описание локаций", "⚠️ Детекция Soft-locks"],
        "architecture": ["FastAPI + Streamlit", "LangGraph (Cycle of Consequences)", "Neo4j (жесткие связи)", "pgvector (память)"],
        "examples": ["'Сжёг мельницу' → цены на хлеб выросли", "'NPC передают слухи' → репутация меняется"],
        "sources": ["Fallout/Baldur's Gate транскрипты", "Синтетические данные (GPT-4)"],
        "wow": "⭐⭐⭐⭐⭐",
        "complexity": "⭐⭐⭐⭐⭐",
        "risk": "⚠️ Высокий"
    },
    "kirill_mefodiy": {
        "title": "📚 Кирилл & Мефодий AI",
        "subtitle": "Мультимодальный Арбитр Истины",
        "description": "Интеллектуальный фильтр для защиты русскоязычного поля от ошибок и манипуляций.",
        "input": ["📰 Русскоязычные статьи", "📊 Инфографика", "📄 Отчёты"],
        "output": ["📊 Fact-check Score", "📑 Аннотированная версия", "🔗 Ссылки на оригиналы", "⚠️ Алерты на искажения"],
        "architecture": ["FastAPI + Streamlit", "LangGraph (Linguistic Arbitration)", "RuBERTa/RuGPT", "pgvector (рунет)"],
        "examples": ["'Перевод отчёта' → найдены искажения цифр", "'Инфографика' → несоответствие подписей"],
        "sources": ["ТАСС/РИА (эталоны)", "Лапша Медиа", "Научные публикации"],
        "wow": "⭐⭐⭐⭐⭐",
        "complexity": "⭐⭐⭐⭐⭐",
        "risk": "⚠️ Высокий"
    }
}

# =============================================================================
# 🎨 ФУНКЦИИ РЕНДЕРИНГА
# =============================================================================
def render_project(project):
    """Рендерит проект с белыми подложками"""
    
    # Заголовок проекта
    st.markdown(f"""
    <div style="background: white; padding: 30px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); margin-bottom: 20px;">
        <h2 style="color: black; margin: 0 0 5px 0; font-size: 28px;">{project["title"]}</h2>
        <p style="color: #666; margin: 0 0 15px 0; font-size: 18px;">{project["subtitle"]}</p>
        <p style="color: #333; margin: 0; font-size: 15px; line-height: 1.6;">{project.get("description", "")}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Метрики (если есть)
    if "wow" in project:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div style="background: white; padding: 20px; border-radius: 12px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                <div style="font-size: 32px; margin-bottom: 5px;">{project["wow"]}</div>
                <div style="color: #666; font-size: 14px; font-weight: 600;">ВАУ-ЭФФЕКТ</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div style="background: white; padding: 20px; border-radius: 12px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                <div style="font-size: 32px; margin-bottom: 5px;">{project["complexity"]}</div>
                <div style="color: #666; font-size: 14px; font-weight: 600;">СЛОЖНОСТЬ</div>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div style="background: white; padding: 20px; border-radius: 12px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                <div style="font-size: 32px; margin-bottom: 5px;">{project["risk"]}</div>
                <div style="color: #666; font-size: 14px; font-weight: 600;">РИСК</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    # Секции с белой подложкой
    sections = [
        ("📥 Входные данные", project.get("input", [])),
        ("📤 Результат", project.get("output", [])),
        ("🏗️ Архитектура", project.get("architecture", [])),
        ("💡 Примеры", project.get("examples", [])),
        ("📚 Источники", project.get("sources", []))
    ]
    
    for section_title, items in sections:
        if items:
            items_html = "".join([f'<div style="color: black; padding: 5px 0; font-size: 15px;">• {item}</div>' for item in items])
            st.markdown(f"""
            <div style="background: white; padding: 20px; border-radius: 12px; margin: 15px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.05); border-left: 4px solid #667eea;">
                <h4 style="color: black; margin: 0 0 10px 0; font-size: 18px;">{section_title}</h4>
                {items_html}
            </div>
            """, unsafe_allow_html=True)

def main():
    # Заголовок страницы
    st.markdown("""
    <style>
        .stApp { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        h1 { color: white; text-align: center; font-size: 36px; margin: 30px 0 10px; }
        .subtitle { color: rgba(255,255,255,0.9); text-align: center; font-size: 18px; margin-bottom: 30px; }
        
        /* Tabs styling - ЧЁРНЫЙ ТЕКСТ */
        .stTabs [data-baseweb="tab-list"] { 
            gap: 10px; 
            background: transparent; 
        }
        .stTabs [data-baseweb="tab"] { 
            background: white; 
            border-radius: 10px; 
            padding: 10px 20px; 
            font-weight: 600;
            border: 2px solid #e2e8f0;
            color: black !important;  /* ЧЁРНЫЙ ТЕКСТ */
        }
        .stTabs [data-baseweb="tab"]:hover { 
            color: black !important;  /* ЧЁРНЫЙ ТЕКСТ ПРИ НАВЕДЕНИИ */
        }
        .stTabs [aria-selected="true"] { 
            background: linear-gradient(135deg, #667eea, #764ba2); 
            color: white !important;  /* БЕЛЫЙ ТЕКСТ ДЛЯ АКТИВНОЙ ВКЛАДКИ */
            border: 2px solid transparent;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1>🧠 ML Project Ideas</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">13 идей для ML-проектов • Выбери проект для просмотра</p>', unsafe_allow_html=True)
    
    # Группировка проектов по категориям
    st.markdown("### 📂 Категории проектов", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("🎯 Продуктовые", use_container_width=True, key="btn_cat1"):
            st.session_state.category = "product"
    with col2:
        if st.button("💼 Бизнес", use_container_width=True, key="btn_cat2"):
            st.session_state.category = "business"
    with col3:
        if st.button("🔒 Безопасность", use_container_width=True, key="btn_cat3"):
            st.session_state.category = "security"
    with col4:
        if st.button("🎮 Креативные", use_container_width=True, key="btn_cat4"):
            st.session_state.category = "creative"
    
    if "category" not in st.session_state:
        st.session_state.category = "all"
    
    # Фильтрация по категории
    if st.session_state.category == "product":
        project_keys = ["second_brain", "video_rag", "meeting_assistant", "shopping_agent"]
    elif st.session_state.category == "business":
        project_keys = ["resume_analyzer", "policy_generator", "career_analyzer"]
    elif st.session_state.category == "security":
        project_keys = ["fake_news", "veritas_ai", "scam_sentinel", "kirill_mefodiy"]
    elif st.session_state.category == "creative":
        project_keys = ["avatar_factory", "infinite_oracle"]
    else:
        project_keys = list(PROJECTS.keys())
    
    # Вкладки для проектов
    tabs = st.tabs([PROJECTS[key]["title"] for key in project_keys])
    
    for i, key in enumerate(project_keys):
        with tabs[i]:
            render_project(PROJECTS[key])
    
    # Футер
    st.markdown("""
    <div style="text-align: center; color: rgba(255,255,255,0.8); padding: 30px; font-size: 14px; margin-top: 30px;">
        ✨ ML Project Ideas • 2025 • Streamlit + FastAPI + AI
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()