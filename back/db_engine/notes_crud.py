#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from db_engine import models
from sqlalchemy.orm import Session

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
