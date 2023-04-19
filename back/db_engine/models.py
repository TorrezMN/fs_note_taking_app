#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from db_engine.database import Base
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship

note_tags = Table(
    "note_tags",
    Base.metadata,
    Column("note_id", ForeignKey("Note.id"), primary_key=True),
    Column("tags_id", ForeignKey("Tags.id"), primary_key=True),
)


class Tags(Base):
    __tablename__ = "Tags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tag_name = Column(String(30), unique=True, index=True)
    notes = relationship("Note", secondary=note_tags, back_populates="Tags")


class Note(Base):
    __tablename__ = "Note"
    id = Column(Integer, primary_key=True, autoincrement=True)
    note_content = Column(String(1000), unique=True, index=True)
    note_date = Column(Date, index=True)
    tags = relationship("Tags", secondary=note_tags, back_populates="Note")


class Topics(Base):
    __tablename__ = "Topics"
    id = Column(Integer, primary_key=True, autoincrement=True)
    topic_name = Column(String(30), unique=True, index=True)
