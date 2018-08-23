from flask import Flask, jsonify, abort, request, make_response

app = Flask(__name__, static_url_path="")


@app.route('/')
def home():
    return 'index'


@app.errorhandler(400)
def bad_request(error):
    error
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': ' not found '}), 404)


questions = [
    {
        'id': 1,
        'title': u'What are API',
        'description': u'THese ate web endpoints to GET, POST or DELETE',
        'answer': [
            {
                'answer_id': 1,
                'answer': 'this is answer to the question'
            }
        ]
    },
    {
        'id': 2,
        'title': u'My second question',
        'description': u'This is the second question',
        'answer': True
    }
]

answers = [
    {
        'id': 1,
        'description': u'Are restful API',
        'done': False

    }
]


@app.route('/api/v1/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    # Get method for one question
    question = [question for question in questions if question['id'] == question_id]
    if len(question) == 0:
        abort(404)
    return jsonify({'question': question})


@app.route('/api/v1/questions', methods=['POST'])
def create_question():
    # Post method that post a question
    if not request.json or not 'tittle' in request.json:
        abort(404)
        question = {
            'id': questions[-1]['id'] + 1,
            'tittle': request.json['tittle'],
            'description': request.json.get('description', ""),
            'done': False
        }
        questions.append(question)
    return jsonify({'question': questions}), 201


@app.route('/api/v1questions/<questionId>/answers', methods=['POST'])
def post_answers():
    if not request.json:
        abort(404)
        answer = {
            'id': answers[+1]['id'],
            'description': request.json.get('description', ""),
            'done': False
        }
        questions.append(answer)
    return jsonify({'answer': answers}), 201


if __name__ == '__main__':
    app.run(debug=True)
