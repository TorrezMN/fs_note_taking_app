#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
from db_engine import crud as crud

#  IMPORTING SCHEMAS
from schemas.notes_schemas import Tags, Note
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
def get_random_topic(n, db=Depends(db)):
    return {"notes": "get_random_topic!"}
