from sqlalchemy import Column, Integer, String
from app.models.engine import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    gender = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)
    email = Column(String)
    location = Column(String)
    picture = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'gender': self.gender,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'email': self.email,
            'location': self.location,
            'picture': self.picture
        }