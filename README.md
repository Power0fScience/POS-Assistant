# P.O.S. - Gemini AI Assistant

A Python-based terminal AI assistant built around two years ago using Google's Gemini API.

The project was an early experiment with generative AI, API integration, conversational interfaces, and basic system interaction.

## Features

- Conversational interaction with Google's Gemini API
- Maintains conversation history during the current session
- Terminal-based colored output
- Internet connectivity checking
- Basic command handling
- PC shutdown command
- Error handling
- Simple terminal interface

## How It Works

The application starts by checking whether an internet connection is available.

It then initializes a Gemini model and starts an interactive terminal session.

User messages are sent to Gemini and the generated responses are displayed directly in the terminal.

The application also recognizes several predefined commands, including:

- `exit`
- `quit`
- `let's stop`
- `lets stop`
- `shut down`
- `turn off the pc`
- `what's your name`
- `what can i call you`

## Requirements

- Python 3
- Google Gemini API access
- Internet connection

Python dependencies:

```bash
pip install google-generativeai requests
```

## Configuration

The application requires a Google Gemini API key.

The original version of this project used a hardcoded API key. This has been removed from the public version for security reasons.

Set your API key as an environment variable instead:

### Linux

```bash
export GEMINI_API_KEY="your_api_key_here"
```

### Windows

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

Then configure the application to read the variable:

```python
import os

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not set")

genai.configure(api_key=api_key)
```

Never commit API keys, tokens, or other credentials to the repository.

## Running the Project

Run the Python script:

```bash
python script.py
```

The assistant will start an interactive terminal session.

Type a message to communicate with Gemini.

Use:

```text
exit
```

to close the application.

## GUI Version

A separate version of this project was later developed with a Tkinter graphical interface.

The original application functionality remained the same, while the interface was changed from a terminal-based interaction to a graphical one.

AI assistance was used during the development of the Tkinter interface.

## Project Background

This project was originally developed around two years ago as an experiment with Google's generative AI APIs.

Looking back at the original implementation, there are several areas that could be improved, including:

- API credential management
- Code organization
- Configuration handling
- Modern Gemini API usage
- More robust command handling
- Improved error handling
- Separation of application logic from the user interface

The project is preserved as an example of an earlier stage of development and experimentation with generative AI.

## Technologies

- Python
- Google Gemini API
- Requests
- Socket programming
- Terminal ANSI escape sequences
- Tkinter (GUI version)

## Disclaimer

This project is provided for educational and archival purposes.

The project interacts with external APIs and system-level commands. Review the code and understand its behavior before running it.

## Project Background

Originally developed in 2024 as an early experiment with Google's Gemini API.

The project was later recovered from my personal archive and published to GitHub in 2026.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
