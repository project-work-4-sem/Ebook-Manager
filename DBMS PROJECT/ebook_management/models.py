from ebook_management import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_reader(reader_id):
    return reader.query.get(int(reader_id))

# reader_books=db.Table('reader_books',
# 	db.Column('reader_id', db.Integer, db.ForeignKey('reader.reader_id')),
# 	db.Column('book_id', db.Integer, db.ForeignKey('books.book_id')))

class reader_books(db.Model) :
	__tablename__ = 'Reader_Books'
	reader_id=db.Column('reader_id',db.Integer,db.ForeignKey('reader.reader_id'),primary_key=True)
	book_id=db.Column('book_id', db.Integer, db.ForeignKey('books.book_id'),primary_key=True)
	content=db.Column('content',db.Text,nullable=True)

class reader(db.Model,UserMixin):
 	reader_id=db.Column(db.Integer,primary_key=True)
 	username=db.Column(db.String(20),unique=True,nullable=False)
 	email=db.Column(db.String(20),nullable=False)
 	name=db.Column(db.String(20),nullable=False)
 	password = db.Column(db.String(60), nullable=False)
 	books_reading=db.relationship('books',secondary='Reader_Books',backref=db.backref('readers',lazy='dynamic'))

 	def get_id(self):
 		return (self.reader_id)

 	def __repr__(self):
 		return f"reader('{self.username}','{self.email}','{self.name}','{self.password}')"


class books(db.Model):
    book_id=db.Column(db.Integer,primary_key=True)
    isbn=db.Column(db.Integer,nullable=False)
    title=db.Column(db.String(20))
    category=db.Column(db.String(20))
    link=db.Column(db.Text)
    path=db.Column(db.Text)
    # readers=db.relationship('reader',secondary='Reader_Books',backref=db.backref('books_reading',lazy='dynamic'))

    def __repr__(self):
    	return f"books('{self.isbn}','{self.title}','{self.category}')"


