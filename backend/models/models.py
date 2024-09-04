from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name =  db.Column(db.String(80), unique=False, nullable = False)
    last_name =  db.Column(db.String(80), unique=False, nullable = False)
    email=  db.Column(db.String(120), unique=True, nullable = False)
    
    
    # Function that take all of the different fields on our object and 
    # convert it to Python dictionary, which we can convert it then into JSON
    def to_json(self):
        return {
            "id": self.id,
            "firstName":  self.first_name,
            "lastName": self.last_name,
            "email": self.email,  
        }