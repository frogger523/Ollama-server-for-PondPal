# PondPal AI Assistant Server

This repository contains the source code for the PondPal server, an AI assistant server built using Flask and the Ollama API. The server provides two API endpoints for interacting with the AI models via chat messages.

## Features

- **/chat**: Endpoint that allows users to chat with the 'wizard-vicuna-uncensored:7b' model.
- **/free3**: Endpoint for chatting with the 'phi3' model.
- Error handling with appropriate response codes.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:
    ```bash
    cd <repository-directory>
    ```

3. Set up a virtual environment and install the required Python packages:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

4. Ensure that you have the Ollama Python client installed and properly configured:
    ```bash
    pip install ollama
    ```

5. Start the Flask server:
    ```bash
    python pondpal_server.py
    ```

The server will run in debug mode and listen on port `2187`.

## API Endpoints

### **`/chat`**

- **Method**: `POST`
- **Payload**: JSON object with the key `message`.
  ```json
  {
    "message": "<Your message to the AI>"
  }
