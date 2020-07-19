from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/forum")
def forum():
    return render_template("forum.html")
@app.route("/women-in-stem")
def wistem():
    topic = "Women in STEM"
    topic1 = "How can I find opportunities as a women in STEM"
    topic2 = "What organizations should I look into as a women in STEM"
    return render_template('topics.html', topic=topic, topic1=topic1, topic2=topic2)
@app.route("/responses")
def wistemrep():
    rep1 = "I would recommend joining community groups which can be found on many different platforms such as Slack, Facebook, etc."
    rep2 = "This is the perfect place to start - if you are looking for opportunities I know we have a great community here, perhaps we should start a new topic for opportunities or even write them here."
    return render_template('discussion.html', rep1=rep1, rep2=rep2)
@app.route("/responses", methods=['GET', 'POST'])
def repond():
    if request.method == 'POST' and 'reply' in request.form:
        reply = request.form('reply')
    return render_template('discussion.html', reply=reply)
if __name__ == "__main__":
    app.run(debug=True)