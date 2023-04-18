#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
from db_engine import crud as crud

#  IMPORTING SCHEMAS
from schemas.notes_schemas import Tags
from schemas.base_schema import API_RESPONSE


tags_router = APIRouter(
    prefix="/tags",
    tags=["tags"],
)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@tags_router.get("/")
def tags_root():
    return {"tags": "root!"}


####################
#  TAGS
####################


@tags_router.get("/get_all_tags")
def get_all_tags(db=Depends(db)):
    API_RESPONSE["data"] = crud.get_all_tags(db)
    return API_RESPONSE


@tags_router.post("/add_new_tag")
def add_new_tag(word: Tags, db=Depends(db)):
    API_RESPONSE["data"] = crud.new_tag(db, word)
    return API_RESPONSE


@tags_router.post("/filter_tags")
def filter_tags(word: str, db=Depends(db)):
    API_RESPONSE["data"] = crud.filter_tag_by_name(db, word)
    return API_RESPONSE
