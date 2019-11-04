from flask import Flask, render_template #we call flask

app = Flask(__name__) #__name__ is the file that pytho offer to start de app
#we initialize flask, then we get an odject called app,
# as from this odject we can create route, initialize a server.

@app.route('/')# @ is a decorator. this is the main website "app is an object and .route is a method"
def home(): #what gonna happen when I call this function.
    return render_template('home.html')

@app.route('/about')#I copied this from above in order to create another route.
def about(): 
    return render_template('about.html')


if __name__ == '__main__': #this confirm if this is our main file, not a module.
    app.run(debug=True)#allow us to run our app. so initialize the odject



