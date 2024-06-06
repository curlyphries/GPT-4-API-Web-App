```markdown
# GPT-4 Web Application

This application allows you to interact with a GPT-4 model through a web interface. You can input prompts and get responses, with a history of your interactions stored and displayed. Additionally, you can upload files and perform basic manipulations on their contents.

## Prerequisites

- **Python 3.8 or higher**
- **pip** (Python package installer)
- **virtualenv** (for creating a virtual environment)
- **OpenAI API Key**

## Installation

### 1. Clone the Repository

```sh
git https://github.com/curlyphries/GPT-4-API-Web-App.git
cd GPT-4-API-Web-App.git
```

### 2. Create a Virtual Environment

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory of your project and add your OpenAI API key:

```sh
touch .env
```

Add the following line to the `.env` file:

```
OPENAI_API_KEY=your_openai_api_key
```

### 5. Prepare the Template Directory

Ensure you have a `templates` directory with the following files:

#### `index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>GPT-4 Web Application</title>
</head>
<body>
    <h1>GPT-4 Web Application</h1>
    <form method="post" action="{{ url_for('prompt') }}">
        <label for="prompt">Enter your prompt:</label>
        <input type="text" id="prompt" name="prompt" required>
        <button type="submit">Submit</button>
    </form>
    <form method="post" action="{{ url_for('upload_file') }}" enctype="multipart/form-data">
        <label for="file">Upload a file:</label>
        <input type="file" id="file" name="file" required>
        <button type="submit">Upload</button>
    </form>
    <h2>Conversation History</h2>
    <ul>
        {% for entry in history %}
            <li>
                <strong>Prompt:</strong> {{ entry.prompt }}<br>
                <strong>Response:</strong> {{ entry.response }}<br>
                <strong>Timestamp:</strong> {{ entry.timestamp }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `file_content.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>File Content</title>
</head>
<body>
    <h1>File Content of {{ filename }}</h1>
    <pre>{{ content }}</pre>
    <form method="post" action="{{ url_for('manipulate_file', filename=filename) }}">
        <label for="operation">Select operation:</label>
        <select id="operation" name="operation">
            <option value="reverse">Reverse</option>
            <option value="uppercase">Uppercase</option>
            <option value="lowercase">Lowercase</option>
        </select>
        <button type="submit">Apply</button>
    </form>
    <a href="{{ url_for('download_file', filename=filename) }}">Download File</a>
</body>
</html>
```

### 6. Run the Application

Start the Flask application:

```sh
python app.py
```

The application should be running on `http://127.0.0.1:5000`.

## Application Structure

```sh
your-repo/
├── app.py
├── gpt_agent.py
├── history.json (created automatically after running the app)
├── requirements.txt
├── .env
└── templates/
    ├── index.html
    └── file_content.html
```

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000`.
2. Enter your prompt in the input field and submit.
3. View the response and interaction history on the same page.
4. Upload a file to read its contents and perform basic manipulations.

## Running the Application

To run the application in different environments (development or production), you can use the following instructions:

### Development

For development, you can run the Flask application with debug mode enabled. This allows you to see detailed error messages and automatically reload the server when you make changes to the code.

```sh
export FLASK_ENV=development
python app.py
```

### Production

For production, you should use a production-ready server like `gunicorn`. First, install `gunicorn`:

```sh
pip install gunicorn
```

Then, run the application using `gunicorn`:

```sh
gunicorn -w 4 app:app
```

This command runs the application with 4 worker processes.

## Troubleshooting

- **Environment Variables:** Make sure your `.env` file is correctly set up with your OpenAI API key.
- **Dependencies:** Ensure all dependencies are installed by running `pip install -r requirements.txt`.
- **File Structure:** Verify that the directory structure is correct and that all files are in the right place.

## License

This project is licensed under the MIT License.
```
