from ebook_management import *
from ebook_management.models import books,reader,reader_books,Author
import random
db.create_all()
print(random.randint(2001,2017))
for x in range(1,990):
	year=random.randint(2001,2017)
	db.engine.execute("UPDATE books SET year = (?)  WHERE book_id= (?)",(year,x))
# db.engine.execute(" INSERT INTO books(isbn,title,category) VALUES (275846,'Eloquent JavaScript','programming')")
# db.engine.execute(" INSERT INTO books(isbn,title,category) VALUES (186518,'Huckleberry Finn','fiction')")
# db.engine.execute(" INSERT INTO books(isbn,title,category) VALUES (187018,'Bleak House','sci-fi')")
# db.engine.execute(" INSERT INTO books(isbn,title,category) VALUES (192819,'Lord of the Rings','fiction')")
# db.engine.execute(" INSERT INTO books(isbn,title,category) VALUES (200520,'Let Us C','programming')")
# db.engine.execute(" INSERT INTO books(isbn,title,category) VALUES (196519,'Dune','sci-fi')")
# db.engine.execute(" INSERT INTO books(isbn,title,category) VALUES (201320,'Digital Design','science')")
# db.engine.execute(" INSERT INTO books(isbn,title,category) VALUES (199819,'A Brief History of Time','science')")
# db.engine.execute(" INSERT INTO books(isbn,title,category) VALUES (199819,'The Art of War','military-art')")

# db.engine.execute(" INSERT INTO reader(username,email,name,password) VALUES ('smq','abc@ab.com','John','123@123')")
# db.engine.execute(" INSERT INTO reader(username,email,name,password) VALUES ('digbick','xyz@xyz.com','Dave','1707@12')")

# db.engine.execute(" INSERT INTO reader_books(reader_id,book_id) VALUES (1,3),(1,5),(1,7),(2,5),(2,9),(2,4) ")
# db.engine.execute(" INSERT INTO review(reader_id,book_id,content) VALUES (2,4,'Amazing Book. Want to read again') ")
#r=db.engine.execute(" SELECT * FROM reader ")
# b=db.engine.execute(" SELECT readers FROM books")
# rb=db.engine.execute(" SELECT * FROM reader_books")

# r1=reader(email='sol@aol.com',name='max',password='121011')
# b1=books(isbn=100001,title='ABC',category='fiction')
# db.session.add(b1);
# b1.readers.append(r1)

# res=rb.fetchall()
# for x in res:
# 	print(x)
db.session.commit()