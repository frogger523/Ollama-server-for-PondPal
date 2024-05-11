from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)


@app.route('/chat', methods=['POST'])
def chat_with_ai():
    # Parse the user message from the incoming request
    user_message = request.json.get('message', '')

    # Ensure the user message is not empty
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        # Call the Ollama chat API with the user messagedrop

        response = ollama.chat(model='wizard-vicuna-uncensored:7b', messages=[
            {
                'role': 'user',
                'content': user_message,
            },
        ])

        # Extract the AI response
        ai_response = response['message']['content']

        # Return the AI response in JSON format
        return jsonify({'response': ai_response})

    except Exception as e:
        # Handle potential errors
        return jsonify({'error': str(e)}), 500


@app.route('/free3', methods=['POST'])
def free3():
    # Parse the user message from the incoming request
    user_message = request.json.get('message', '')

    # Ensure the user message is not empty
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        # Call the Ollama chat API with the user messagedrop

        response = ollama.chat(model='phi3', messages=[
            {
                'role': 'user',

                'content': user_message,
            },
        ])

        # Extract the AI response
        ai_response = response['message']['content']

        # Return the AI response in JSON format
        return jsonify({'response': ai_response})

    except Exception as e:
        # Handle potential errors
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=2187)  # port is princess leia's cell number
