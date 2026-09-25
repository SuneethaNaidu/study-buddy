📚 Study Buddy App
An AI-powered study assistant designed to make learning faster, smarter, and more interactive.

Study Buddy is an AI-powered learning companion built with Streamlit and OpenAI APIs. It helps students understand concepts, summarize notes, create flashcards and quizzes, and transcribe audio — all from a single platform.

✨ Features
Feature	Description
💬 Ask a Question	Get clear and instant answers to academic questions.
📝 Summarize Notes	Convert lengthy notes into concise summaries.
🃏 Generate Flashcards	Automatically create revision-friendly flashcards.
🧠 Quiz Generator	Generate quizzes from study material for practice.
🎙️ Audio Transcription	Convert uploaded audio recordings into text.
🚀 How It Works
                    📚 STUDY BUDDY
                          │
          ┌───────────────┼───────────────┐
          ↓               ↓               ↓
     💬 Q&A          📝 Summarize     🃏 Flashcards
          │               │               │
          └───────────────┼───────────────┘
                          ↓
                   🧠 Quiz Generator
                          │
                          ↓
                   🎙️ Transcription
Simply choose a feature, provide your study material, and let AI do the rest.

🛠️ Tech Stack
💻 Frontend / UI
Streamlit
🐍 Backend
Python
🤖 AI Models
OpenAI GPT

GPT-4o
GPT-4o-mini
🎙️ Transcription
OpenAI Whisper API
☁️ Deployment
Streamlit Cloud
Render
📖 Usage
💬 Ask a Question
Enter an academic question and receive a clear, AI-generated explanation instantly.

📝 Summarize Notes
Paste or upload your study notes and generate a concise summary containing the most important points.

🃏 Generate Flashcards
Convert your notes into question-and-answer flashcards for quick and effective revision.

🧠 Generate a Quiz
Turn your study material into an AI-generated quiz and test your understanding.

🎙️ Transcribe Audio
Upload an audio recording and convert speech into editable text using AI-powered transcription.

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/sathwiksandesh/Study-Buddy-App.git
cd Study-Buddy-App
2️⃣ Create a Virtual Environment
python -m venv venv
Activate the virtual environment.

Windows:

venv\Scripts\activate
macOS / Linux:

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure the API Key
Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key
⚠️ Important: Never commit your API key or .env file to GitHub.

Add .env to your .gitignore:

.env
venv/
__pycache__/
5️⃣ Run the Application
streamlit run app.py
The application will open in your browser.

📂 Project Structure
Study-Buddy/
│
├── 📄 app.py
├── 📄 requirements.txt
├── 📄 README.md
├── 📄 .gitignore
├── 🔐 .env
🧠 AI Capabilities
Study Buddy uses AI to simplify common study tasks:

                  📚 Study Material
                         │
                         ↓
                ┌─────────────────┐
                │  Study Buddy 🤖 │
                └─────────────────┘
                         │
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
   💬 Q&A          📝 Summarization   🃏 Flashcards
        │                │                │
        └────────────────┼────────────────┘
                         ↓
                  🧠 Quiz Generator
                         │
                         ↓
                  🎙️ Transcription
                         │
                         ↓
                  📈 Better Learning
🌟 Why Study Buddy?
Students often need multiple tools for studying, revision, testing, and converting learning materials into different formats.

Study Buddy brings these AI-powered capabilities together into one simple platform.

🔄 Learn → Summarize → Revise → Practice → Improve
📚 Learn concepts through AI-powered Q&A ↓ 📝 Summarize lengthy study material ↓ 🃏 Revise using generated flashcards ↓ 🧠 Practice with AI-generated quizzes ↓ 📈 Improve your understanding

🗺️ Roadmap
 🌍 Add multi-language support
 🔎 Implement semantic search with embeddings
 🎯 Add customizable quiz difficulty levels
 🔐 Add user authentication
 📊 Add study progress tracking
 💾 Add persistent notes and flashcard storage
 📈 Add personalized learning analytics
 🗂️ Add study history
 📱 Improve mobile responsiveness
🚀 Future Improvements
Personalized Learning — Generate content based on the student's learning level.
Smart Recommendations — Recommend topics that need more revision.
Progress Dashboard — Track quizzes, flashcards, and study activity.
Semantic Search — Search uploaded notes using embeddings.
Multi-language Learning — Support students studying in different languages.
Voice-based Interaction — Enable voice questions and responses.
🤝 Contributing
Contributions are welcome and appreciated!

How to contribute
Fork the repository.
Create a new branch.
git checkout -b feature/new-feature
Make your changes.
Commit your changes.
git commit -m "Add new feature"
Push your changes.
git push origin feature/new-feature
Open a Pull Request.
🐛 Issues & Feature Requests
If you find a bug or have an idea for a new feature, feel free to open an issue.

You can also submit feature requests to help improve Study Buddy.

🔐 Security
Never expose your API keys in source code.

Use environment variables:

OPENAI_API_KEY=your_api_key
Make sure .env is included in .gitignore:

.env
📜 License
This project is licensed under the MIT License.

👨‍💻 Author
Siddhantam Sathwik Sandesh
🎓 Artificial Intelligence & Data Science Student

💡 Interested in Artificial Intelligence, Data Science, Machine Learning, and Generative AI.

⭐ Support
If you found this project useful, consider giving the repository a ⭐ Star!

Your support helps improve and expand the project. 🚀

📚 Study Buddy
Learn Smarter. Revise Faster. Practice Better.

Built with ❤️ using Python • Streamlit • OpenAI
