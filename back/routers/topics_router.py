#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
from db_engine import topics_crud as crud

#  IMPORTING SCHEMAS
from schemas.notes_schemas import Topics, Tags, Note
from schemas.base_schema import API_RESPONSE


topics_router = APIRouter(
    prefix="/topics",
    tags=["topics"],
)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@topics_router.get("/")
def topics_root():
    return {"topics": "root!"}


####################
#  TOPICS
####################
@topics_router.get("/get_random_topic")
def get_random_topic(db=Depends(db)):
    API_RESPONSE["data"] = crud.get_random_topic(db)
    return API_RESPONSE


@topics_router.get("/get_all_topics")
def get_all_topics(db=Depends(db)):
    API_RESPONSE["data"] = crud.get_all_topics(db)
    return API_RESPONSE


@topics_router.post("/add_new_topic")
def add_new_topic(word: Topics, db=Depends(db)):
    API_RESPONSE["data"] = crud.new_topic(db, word)
    return API_RESPONSE


@topics_router.post("/filter_topics")
def filter_topics(word: str, db=Depends(db)):
    API_RESPONSE["data"] = crud.filter_topic_by_name(db, word)
    return API_RESPONSE
