#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from db_engine.database import Base
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship


class Tags(Base):
    __tablename__ = "Tags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tag_name = Column(String(30), unique=True, index=True)


class Note(Base):
    __tablename__ = "Note"
    note_id = Column(Integer, primary_key=True, autoincrement=True)
    note_content = Column(String(1000), unique=True, index=True)
    note_date = Column(Date, index=True)
    note_tags = relationship("Tags", backref="Note")
