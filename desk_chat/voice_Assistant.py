import sys
import ollama
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QTextEdit, QScrollArea
)
from PyQt6.QtCore import Qt


# ------------------ FUNCTIONS ------------------
def chat_with_ai():
    user_message = input_box.text().strip()
    if not user_message:
        return

    # Show user message
    append_message("You", user_message, "user")
    input_box.clear()

    try:
        # Send to Ollama
        response = ollama.chat(model="llama2", messages=chat_history)
        assistant_reply = response["message"]["content"]

        # Add assistant reply to chat
        append_message("Assistant", assistant_reply, "assistant")

    except Exception as e:
        append_message("System", f"Error: {str(e)}", "error")


def append_message(sender, message, role):
    """Append formatted message to chat window + history"""
    if role == "user":
        formatted = f"<p style='color:#00aaff;'><b>{sender}:</b> {message}</p>"
        chat_history.append({"role": "user", "content": message})
    elif role == "assistant":
        formatted = f"<p style='color:#ffffff; background:#0078d7; padding:6px; border-radius:8px;'><b>{sender}:</b> {message}</p>"
        chat_history.append({"role": "assistant", "content": message})
    else:  # errors/system
        formatted = f"<p style='color:#ff4444;'><b>{sender}:</b> {message}</p>"

    chat_display.append(formatted)


# ------------------ GUI ------------------
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("💬 Local Chat Assistant")
window.setGeometry(500, 200, 500, 600)

layout = QVBoxLayout()

chat_display = QTextEdit()
chat_display.setReadOnly(True)
chat_display.setStyleSheet(
    "background-color: #1e1e1e; color: #f0f0f0; font-size:14px; padding:10px; border-radius:8px;")

input_layout = QHBoxLayout()
input_box = QLineEdit()
input_box.setPlaceholderText("Type your message...")
input_box.setStyleSheet("padding:8px; font-size:14px; border-radius:6px;")
send_button = QPushButton("Send")
send_button.setStyleSheet("background-color:#0078d7; color:white; padding:8px; border-radius:6px;")

input_layout.addWidget(input_box)
input_layout.addWidget(send_button)

layout.addWidget(chat_display)
layout.addLayout(input_layout)

window.setLayout(layout)

# ------------------ EVENTS ------------------
chat_history = []
send_button.clicked.connect(chat_with_ai)
input_box.returnPressed.connect(chat_with_ai)  # press Enter to send

window.show()
sys.exit(app.exec())
