from flask_app import app
from flask import render_template,redirect,request,session,flash

# import the class from user.py
from flask_app.models.user import User


#removed all previous routes per advice
#paired down to create a new page and the route that creates the user


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = User.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)
    #all_friends=friends

@app.route("/users/new")
def new_page():
    return render_template("create_page.html")


#this app route processes teh form - hence the POST method
@app.route('/create', methods=["POST"])
def create():
    #check if form info is valid
    #create user if it is valide
    #if not valid send user back to create page adn show message

    if User.is_valid_user(request.form):
        User.save(request.form)
        return redirect("/")
    
    else:
        return redirect("/users/new")


    
    
    
    # user_form_info = request.form  

    # if User.is_valid_user(user_form_info):
    #     User.save(user_form_info)
    
    return redirect("/users/new")






    # user_info = request.form
    # if User.is_valid_user(user_info):
    #     User.save(user_info)
    #     print("PASS")
    #     return redirect('/')
    # print("FAIL")

    # return redirect('/users/new')


