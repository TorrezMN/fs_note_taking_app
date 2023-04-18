#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from db_engine import models
from sqlalchemy.orm import Session
from random import choice

#  IMPORTING SCHEMAS
from schemas.notes_schemas import Topics


def get_random_topic(db: Session):
    data = choice(db.query(models.Topics).all())
    return data


def get_all_topics(db: Session):
    return db.query(models.Topics).all()


def new_topic(db: Session, t: Topics):
    topic = models.Topics(**t.dict())
    db.add(topic)
    db.commit()
    db.refresh(topic)
    return topic


def filter_topic_by_name(db: Session, topic_name: str):
    return (
        db.query(models.Topics)
        .filter(models.Topics.topic_name.contains(topic_name))
        .first()
    )
