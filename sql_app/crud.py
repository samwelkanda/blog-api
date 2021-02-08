from sqlalchemy.orm import Session

from . import models, schemas

def get_posts(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()

def get_post(db:Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id==post_id).first()

def create_post(db:Session, post: schemas.PostCreate):
    db_post = models.Post(title=post.title, text=post.text)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_post(db:Session, post_id: int, post: schemas.PostCreate):
    db_post = db.query(models.Post).filter(models.Post.id==post_id).first()
    db_post.title = post.title
    db_post.text = post.text
    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    db_post = db.query(models.Post).filter(models.Post.id==post_id).first()
    db.delete(db_post)
    db.commit()



