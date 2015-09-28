from flask import Flask, flash, request, url_for, render_template, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager, UserMixin, login_required,login_user,logout_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask (__name__)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/wirewords/Documents/PowerMeter/database.db'
app.secret_key = 'my secret key is this'
login_manager = LoginManager()
login_manager.session_protection ='strong'
login_manager.login_view = "/"
login_manager.init_app(app)




class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username
    

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        userName=request.form['username']
        
        user = User.query.filter_by(username=userName).first()

        print '--------->((('+str(userName)+')))<--------, '+ str(request.form['password'])
        if userName == 'admin' and request.form['password']=='admin':
            login_user(user,False)
            return redirect(request.args.get('next') or url_for('home'))
        flash ('Invalid credentials!!')
    return render_template('login.html')



@app.route ("/home", methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        if request.form['submit'] == "on":
            flash ('On')
        elif request.form['submit'] == "off":
            flash ('Off')

    return render_template('home.html')





@app.route("/logout",methods=["GET"])
@login_required
def logout():
    logout_user()
    flash("You've logged out!!")
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

