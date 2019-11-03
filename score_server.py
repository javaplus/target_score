from flask import Flask, request

import score_keeper
app = Flask(__name__)

@app.route('/scores',methods=['GET', 'DELETE'])
def handleScores():
    if(request.method=='GET'):
        scores = {}
        scores["RED"]= score_keeper.getScoreForTarget("RED")
        scores["BLUE"]= score_keeper.getScoreForTarget("BLUE")
        return scores
    elif(request.method == 'DELETE'):
        score_keeper.clearAllScores()
        return 'success'

if __name__ == '__main__':
    app.run(host='0.0.0.0')