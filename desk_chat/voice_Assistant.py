import sys
import ollama
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QLabel, QScrollArea, QFrame
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QTimer


# ------------------ CONFIG ------------------
MODEL_NAME = "mistral"  # ✅ using Mistral


# ------------------ Worker Thread ------------------
class ChatWorker(QThread):
    finished = pyqtSignal(str)   # Signal for assistant reply
    error = pyqtSignal(str)      # Signal for errors

    def __init__(self, messages):
        super().__init__()
        self.messages = messages

    def run(self):
        try:
            response = ollama.chat(model=MODEL_NAME, messages=self.messages)
            reply = response["message"]["content"]
            self.finished.emit(reply)
        except Exception as e:
            self.error.emit(str(e))


# ------------------ FUNCTIONS ------------------
def chat_with_ai():
    user_message = input_box.text().strip()
    if not user_message:
        return

    # Add user msg to history
    chat_history.append({"role": "user", "content": user_message})
    add_message_bubble("You", user_message, "user")

    input_box.clear()

    # Add "thinking..." placeholder
    chat_history.append({"role": "thinking", "content": "💭 DeskChat is thinking"})
    add_message_bubble("DeskChat", "💭 DeskChat is thinking", "thinking")

    # Start animation
    global thinking_timer
    thinking_timer = QTimer()
    thinking_timer.timeout.connect(update_thinking_animation)
    thinking_timer.start(500)

    # Start worker thread
    global worker
    worker = ChatWorker(chat_history[:-1])  # exclude "thinking"
    worker.finished.connect(handle_reply)
    worker.error.connect(handle_error)
    worker.start()


def handle_reply(reply):
    stop_thinking_animation()
    chat_history.append({"role": "assistant", "content": reply})
    add_message_bubble("DeskChat", reply, "assistant")


def handle_error(err_msg):
    stop_thinking_animation()
    chat_history.append({"role": "system", "content": f"Error: {err_msg}"})
    add_message_bubble("System", f"Error: {err_msg}", "system")


def add_message_bubble(sender, message, role):
    """Create proper messenger-style chat bubbles"""
    # Container for alignment (left/right)
    container = QFrame()
    layout = QHBoxLayout(container)

    bubble = QLabel(message)
    bubble.setWordWrap(True)
    bubble.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)  # ❌ disables highlight
    bubble.setMaximumWidth(350)  # ✅ ensures long messages wrap nicely

    if role == "user":
        bubble.setStyleSheet("""
            background-color: #0078d7;
            color: white;
            padding: 10px;
            border-radius: 15px;
            font-size: 14px;
        """)
        layout.addStretch()
        layout.addWidget(bubble)
    elif role == "assistant":
        bubble.setStyleSheet("""
            background-color: #3a3a3a;
            color: white;
            padding: 10px;
            border-radius: 15px;
            font-size: 14px;
        """)
        layout.addWidget(bubble)
        layout.addStretch()
    elif role == "thinking":
        bubble.setStyleSheet("""
            color: #aaaaaa;
            font-style: italic;
            padding: 6px;
        """)
        layout.addWidget(bubble)
        layout.addStretch()
    else:  # system / error
        bubble.setStyleSheet("""
            color: #ff4444;
            padding: 6px;
        """)
        layout.addWidget(bubble)
        layout.addStretch()

    container_layout.insertWidget(container_layout.count() - 1, container)
    scroll_area.verticalScrollBar().setValue(scroll_area.verticalScrollBar().maximum())


def update_thinking_animation():
    """Animate dots for thinking message"""
    for msg in chat_history:
        if msg["role"] == "thinking":
            if msg["content"].endswith("..."):
                msg["content"] = "💭 DeskChat is thinking"
            else:
                msg["content"] += "."
    refresh_bubbles()


def stop_thinking_animation():
    """Stop animation and remove 'thinking...' from history"""
    global thinking_timer
    if thinking_timer:
        thinking_timer.stop()
    global chat_history
    chat_history = [msg for msg in chat_history if msg["role"] != "thinking"]
    refresh_bubbles()


def refresh_bubbles():
    """Re-render chat bubbles from chat history"""
    for i in reversed(range(container_layout.count() - 1)):  # keep last spacer
        widget = container_layout.itemAt(i).widget()
        if widget:
            widget.deleteLater()

    for msg in chat_history:
        add_message_bubble("DeskChat" if msg["role"] == "assistant" else "You", msg["content"], msg["role"])


# ------------------ GUI ------------------
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("💬 DeskChat (Mistral)")
window.setGeometry(500, 200, 500, 600)

layout = QVBoxLayout(window)

# Scroll area
scroll_area = QScrollArea()
scroll_area.setWidgetResizable(True)
scroll_area.setStyleSheet("background-color: #1e1e1e; border:none;")

scroll_widget = QWidget()
container_layout = QVBoxLayout(scroll_widget)
container_layout.addStretch(1)

scroll_area.setWidget(scroll_widget)
layout.addWidget(scroll_area)

# Input area
input_layout = QHBoxLayout()
input_box = QLineEdit()
input_box.setPlaceholderText("Type your message...")
input_box.setStyleSheet("""
    padding:10px;
    font-size:14px;
    border-radius:12px;
    border:1px solid #555;
    background:#2d2d30;
    color:#f0f0f0;
""")
send_button = QPushButton("Send")
send_button.setStyleSheet("""
    background-color:#0078d7;
    color:white;
    padding:10px 16px;
    border-radius:12px;
    font-weight:bold;
""")

input_layout.addWidget(input_box)
input_layout.addWidget(send_button)
layout.addLayout(input_layout)

window.setLayout(layout)

# ------------------ EVENTS ------------------
chat_history = []
thinking_timer = None

send_button.clicked.connect(chat_with_ai)
input_box.returnPressed.connect(chat_with_ai)

window.show()
sys.exit(app.exec())
