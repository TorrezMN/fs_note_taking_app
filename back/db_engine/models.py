#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from db_engine.database import Base
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import backref, relationship


note_tag = Table(
    "note_tag",
    Base.metadata,
    Column("tag_id", Integer(), ForeignKey("tag.id")),
    Column("note_id", Integer(), ForeignKey("note.id")),
)


class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tag_name = Column(String(30), unique=True, index=True)


class Note(Base):
    __tablename__ = "note"
    id = Column(Integer, primary_key=True, autoincrement=True)
    note_content = Column(String(1000), unique=True, index=True)
    note_date = Column(Date, index=True)
    tags = relationship("Tag", secondary=note_tag, backref="tags")


class Topic(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True, autoincrement=True)
    topic_name = Column(String(30), unique=True, index=True)
