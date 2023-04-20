#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from db_engine import models
from sqlalchemy.orm import Session
from random import choice

#  IMPORTING SCHEMAS
from schemas.notes_schemas import Topics


def get_random_topic(db: Session):
    data = choice(db.query(models.Topic).all())
    return data


def get_all_topics(db: Session):
    return db.query(models.Topic).all()


def new_topic(db: Session, t: Topics):
    topic = models.Topic(**t.dict())
    db.add(topic)
    db.commit()
    db.refresh(topic)
    return topic


def filter_topic_by_name(db: Session, topic_name: str):
    return (
        db.query(models.Topic)
        .filter(models.Topic.topic_name.contains(topic_name))
        .first()
    )
