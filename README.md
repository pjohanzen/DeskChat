
# DeskChat

**DeskChat** is a simple, modern desktop chat application that lets you interact with **local AI models** using [Ollama](https://ollama.ai).
It provides a **ChatGPT-like experience** but runs **completely offline**, ensuring **privacy, speed, and zero subscription cost**.

---

## ✨ Features

* **Messenger-Style Chat UI**

  * Modern dark theme
  * Chat bubbles for user & AI messages
  * Smooth scrolling, auto-scroll to latest message

* **AI Response Animation**

  * Shows `💭 DeskChat is thinking...` with animated dots while AI processes

* **Local AI Integration**

  * Powered by [Ollama](https://ollama.ai)
  * Default model: **Mistral**
  * Supports other Ollama models (LLaMA2, CodeLlama, etc.)

* **Real-time Chat**

  * Full conversation history retained
  * Interactive and responsive

* **Cross-platform**

  * Works on **Windows, macOS, Linux**

* **Lightweight**

  * Minimal dependencies
  * Efficient even on mid-range machines

---

## 🖼️ Screenshot

*(Insert your screenshot here — showing chat bubbles for user & assistant messages)*

---

## 📦 Requirements

* **Python 3.9+**
* **PyQt6** (GUI framework)
* **Ollama** installed and running locally

---

## ⚙️ Installation & Setup

1. **Clone the repo**:

   ```bash
   git clone https://github.com/yourusername/deskchat.git
   cd deskchat
   ```

2. **Install Python dependencies**:

   ```bash
   pip install PyQt6 ollama
   ```

3. **Install Ollama**:

   * Download Ollama from [ollama.ai](https://ollama.ai).
   * After installation, pull the **Mistral** model (default):

     ```bash
     ollama pull mistral
     ```

4. *(Optional)* Pull additional models:

   ```bash
   ollama pull llama2
   ollama pull codellama
   ollama pull gemma
   ```

5. **Run the application**:

   ```bash
   python deskchat.py
   ```

---

## 💡 Usage

1. Start DeskChat with:

   ```bash
   python deskchat.py
   ```

2. Type your message at the bottom input bar.

3. Press **Enter** or click **Send**.

4. DeskChat responds with **AI messages in chat bubbles**.

5. The full conversation stays visible in the window.

---

## 🔄 Switching Models

DeskChat is model-agnostic — you can switch between supported Ollama models:

1. Open the code (`deskchat.py`).

2. Look for:

   ```python
   MODEL_NAME = "mistral"
   ```

3. Replace `"mistral"` with any installed model:

   * `"llama2"` → Meta’s LLaMA 2
   * `"codellama"` → Code-optimized LLaMA
   * `"gemma"` → Lightweight Google model
   * `"mistral"` → Default balanced model

4. Restart the app.

Example:

```python
MODEL_NAME = "llama2"
```

---

## 🎨 Customization

* **Bubble Styling**: Edit the `refresh_chat_display()` function to change chat bubble colors, fonts, or alignments.
* **Window Settings**: Adjust `window.setGeometry(500, 200, 500, 600)` for default size.
* **Themes**: Update the `setStyleSheet()` calls to customize dark/light mode.

---

## 🔧 Troubleshooting

* **Model not found**
  Run:

  ```bash
  ollama pull mistral
  ```

* **Ollama not running**
  Make sure the Ollama service is active in the background.

* **Black or Empty Window**
  Reinstall PyQt6:

  ```bash
  pip install --upgrade PyQt6
  ```

---

## 📜 License

MIT License – free for personal & commercial use.

---

## 🚀 Roadmap / Future Features

* ✅ Local chat bubbles (like Messenger/WhatsApp)
* ⏳ Multi-model dropdown to switch models inside UI
* ⏳ Export chat history to file
* ⏳ Voice input/output (speech-to-text + TTS)
* ⏳ Custom themes

---

👉 DeskChat = your **personal, private ChatGPT alternative** powered by **Ollama + local AI models**.
