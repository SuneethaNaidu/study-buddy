import streamlit as st
import os
import time
from groq import Groq
from fpdf import FPDF

# ── Groq client ──────────────────────────────────────────────────────────────
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="AI Study Buddy", page_icon="📚", layout="wide")
st.title("📚 AI Study Buddy")
st.write("Your smart assistant for notes, Q&A, flashcards, quizzes & audio transcription!")

# ── Sidebar menu ──────────────────────────────────────────────────────────────
menu = st.sidebar.radio("Choose a feature:", [
    "Ask a Question",
    "Summarize Notes",
    "Generate Flashcards",
    "Quiz Me",
    "Transcribe Audio",
])

# ── Helpers ───────────────────────────────────────────────────────────────────

def ask_groq(prompt: str, model: str = "llama-3.3-70b-versatile") -> str:
    """Send a prompt to Groq and return the text response with retry logic."""
    retries = 3
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1024,
            )
            return response.choices[0].message.content
        except Exception as e:
            error_message = str(e).lower()
            if "rate_limit" in error_message or "429" in error_message:
                wait_time = (attempt + 1) * 5
                st.warning(f"⚠️ Rate limit hit. Retrying in {wait_time} seconds…")
                time.sleep(wait_time)
            else:
                return f"⚠️ Error: {e}"
    return "🤖 (Demo Mode) This is a sample AI-generated response."


def save_pdf(text: str, filename: str = "study_notes.pdf") -> str:
    """Export plain text to a PDF file and return the path."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    # encode to latin-1 to avoid FPDF unicode issues
    safe_text = text.encode("latin-1", errors="replace").decode("latin-1")
    pdf.multi_cell(0, 10, safe_text)
    pdf.output(filename)
    return filename


def download_pdf_button(text: str, filename: str, label: str = "💾 Save as PDF"):
    """Render a Streamlit download button that generates a PDF on-the-fly."""
    if st.button(label, key=f"pdf_{filename}"):
        path = save_pdf(text, filename)
        with open(path, "rb") as f:
            st.download_button(
                "⬇️ Download PDF",
                f,
                file_name=filename,
                key=f"dl_{filename}",
            )


# ── Feature pages ─────────────────────────────────────────────────────────────

# 1. Ask a Question
if menu == "Ask a Question":
    question = st.text_input("Enter your question:")
    if st.button("Get Answer") and question:
        with st.spinner("Thinking…"):
            answer = ask_groq(f"Answer this question clearly:\n\n{question}")
        st.success(answer)
        download_pdf_button(answer, "answer.pdf")

# 2. Summarize Notes
elif menu == "Summarize Notes":
    notes = st.text_area("Paste your notes:", height=250)
    if st.button("Summarize") and notes:
        with st.spinner("Summarizing…"):
            summary = ask_groq(f"Summarize these study notes concisely:\n\n{notes}")
        st.info(summary)
        download_pdf_button(summary, "summary.pdf")

# 3. Generate Flashcards
elif menu == "Generate Flashcards":
    content = st.text_area("Enter topic or notes:", height=200)
    num = st.slider("Number of flashcards", 3, 15, 5)
    if st.button("Create Flashcards") and content:
        with st.spinner("Generating flashcards…"):
            flashcards = ask_groq(
                f"Create {num} study flashcards in Q&A format for:\n\n{content}"
            )
        st.write(flashcards)
        download_pdf_button(flashcards, "flashcards.pdf")

# 4. Quiz Me
elif menu == "Quiz Me":
    topic = st.text_input("Enter topic for quiz:")
    num_q = st.slider("Number of questions", 3, 10, 5)
    if st.button("Start Quiz") and topic:
        with st.spinner("Preparing quiz…"):
            quiz = ask_groq(
                f"Create a {num_q}-question multiple-choice quiz with answers on:\n\n{topic}"
            )
        st.write(quiz)
        download_pdf_button(quiz, "quiz.pdf")

# 5. Transcribe Audio
elif menu == "Transcribe Audio":
    uploaded_file = st.file_uploader(
        "Upload audio file (mp3, wav, m4a, ogg, flac)",
        type=["mp3", "wav", "m4a", "ogg", "flac"],
    )
    if uploaded_file is not None:
        if st.button("Transcribe"):
            with st.spinner("Transcribing with Whisper…"):
                # Groq expects a file-like object with a .name attribute
                transcript = client.audio.transcriptions.create(
                    model="whisper-large-v3",
                    file=(uploaded_file.name, uploaded_file.read()),
                    response_format="text",
                )
            # Groq returns plain text when response_format="text"
            text = transcript if isinstance(transcript, str) else transcript.text
            st.success(text)
            download_pdf_button(text, "transcript.pdf")
