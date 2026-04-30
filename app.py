import json
import os
import re
import random
import hashlib
import html
from datetime import datetime

import streamlit as st

from data.questions import QUIZ, UNIT1_WORDS, UNIT2_WORDS, IDIOMS, READING_TEXT, READING_QUESTIONS

APP_TITLE = "English Adventure 7th Grade"
USERS_FILE = "storage/users.json"
PROGRESS_FILE = "storage/progress.json"

st.set_page_config(page_title=APP_TITLE, page_icon="🌍", layout="wide")

CUSTOM_CSS = """
<style>
.main .block-container {padding-top: 1.4rem; max-width: 1150px;}
.card {border: 1px solid rgba(120,120,120,.25); border-radius: 18px; padding: 18px; background: rgba(250,250,250,.04); box-shadow: 0 4px 16px rgba(0,0,0,.06);}
.small {font-size: 0.9rem; opacity: .85;}
.big-score {font-size: 2.2rem; font-weight: 800;}
.badge {display:inline-block; padding: 4px 10px; border-radius: 999px; border: 1px solid rgba(120,120,120,.35); margin: 2px; font-size: .85rem;}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

WORLD_EMOJI = {
    "Vocabulary Unit 1": "🏕️",
    "Vocabulary Unit 2": "🎭",
    "Past Simple": "⏳",
    "Past Continuous": "🎬",
    "Prepositions of Time": "🕒",
    "Adverbs": "⚡",
    "Infinitives and Gerunds": "🧩",
    "Present Continuous as Future": "📅",
    "Prepositions": "📍",
    "Adjectives Fact and Opinion": "🎨",
    "Idioms": "💬",
    "Writing Lab": "✍️",
    "Reading Challenge": "📖",
}

WORLD_OBJECTIVE = {
    "Vocabulary Unit 1": "Identify Unit 1 vocabulary in context and through definitions.",
    "Vocabulary Unit 2": "Identify and produce sentences using Unit 2 vocabulary.",
    "Past Simple": "Practice regular/irregular verbs, negatives, and questions.",
    "Past Continuous": "Use was/were + verb-ing for actions in progress in the past.",
    "Prepositions of Time": "Practice IN / ON / AT and notebook exceptions.",
    "Adverbs": "Practice adverbs of time and manner.",
    "Infinitives and Gerunds": "Choose infinitive or gerund according to the verb.",
    "Present Continuous as Future": "Use am/is/are + verb-ing for future arrangements.",
    "Prepositions": "Practice just + prepositions, preposition + -ing, and WH-questions with prepositions.",
    "Adjectives Fact and Opinion": "Classify fact and opinion adjectives.",
    "Idioms": "Practice the five idioms from the exam topics.",
    "Writing Lab": "Write sentences that follow the selected topic.",
    "Reading Challenge": "Recognize characters, place, time, problem, and solution in a reading.",
}

WRITING_TASKS = [
    {
        "title": "Unit 2 vocabulary sentence",
        "topic": "Vocabulary Unit 2",
        "instruction": "Write one complete sentence using the three words.",
        "words": ["weekend", "go shopping", "bookstore"],
        "checks": {"vocab": True, "capital_period": True},
        "hint": "Example structure: This weekend, my friends and I will...",
    },
    {
        "title": "Present Continuous as Future",
        "topic": "Present Continuous as Future",
        "instruction": "Write one future arrangement using present continuous.",
        "words": ["friends", "tomorrow"],
        "checks": {"present_cont_future": True, "vocab": True, "capital_period": True},
        "hint": "Use am/is/are + verb-ing and a future time expression.",
    },
    {
        "title": "Past Simple",
        "topic": "Past Simple",
        "instruction": "Write one past sentence using the required words.",
        "words": ["movie theater", "last weekend"],
        "checks": {"past_marker": True, "vocab": True, "capital_period": True},
        "hint": "Use a past time expression and a past verb.",
    },
    {
        "title": "Prepositions of Time",
        "topic": "Prepositions of Time",
        "instruction": "Write one sentence with the correct time preposition.",
        "words": ["Monday"],
        "checks": {"on_monday": True, "capital_period": True},
        "hint": "Days use ON: on Monday.",
    },
    {
        "title": "Idioms",
        "topic": "Idioms",
        "instruction": "Write one sentence using the idiom correctly.",
        "words": ["walking on air"],
        "checks": {"vocab": True, "capital_period": True},
        "hint": "Walking on air means very happy.",
    },
]

# -----------------------------
# Storage helpers
# -----------------------------
def ensure_files():
    os.makedirs("storage", exist_ok=True)
    for path in [USERS_FILE, PROGRESS_FILE]:
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump({}, f)


def load_json(path):
    ensure_files()
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_json(path, data):
    ensure_files()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def normalize(text: str) -> str:
    text = (text or "").strip().lower()
    text = re.sub(r"[’']", "'", text)
    text = re.sub(r"\s+", " ", text)
    return text


def clean_for_compare(text: str) -> str:
    text = normalize(text)
    text = re.sub(r"[.!?]$", "", text)
    return text


def speak_button(text, label="🔊 Listen"):
    safe_text = json.dumps(text)
    button_id = "btn_" + hashlib.md5(text.encode("utf-8")).hexdigest()[:10]
    st.components.v1.html(f"""
        <button id="{button_id}" style="padding:8px 12px;border-radius:12px;border:1px solid #999;cursor:pointer;">
            {html.escape(label)}
        </button>
        <script>
        document.getElementById('{button_id}').onclick = function() {{
            const msg = new SpeechSynthesisUtterance({safe_text});
            msg.lang = 'en-US';
            msg.rate = 0.9;
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(msg);
        }};
        </script>
    """, height=45)

# -----------------------------
# Progress
# -----------------------------
def user_progress():
    data = load_json(PROGRESS_FILE)
    user = st.session_state.get("user")
    if user not in data:
        data[user] = {"xp": 0, "worlds": {}, "attempts": [], "created_at": datetime.now().isoformat()}
        save_json(PROGRESS_FILE, data)
    return data


def record_result(world, correct, question="", detail=""):
    data = user_progress()
    user = st.session_state.user
    profile = data[user]
    profile.setdefault("xp", 0)
    profile.setdefault("worlds", {})
    profile.setdefault("attempts", [])
    w = profile["worlds"].setdefault(world, {"correct": 0, "wrong": 0})
    if correct:
        w["correct"] += 1
        profile["xp"] += 10
    else:
        w["wrong"] += 1
        profile["xp"] += 2
    profile["attempts"].append({
        "time": datetime.now().isoformat(timespec="seconds"),
        "world": world,
        "correct": bool(correct),
        "question": question[:160],
        "detail": detail[:200],
    })
    profile["attempts"] = profile["attempts"][-250:]
    save_json(PROGRESS_FILE, data)


def get_stats(world=None):
    data = user_progress()
    profile = data[st.session_state.user]
    if world:
        return profile.get("worlds", {}).get(world, {"correct":0, "wrong":0})
    return profile

# -----------------------------
# Auth
# -----------------------------
def auth_screen():
    st.title("🌍 English Adventure 7th Grade")
    st.caption("Practice app independiente para inglés: vocabulario, gramática, writing, idioms y reading.")
    left, right = st.columns([1, 1])
    with left:
        st.markdown("### 🔐 Login")
        user_login = st.text_input("Username", key="login_user")
        pass_login = st.text_input("Password", type="password", key="login_pass")
        if st.button("Enter", use_container_width=True):
            users = load_json(USERS_FILE)
            if user_login in users and users[user_login]["password"] == hash_password(pass_login):
                st.session_state.user = user_login
                st.success("Welcome!")
                st.rerun()
            else:
                st.error("Invalid username or password.")
    with right:
        st.markdown("### 🆕 Create user")
        new_user = st.text_input("New username")
        new_pass = st.text_input("New password", type="password")
        if st.button("Create account", use_container_width=True):
            users = load_json(USERS_FILE)
            if not new_user or not new_pass:
                st.warning("Write username and password.")
            elif new_user in users:
                st.error("That user already exists.")
            else:
                users[new_user] = {"password": hash_password(new_pass), "created_at": datetime.now().isoformat()}
                save_json(USERS_FILE, users)
                st.success("User created. Now log in.")

# -----------------------------
# Quiz engine
# -----------------------------
def check_answer(q, response):
    n_resp = clean_for_compare(str(response))
    answers = [q.get("answer", "")] + q.get("alt", [])
    answers = [clean_for_compare(str(a)) for a in answers]
    if q["type"] in ["fill", "transform"]:
        return n_resp in answers or any(a and a in n_resp for a in answers if len(a) > 8)
    return n_resp in answers


def render_question(world, q, idx):
    st.markdown(f"#### Question {idx + 1}")
    st.write(q["q"])
    speak_button(q["q"], "🔊 Listen to question")
    key = f"{world}_{idx}_{hashlib.md5(q['q'].encode()).hexdigest()[:6]}"

    if q["type"] in ["mcq", "match", "classify", "tf"]:
        response = st.radio("Choose one:", q["options"], key=key, index=None)
    else:
        response = st.text_input("Your answer:", key=key)

    if st.button("Check answer", key=f"check_{key}"):
        if response is None or str(response).strip() == "":
            st.warning("Write or choose an answer first.")
            return
        correct = check_answer(q, response)
        record_result(world, correct, q["q"], str(response))
        if correct:
            st.success("✅ Correct!")
        else:
            ans = q.get("answer")
            st.error(f"❌ Not yet. Correct answer: {ans}")
        st.info(q.get("explain", "Keep practicing."))


def quiz_world(world):
    st.header(f"{WORLD_EMOJI.get(world, '🌍')} {world}")
    st.caption(WORLD_OBJECTIVE.get(world, "Practice."))
    questions = QUIZ[world]
    mode = st.radio("Practice mode", ["One by one", "Random question", "All questions"], horizontal=True)

    if mode == "Random question":
        if st.button("🎲 New random question") or "random_q" not in st.session_state:
            st.session_state.random_q = random.randrange(len(questions))
        idx = st.session_state.random_q % len(questions)
        render_question(world, questions[idx], idx)
    elif mode == "All questions":
        for idx, q in enumerate(questions):
            with st.expander(f"Question {idx + 1}: {q['q'][:70]}", expanded=(idx == 0)):
                render_question(world, q, idx)
    else:
        idx = st.number_input("Question number", min_value=1, max_value=len(questions), value=1) - 1
        render_question(world, questions[idx], idx)

# -----------------------------
# Writing Lab
# -----------------------------
def validate_writing(text, task):
    feedback = []
    ok = True
    raw = text or ""
    low = normalize(raw)

    if len(raw.strip().split()) < 5:
        ok = False
        feedback.append("Write a complete sentence with at least 5 words.")

    if task["checks"].get("capital_period"):
        if raw.strip() and not raw.strip()[0].isupper():
            ok = False
            feedback.append("Start with a capital letter.")
        if raw.strip() and raw.strip()[-1] not in ".!?":
            ok = False
            feedback.append("Finish with a period, question mark, or exclamation mark.")

    if task["checks"].get("vocab"):
        missing = [w for w in task["words"] if normalize(w) not in low]
        if missing:
            ok = False
            feedback.append("Missing required word(s): " + ", ".join(missing))

    if task["checks"].get("present_cont_future"):
        has_be = re.search(r"\b(am|is|are)\b", low)
        has_ing = re.search(r"\b\w+ing\b", low)
        has_future = any(x in low for x in ["tomorrow", "next week", "tonight", "this afternoon", "on friday", "this weekend"])
        if not (has_be and has_ing and has_future):
            ok = False
            feedback.append("Use present continuous as future: am/is/are + verb-ing + future time expression.")

    if task["checks"].get("past_marker"):
        if not any(x in low for x in ["yesterday", "last", "ago"]):
            ok = False
            feedback.append("Use a past time expression such as yesterday, last weekend, or ago.")

    if task["checks"].get("on_monday"):
        if "on monday" not in low:
            ok = False
            feedback.append("Days use ON: write 'on Monday'.")
        if "in monday" in low or "at monday" in low:
            ok = False
            feedback.append("Do not use IN or AT with Monday. Use ON.")

    if ok:
        feedback.append("Good sentence. It follows the topic and uses the required language.")
    return ok, feedback


def writing_lab():
    st.header("✍️ Writing Lab")
    st.caption("The writing checker validates vocabulary, topic, basic structure, capitalization, and final punctuation.")
    task_title = st.selectbox("Choose a writing task", [t["title"] for t in WRITING_TASKS])
    task = next(t for t in WRITING_TASKS if t["title"] == task_title)
    st.markdown(f"**Topic:** {task['topic']}")
    st.write(task["instruction"])
    st.markdown("Required word(s): " + " ".join([f"<span class='badge'>{html.escape(w)}</span>" for w in task["words"]]), unsafe_allow_html=True)
    with st.expander("Hint"):
        st.info(task["hint"])
    text = st.text_area("Your sentence", height=120)
    speak_button("Write one complete sentence. " + task["instruction"], "🔊 Listen to instruction")
    if st.button("Check writing", type="primary"):
        ok, feedback = validate_writing(text, task)
        record_result("Writing Lab", ok, task["title"], text)
        if ok:
            st.success("✅ Good work!")
        else:
            st.error("❌ Needs revision.")
        for f in feedback:
            st.write("- " + f)

# -----------------------------
# Reading
# -----------------------------
def reading_challenge():
    st.header("📖 Reading Challenge")
    st.caption("Practice reading comprehension: characters, setting time, setting place, problem and solution.")
    with st.expander("Read the text", expanded=True):
        st.write(READING_TEXT)
        speak_button(READING_TEXT, "🔊 Listen to text")

    st.subheader("Comprehension questions")
    for idx, q in enumerate(READING_QUESTIONS):
        with st.expander(f"Question {idx + 1}: {q['q']}", expanded=(idx == 0)):
            render_question("Reading Challenge", q, idx)

    st.subheader("Story elements")
    col1, col2 = st.columns(2)
    with col1:
        characters = st.text_input("Characters")
        time = st.text_input("Setting time")
        place = st.text_input("Setting place")
    with col2:
        problem = st.text_input("Problem")
        solution = st.text_input("Solution")
    if st.button("Check story elements"):
        score = 0
        notes = []
        if any(x in normalize(characters) for x in ["friends", "writer", "parents"]):
            score += 1
            notes.append("✅ Characters: good.")
        else:
            notes.append("Try including the writer, friends, and/or parents.")
        if "weekend" in normalize(time):
            score += 1
            notes.append("✅ Time: last weekend.")
        else:
            notes.append("The time is last weekend.")
        if any(x in normalize(place) for x in ["city", "bookstore", "exhibition", "concert", "movie theater"]):
            score += 1
            notes.append("✅ Place: good.")
        else:
            notes.append("Places include city, bookstore, exhibition, concert, and movie theater.")
        if normalize(problem):
            score += 1
            notes.append("✅ Problem written. In this practice, the problem can be simple: they wanted to find out more information and plan their day.")
        else:
            notes.append("Write a simple problem from the text.")
        if normalize(solution):
            score += 1
            notes.append("✅ Solution written. They looked for information and did the activities.")
        else:
            notes.append("Write how the problem was solved.")
        ok = score >= 4
        record_result("Reading Challenge", ok, "story elements", f"score {score}/5")
        st.progress(score / 5)
        st.write(f"Score: {score}/5")
        for n in notes:
            st.write("- " + n)

# -----------------------------
# Idiom cards / audio vocab
# -----------------------------
def study_cards():
    st.header("📚 Study Cards")
    tab1, tab2, tab3 = st.tabs(["Unit 1", "Unit 2", "Idioms"])
    with tab1:
        st.write("Vocabulary Unit 1")
        cols = st.columns(3)
        for i, w in enumerate(UNIT1_WORDS):
            with cols[i % 3]:
                st.markdown(f"<span class='badge'>{html.escape(w)}</span>", unsafe_allow_html=True)
                speak_button(w, "🔊")
    with tab2:
        st.write("Vocabulary Unit 2")
        cols = st.columns(3)
        for i, w in enumerate(UNIT2_WORDS):
            with cols[i % 3]:
                st.markdown(f"<span class='badge'>{html.escape(w)}</span>", unsafe_allow_html=True)
                speak_button(w, "🔊")
    with tab3:
        st.info("Tip Pro: Walking on air = happiness. Up in the air = uncertainty. Same word 'air', different feeling.")
        for idiom, data in IDIOMS.items():
            with st.expander(idiom):
                st.write("**Meaning:** " + data["meaning"])
                st.write("**Spanish:** " + data["spanish"])
                st.write("**Example:** " + data["example"])
                speak_button(idiom + ". " + data["example"], "🔊 Listen")

# -----------------------------
# Dashboard
# -----------------------------
def dashboard():
    st.header("📊 Progress Dashboard")
    profile = get_stats()
    xp = profile.get("xp", 0)
    worlds = profile.get("worlds", {})
    c1, c2, c3 = st.columns(3)
    total_correct = sum(v.get("correct", 0) for v in worlds.values())
    total_wrong = sum(v.get("wrong", 0) for v in worlds.values())
    with c1:
        st.metric("XP", xp)
    with c2:
        st.metric("Correct", total_correct)
    with c3:
        st.metric("Needs practice", total_wrong)

    st.subheader("By world")
    rows = []
    for w in list(QUIZ.keys()) + ["Writing Lab", "Reading Challenge"]:
        stats = worlds.get(w, {"correct":0, "wrong":0})
        attempts = stats.get("correct",0) + stats.get("wrong",0)
        pct = round((stats.get("correct",0) / attempts) * 100, 1) if attempts else 0
        rows.append({"World": w, "Correct": stats.get("correct",0), "Wrong": stats.get("wrong",0), "Accuracy %": pct})
    st.dataframe(rows, use_container_width=True, hide_index=True)

    attempts = profile.get("attempts", [])[-15:]
    if attempts:
        st.subheader("Recent attempts")
        st.dataframe(list(reversed(attempts)), use_container_width=True, hide_index=True)

# -----------------------------
# Main app
# -----------------------------
def home():
    st.title("🌍 English Adventure 7th Grade")
    st.markdown("Hybrid practice app: game-style worlds + tutor-style feedback.")
    st.markdown("""
    <div class='card'>
    <b>Includes:</b> login, user progress, XP, all worlds, writing validation, reading comprehension, idioms, and audio buttons in English.
    </div>
    """, unsafe_allow_html=True)
    st.subheader("Worlds")
    cols = st.columns(3)
    worlds = list(QUIZ.keys()) + ["Writing Lab", "Reading Challenge"]
    for i, w in enumerate(worlds):
        with cols[i % 3]:
            stats = get_stats(w)
            attempts = stats.get("correct",0) + stats.get("wrong",0)
            st.markdown(f"### {WORLD_EMOJI.get(w, '🌍')} {w}")
            st.caption(WORLD_OBJECTIVE.get(w, "Practice."))
            st.write(f"Attempts: {attempts} | ✅ {stats.get('correct',0)} | ❌ {stats.get('wrong',0)}")


def app_shell():
    with st.sidebar:
        st.markdown(f"### 👤 {st.session_state.user}")
        profile = get_stats()
        st.metric("XP", profile.get("xp", 0))
        page = st.radio("Menu", ["Home", "Study Cards", "Dashboard"] + list(QUIZ.keys()) + ["Writing Lab", "Reading Challenge"])
        if st.button("Logout", use_container_width=True):
            st.session_state.pop("user", None)
            st.rerun()

    if page == "Home":
        home()
    elif page == "Study Cards":
        study_cards()
    elif page == "Dashboard":
        dashboard()
    elif page == "Writing Lab":
        writing_lab()
    elif page == "Reading Challenge":
        reading_challenge()
    else:
        quiz_world(page)

ensure_files()
if "user" not in st.session_state:
    auth_screen()
else:
    app_shell()
