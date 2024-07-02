from flask import render_template, redirect, flash, session
from forms import LoginForm, RegisterForm, Editor, Addproduct, Deleteproduct
from models import UI, db, Products
from werkzeug.security import check_password_hash, generate_password_hash
from extensions import app




@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "adminadmin":
            return redirect("admin")
        
        user = UI.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_email'] = user.email
            return redirect('secondpage')
        else:
            error = "Invalid email or password. Please try again."
        
    return render_template("index.html", form=form, error=error)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    error = None
    if form.validate_on_submit():
        existing_user = UI.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            hashed_password = generate_password_hash(form.password.data)
            new_user = UI(
                name=form.name.data,
                lastname=form.lastname.data,
                email=form.email.data,
                password=hashed_password
            )
            db.session.add(new_user)
            db.session.commit()
            session['user_email'] = new_user.email
            return redirect('secondpage')
        else:
            error = "Email already exists. Please use a different email."
    return render_template("register.html", form=form, error=error)

@app.route("/secondpage", methods=['GET','POST'])
def second_page():
    products = Products.query.all()
    return render_template("secondpage.html",products=products)

@app.route("/thirdpage", methods=['GET','POST'])
def third_page():
    form = Editor()
    
    user_email = session.get('user_email')   
    user = UI.query.filter_by(email=user_email).first()
    
    if form.validate_on_submit():
        if form.name.data:
            user.name = form.name.data
        if form.lastname.data:
            user.lastname = form.lastname.data
        if form.email.data:
            user.email = form.email.data
        if form.number.data:
            user.number = form.number.data
        
        db.session.commit()
        flash('Your changes have been saved successfully.', 'success')
    
    return render_template("thirdpage.html", form=form, user=user)

@app.route("/admin", methods=["GET","POST"])
def admin_page():
    products = Products.query.all()
    return render_template("admin.html", products=products)

@app.route("/addproduct", methods=["GET","POST"])
def add_product():
    form = Addproduct()
    if form.validate_on_submit():
        new_product =  Products(
                name=form.name.data,
                photo = form.photo.data
            )
        db.session.add(new_product)
        db.session.commit()
        return redirect("/admin")
    return render_template("addproduct.html", form=form)

@app.route("/deleteproduct", methods=["GET", "POST"])
def delete_product():
    form = Deleteproduct()
    error = None 
    if form.validate_on_submit():
        product_name = form.name.data
        product_to_delete = Products.query.filter_by(name=product_name).first()
        if product_to_delete:
            db.session.delete(product_to_delete)
            db.session.commit()
            flash('Product deleted successfully.', 'success')
            return redirect('/admin')
        else:
            error = 'Product not found.'
            return render_template("deleteproduct.html", form=form, error=error)

    return render_template("deleteproduct.html", form=form)


