from flask import Flask #we call flask

app = Flask(__name__) #we initialize flask, then we get an odject called app,
# as from this odject we can create route, initialize a server.

@app.route('/')# this is the main website "app is an object"
def home(): #what gonna happen when I call this function.
    return 'hello world'

@app.route('/about')#I copied this from above in order to create another route.
def about(): 
    return 'about page'


if __name__ == '__main__': #this confirm if this is our main file, not a module.
    app.run()#allow us to run our app. so initialize the odject



