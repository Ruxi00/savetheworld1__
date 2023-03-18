from flask import Flask, render_template, request
import random
import statistics

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
        result = 'You are not in this class '

    #calculator of stats
    mean_score = int(statistics.mean(score_list))
    median_score = int(statistics.median(score_list))
    mode_score = int(statistics.mode(score_list))
    stdev_score = int(statistics.stdev(score_list))
      
    return render_template('result.html', result=result, score_list=score_list, mean_score=mean_score, median_score=median_score, mode_score=mode_score, stdev_score=stdev_score)

app.run(host='0.0.0.0', port=81)
