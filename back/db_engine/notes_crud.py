#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from db_engine import models
from sqlalchemy.orm import Session

#  IMPORTING SCHEMAS
from schemas.notes_schemas import Tags, Note


def get_all_tags(db: Session):
    return db.query(models.Tags).all()


def new_tag(db: Session, t: Tags):
    tag = models.Tags(**t.dict())
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag


def filter_tag_by_name(db: Session, tag_name: str):
    return db.query(models.Tags).filter(models.Tags.tag_name.contains(tag_name)).first()
