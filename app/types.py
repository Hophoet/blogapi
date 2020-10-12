from typing import List, Optional

from pydantic import BaseModel

class CommentBase(BaseModel):
    """ categories base schema """
    content: Optional[str] = None
    user_id: Optional[int] = None


class Comment(CommentBase):
    """ comments  base model """
    id: int = None

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    """ posts base type """
    content: str
    date: float
    category_id: Optional[int] = None


class Post(PostBase):
    """ post type  """
    id: int = None
    comments: List[Comment] = []

    class Config:
        orm_mode = True




class CategoryBase(BaseModel):
    """ categories base schema """
    name: Optional[str] = None


class Category(CategoryBase):
    """ categories schema on the base model """
    id: int
    posts: List[Post] = []
  
    
    class Config:
        orm_mode = True




class UserBase(BaseModel):
    """ users base schema """
    id: int


class User(UserBase):
    """ users schema on the base model """
    id: int
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    comments: List[Comment] = []
    
    class Config:
        orm_mode = True

