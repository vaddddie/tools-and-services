from sqlalchemy import func, inspect
from app.models.engine import engine, Base, Session
from app.schemas.user import User

inspector = inspect(engine)
tables = inspector.get_table_names()

def create_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    if tables:
        Base.metadata.drop_all(engine, checkfirst=True)

    Base.metadata.create_all(engine)
    
def add_new_users(users):
    with Session() as session:
        for user in users:
            location = [
                user['location']['country'],
                user['location']['state'],
                user['location']['city'],
                user['location']['street']['name'],
                str(user['location']['street']['number'])
            ]
            new_user = User(
                gender = user['gender'],
                first_name = user['name']['first'],
                last_name = user['name']['last'],
                phone = user['phone'],
                email = user['email'],
                location = ', '.join(location),
                picture = user['picture']['medium']
            )
            session.add(new_user)
        session.commit()
        
def get_user_by_id(user_id: int):
    with Session() as session:
        return session.query(User).filter(User.id == user_id).first()
    
def get_random_user():
    with Session() as session:
        return session.query(User).order_by(func.random()).first()
    
def get_all_users():
    with Session() as session:
        return session.query(User).all()
    
