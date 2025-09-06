# DeskChat

A simple, lightweight desktop chat application with a clean GUI for interacting with local AI models via [Ollama](https://ollama.ai).

## Features

- **Clean, Modern UI**: Sleek dark theme with an intuitive chat interface.
- **Local AI Integration**: Powered by Ollama, using the Llama2 model by default.
- **Real-time Chat**: Interactive conversations with message history.
- **Cross-platform**: Built with PyQt6, supporting Windows, macOS, and Linux.
- **Lightweight**: Minimal dependencies for fast startup and low resource usage.

## Screenshot

The application offers a modern, dark-themed interface featuring:

- A chat display area with color-coded messages (user and AI).
- A text input field with placeholder text for easy message entry.
- Support for both "Send" button and Enter key for sending messages.
- A responsive layout that adjusts seamlessly to window resizing.

## Requirements

- Python 3.7 or higher
- PyQt6
- Ollama (with the Llama2 model installed)

## Installation

1. **Install Python dependencies**:
   ```bash
   pip install PyQt6 ollama
   ```

2. **Install and set up Ollama**:
   - Download and install Ollama from [ollama.ai](https://ollama.ai).
   - Pull the Llama2 model:
     ```bash
     ollama pull llama2
     ```

3. **Run the application**:
   ```bash
   python chat_assistant.py
   ```

## Usage

1. Launch the application using the command above.
2. Type your message in the text input field at the bottom.
3. Press the "Send" button or hit Enter to interact with the AI.
4. View the conversation history in the main chat area, with AI responses highlighted in a blue background for clarity.

## Customization

The application is highly customizable:

- **Change AI Model**: Update the `model="llama2"` parameter in the `chat_with_ai()` function to use a different Ollama-compatible model.
- **Adjust Styling**: Modify the `setStyleSheet()` calls to customize colors, fonts, or other UI elements.
- **Window Settings**: Adjust the `setGeometry()` function to change the default window size and position.

## Technical Details

- **GUI Framework**: PyQt6 for a robust, cross-platform desktop interface.
- **AI Backend**: Ollama API for efficient local model inference.
- **Architecture**: Event-driven design with separate logic for message handling and display.
- **Error Handling**: Graceful handling of connection issues with user-friendly error messages.

## Troubleshooting

- **"Connection Error"**: Ensure the Ollama server is running (`ollama serve`).
- **"Model not found"**: Verify the Llama2 model is installed (`ollama pull llama2`).
- **UI not displaying**: Confirm PyQt6 is installed correctly (`pip install PyQt6`).

## License

This project is open source and licensed under the MIT License. Feel free to modify and distribute as needed.

## Contributing

Contributions are welcome! To contribute, please fork the repository and submit a pull request. Some ideas for enhancements include:

- Support for multiple AI models.
- Message export and import functionality.
- Customizable themes and UI styles.
- Voice input/output integration.
- Message search and filtering capabilities.

For bug reports or feature requests, please open an issue on the GitHub repository.
