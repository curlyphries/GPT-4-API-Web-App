from flask import Flask, request, render_template, redirect, url_for
from gpt_agent import GPTAgent

app = Flask(__name__)
agent = GPTAgent()
agent.load_history('history.json')

@app.route('/')
def index():
    return render_template('index.html', history=agent.history)

@app.route('/prompt', methods=['POST'])
def prompt():
    user_prompt = request.form['prompt']
    response = agent.get_response(user_prompt)
    agent.save_history('history.json')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
