from sqlalchemy.orm import Session
from db_user import engine, User, Password
from typing import Optional

session = Session(engine)


def clear_db():
    users = session.query(User).all()
    for user in users:
        delete_user_by_id(user.id)


def user_exists(email: str) -> bool:
    return get_user_by_email(email) is not None


def get_user_by_id(_id: int) -> Optional[User]:
    return session.query(User).filter(User.id == _id).first()


def get_user_by_email(email: str) -> Optional[User]:
    return session.query(User).filter(User.email == email).first()


def ger_user_id_by_email(email: str) -> int:
    user = get_user_by_email(email)
    return user.id if user else -1


def add_new_user(name: str, email: str, password: str) -> bool:
    if user_exists(email):
        return False

    user = User(name=name, email=email, password=Password(password=password))
    session.add(user)
    session.commit()
    return True


def delete_user_by_id(_id: int) -> None:
    session.query(User).filter(User.id == _id).delete()
    session.commit()


def delete_user_by_email(email: str) -> None:
    user = get_user_by_email(email)
    if user:
        delete_user_by_id(user.id)


def show_db(db_name) -> None:
    print(*session.query(db_name).all(), sep='\n')


if __name__ == "__main__":
    show_db(User)
