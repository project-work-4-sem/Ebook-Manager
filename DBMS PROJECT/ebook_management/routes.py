import os
import secrets
import csv
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from ebook_management import app, db, bcrypt
from ebook_management.forms import LoginForm,RegistrationForm, UpdateAccountForm, AddReviewForm, EditReviewForm
from ebook_management.models import books, reader, reader_books, reader_books_review
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename


@app.route('/')
@app.route('/home')
def home():
    res1=db.engine.execute(" SELECT * FROM books ")
    book=res1.fetchall()
    return render_template("home.html",book=book)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        q=db.engine.execute(" SELECT email,password FROM reader where email=(?)",(form.email.data))
        res=q.fetchone()
        email=res.email
        password=res.password
        Reader = reader.query.filter_by(email=form.email.data).first()
        if res and password==form.password.data:
            login_user(Reader, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('MyBooks'))  # change home to MyBooks
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated: 
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #Reader = reader(username=form.username.data,email=form.email.data,name=form.name.data,password=hashed_password)
        db.engine.execute("INSERT INTO reader(username,email,name,password) VALUES (?,?,?,?) ",
            (form.username.data,form.email.data,form.name.data,form.password.data))
        #db.session.add(Reader)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route("/MyBooks")
@login_required
def MyBooks():
    q=db.engine.execute("SELECT book_id,title,link,isbn,path,category FROM books NATURAL JOIN reader_books WHERE reader_id=(?)",(current_user.reader_id))
    books=q.fetchall()
    
    return render_template('MyBooks.html', books=books)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/AddBooks/<int:book_id>',methods=['GET', 'POST'])
@login_required
def AddBooks(book_id):
    db.engine.execute(" INSERT INTO reader_books(reader_id,book_id) VALUES (?,?) ",(current_user.reader_id,book_id))
    db.session.commit()
    flash('Book Added! YAY!', 'success')
    return redirect(url_for('MyBooks'))

@app.route('/DeleteBooks',methods=['GET', 'POST'])
@login_required
def DeleteBooks():
    q=db.engine.execute("SELECT book_id,title,category FROM books NATURAL JOIN reader_books WHERE reader_id=(?)",(current_user.reader_id))
    books=q.fetchall()
    if request.method=='POST':
        response=request.form.getlist('myselect')
        for i in response:
            db.engine.execute("DELETE FROM reader_books WHERE reader_id=(?) AND book_id=(?) ",(current_user.reader_id,int(i)) )
            db.session.commit()
        flash('Books Deleted!', 'success')
        return redirect(url_for('MyBooks'))
    return render_template('DeleteBooks.html', books=books)


@app.route('/SearchBooks',methods=['GET','POST'])
@login_required
def SearchBooks():
    q=db.engine.execute("SELECT * FROM BOOKS")
    books=q.fetchall()
    return render_template('search.html', books=books)

@app.route("/books/<int:book_id>",methods=['GET', 'POST'])
def Books(book_id):
    q=db.engine.execute("SELECT * FROM reader_books_review WHERE book_id=(?)",book_id)
    reviews=q.fetchall()
    form=AddReviewForm()
    form2=EditReviewForm()
    book = books.query.get_or_404(book_id)
    authors={}
    present=False
    #query for book already owned by user
    q1=db.engine.execute("SELECT book_id FROM reader_books WHERE reader_id=(?)",current_user.reader_id)
    rbooks=q1.fetchall()
    owned=False
    for x in rbooks:
        if x.book_id==book_id:
            owned=True
    if current_user.is_authenticated==False:
        return redirect(url_for('login'))
    for x in reviews:
    	if x.content!=None:
    		author=reader.query.get(x.reader_id)
    		authors[x.reader_id]=author.username

    	if current_user.reader_id==x.reader_id:
    		present=True
    if form.validate_on_submit() and form.submit.data:
    	db.engine.execute("INSERT INTO reader_books_review(reader_id,book_id,content) VALUES (?,?,?)",(current_user.reader_id,book_id,form.review_content.data) )
    	db.session.commit()
    	flash('Review Added! YAY!', 'success')
    	return redirect(url_for('Books',book_id=book_id))
    if form2.validate_on_submit() and form2.submit_edit.data:
    	db.engine.execute( "UPDATE reader_books_review SET content=(?) WHERE reader_id=(?) AND book_id=(?)",(form2.review_content_edit.data,current_user.reader_id,book_id))
    	db.session.commit()
    	flash('Your review has been updated!', 'success')
    	return redirect(url_for('Books',book_id=book_id))
    elif request.method == 'GET':
        for x in reviews:
            if x.reader_id==current_user.reader_id:
                form2.review_content_edit.data=x.content
                break
    
    return render_template('Book.html',book=book,reviews=reviews,authors=authors,present=present,form=form,form2=form2,owned=owned)

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html',image_file=image_file, form=form)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/books/<int:book_id>/delete", methods=['POST'])
@login_required
def delete_review(book_id):
    q=db.engine.execute("DELETE FROM reader_books_review WHERE reader_id= (?) AND book_id=(?)",(current_user.reader_id,book_id))
    db.session.commit()
    flash('Your review has been deleted!', 'success')
    return redirect(url_for('Books',book_id=book_id))

@app.route('/SearchBooksAdd',methods=['GET','POST'])
@login_required
def SearchBooksAdd():
    q=db.engine.execute("SELECT * FROM books WHERE books.book_id NOT IN (SELECT b.book_id FROM books AS b JOIN reader_books AS rb ON b.book_id=rb.book_id AND rb.reader_id=(?))",(current_user.reader_id))
    books=q.fetchall()
    return render_template('search.html', books=books)