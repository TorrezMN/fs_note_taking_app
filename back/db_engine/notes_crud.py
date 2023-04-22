#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from db_engine import models
from sqlalchemy.orm import Session
from random import choice
from sqlalchemy import desc


from db_engine.tags_crud import get_tag_by_id

#  IMPORTING SCHEMAS
from schemas.notes_schemas import Tags, Note


def new_note(db: Session, t: Note):
    tags = [get_tag_by_id(db, i) for i in t.tags]
    n = models.Note()
    n.note_content = t.note_content
    n.note_date = t.note_date
    n.tags = tags
    db.add(n)
    db.commit()
    db.refresh(n)
    return n


def get_all_notes(db: Session):
    notes = db.query(models.Note).all()
    tags = [i.tags for i in notes]
    return notes


def filter_note(db: Session, word: str):
    note = db.query(models.Note).filter(models.Note.note_content.contains(word)).first()
    tags = note.tags
    return note


def filter_note_id(db: Session, id: int):
    note = db.query(models.Note).filter(models.Note.id == id).first()
    tags = note.tags
    return note


def get_n_notes(db: Session, n: int):
    results = db.query(models.Note).all()
    tags = [i.tags for i in results]
    return [choice(results) for i in range(0, n)]


def get_latest_note(db: Session):
    results = db.query(models.Note).all()
    return results
