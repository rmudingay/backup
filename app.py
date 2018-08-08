from flask import Flask, request, render_template, session, url_for
#from flask_simpleldap import LDAP

app = Flask(__name__)

@app.route('/')
def index():
    login = request.form.get('username')
    return render_template('home.html', login=login)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

@app.route('/addjob')
def addjobs():
    return render_template('forms/add_jobs.html')

@app.route('/addlocation')
def addlocation():
    return render_template('forms/add_location.html')

@app.route('/policy')
def policy():
    return render_template('policy.html')

@app.route('/addpolicy')
def addpolicy():
    return render_template('forms/add_policy.html')

@app.route('/scripts')
def scripts():
    return render_template('scripts.html')

@app.route('/addscript')
def addscript():
    return render_template('forms/add_script.html')

@app.route('/events')
def backup():
    return render_template('events.html')

@app.route('/settings', methods = ['POST', 'GET'])
def config():
    login = request.form.get('username')
    return render_template('settings.html', login=login)

@app.route('/sshkeys')
def sshkey():
    return render_template('sshkeys.html')

@app.route('/addkey')
def addkey():
    return render_template('forms/add_key.html')

@app.route('/accounts')
def account():
    return render_template('accounts.html')

@app.route('/adduser')
def adduser():
    return render_template('forms/add_user.html')

if __name__ == '__main__':
    app.run(debug=True)
