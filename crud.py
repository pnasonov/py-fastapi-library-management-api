from sqlalchemy.orm import Session

import models
import schemas


def get_all_authors(db: Session):
    return db.query(models.DBAuthor).all()


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.DBAuthor(name=author.name, bio=author.bio)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    return db_author
