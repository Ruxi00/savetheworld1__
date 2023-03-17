from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rank', methods=['POST'])

def rank():
    #get scores of ppl in class
    num_people = int(request.form['number_people'])
    score = int(request.form['score'])
    #arrange scores in list in descending order
    random.seed(1)
    score_list = random.sample(range(1, 100), num_people)
    score_list.sort(reverse=True)
    #score and placing
    if score in score_list:
        rank = score_list.index(score) + 1
        result = f'The placing of your score within your class is #{rank}'
    else:
        result = 'you are not in this class'
  
    return render_template('result.html', result=result, score_list=score_list)


app.run(host='0.0.0.0', port=81)
