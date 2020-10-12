import time
from sqlalchemy.orm import Session

from . import models, types

#POST
def get_posts(db: Session, skip: int = 0, limit: int = 100):
    """ contacts getter """
    return db.query(models.Post).offset(skip).limit(limit).all()

def get_post_by_id(db: Session, id: int):
    """ contact getter by id """
    post =  db.query(models.Post).filter(models.Post.id == id).first()
    # date_object = time.localtime(post.date)
    # formated_date = time.strftime('%A %D %B %Y %H:%M:%S')
    return post


def create_post(db: Session, post: types.Post):
    date = time.time()
    db_post = models.Post(content=post.content, date=date)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# def set_post_category(db: Session, )


#CATEGORIE
def get_categories(db: Session, skip: int = 0, limit: int = 100):
    """ categories getter """
    return db.query(models.Category).offset(skip).limit(limit).all()

def get_category_by_id(db: Session, id: int):
    """ categorie getter by id """
    return db.query(models.Category).filter(models.Category.id == id).first()


#COMMENT
def get_comments(db: Session, skip: int = 0, limit: int = 100):
    """ comments getter """
    return db.query(models.Comment).offset(skip).limit(limit).all()

def get_comment_by_id(db: Session, id: int):
    """ comment getter by id """
    return db.query(models.Comment).filter(models.Comment.id == id).first()



#USER
def get_users(db: Session, skip: int = 0, limit: int = 100):
    """ users getter """
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, id: int):
    """ user getter by id """
    return db.query(models.User).filter(models.User.id == id).first()
