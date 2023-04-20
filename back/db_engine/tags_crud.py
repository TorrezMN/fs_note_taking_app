#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from db_engine import models
from sqlalchemy.orm import Session

#  IMPORTING SCHEMAS
from schemas.notes_schemas import Tags, Note


def get_all_tags(db: Session):
    return db.query(models.Tag).all()


def new_tag(db: Session, t: Tags):
    tag = models.Tag(**t.dict())
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag


def filter_tag_by_name(db: Session, tag_name: str):
    return db.query(models.Tag).filter(models.Tag.tag_name.contains(tag_name)).first()


def get_tag_by_id(db: Session, tag_id: int):
    return db.query(models.Tag).get(tag_id)
