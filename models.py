from extensions import db, app

class UI(db.Model):
    __tablename__ = 'users'

 
    name = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    id = db.Column(db.Integer, primary_key=True,unique=True, nullable=False)
    number =  db.Column(db.Integer)

    def __repr__(self):
        return f'<User {self.email}>'
    
class Products(db.Model):
    __tablename__ = 'products'

    name = db.Column(db.String, nullable = False)
    photo = db.Column(db.String,nullable=False)
    id = db.Column(db.Integer, primary_key=True, unique=True,nullable=False)    

    def __repr__(self):
        return f'<Product {self.id}>'

