from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Global variables to track score
player_score = 0
computer_score = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    global player_score, computer_score

    user_choice = request.json['choice']
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = 'Tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = 'You Win!'
        player_score += 1
    else:
        result = 'You Lose!'
        computer_score += 1

    # Check for max score
    game_over = False
    if player_score == 10:
        result = "🎉 You won the game! Score reset."
        player_score = 0
        computer_score = 0
        game_over = True
    elif computer_score == 10:
        result = "💻 Computer won the game! Score reset."
        player_score = 0
        computer_score = 0
        game_over = True

    return jsonify({
        'user': user_choice,
        'computer': computer_choice,
        'result': result,
        'player_score': player_score,
        'computer_score': computer_score,
        'game_over': game_over
    })

@app.route('/reset', methods=['POST'])
def reset():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    return jsonify({'status': 'reset'})

if __name__ == '__main__':
    app.run(debug=True)
