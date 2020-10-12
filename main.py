from fastapi import Depends, FastAPI, HTTPException, Query, Path, Body
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel, Field

#
from app import crud, models, types
from app.database import SessionLocal, engine


app = FastAPI()


# database managment object getter
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


class Item(BaseModel):
    name: str = 'default name'
    description: str = 'default description'



@app.get('/')
def root():
    return {
        'message':'amazing blog site',
        
        }




@app.get('/db/')
def create_nb(db:Session = Depends(get_db)):
    print(dir(db))
    return db



@app.put('/post/create/', response_model=types.Post)
def create_post(post: types.Post = Body(..., embed=True),  db:Session = Depends(get_db)):
    db_post = crud.create_post(db, post)
    return db_post




@app.get("/posts/", response_model=List[types.Post])
def read_posts(d: int = 0, f: int = 100, db: Session = Depends(get_db)):
    """ all posts getter endpoind """
    #get posts
    posts = crud.get_posts(db, skip=d, limit=f)
    return posts

@app.get("/post/{post_id}", response_model=types.Post)
def read_contact(post_id: str, q: str = None, db: Session = Depends(get_db)):
    """ specific post getter endpoint """
    #get post by the id 
    post = crud.get_post_by_id(db, post_id)
  
    return post



@app.get("/categories/", response_model=List[types.Category])
def read_categories(d: int = 0, f: int = 100, db: Session = Depends(get_db)):
    """ all categories getter endpoind """
    #get categories
    categories = crud.get_categories(db, skip=d, limit=f)
    return categories

@app.get("/category/{categorie_id}", response_model=types.Category)
def read_categorie(categorie_id: str, q: str = None, db: Session = Depends(get_db)):
    """ specific categorie getter endpoint """
    #get category the id 
    category = crud.get_category_by_id(db, categorie_id)
    return category


#COMMENTS
@app.get("/comments/", response_model=List[types.Comment])
def read_comments(d: int = 0, f: int = 100, db: Session = Depends(get_db)):
    """ all comments getter endpoind """
    #get comments
    comments = crud.get_comments(db, skip=d, limit=f)
    return comments

@app.get("/comment/{comment_id}", response_model=types.Comment)
def read_comment(comment_id: str, q: str = None, db: Session = Depends(get_db)):
    """ specific comment getter endpoint """
    #get comment by the id 
    comment = crud.get_comment_by_id(db, comment_id)
    return comment


#USERS
@app.get("/users/", response_model=List[types.User])
def read_users(d: int = 0, f: int = 100, db: Session = Depends(get_db)):
    """ all users getter endpoind """
    #get users
    users = crud.get_users(db, skip=d, limit=f)
    return users

@app.get("/user/{user_id}", response_model=types.User)
def read_user(user_id: str, q: str = None, db: Session = Depends(get_db)):
    """ specific user getter endpoint """
    #get user by the id 
    user = crud.get_user_by_id(db, user_id)
    return user
