#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
from db_engine import crud as crud

#  IMPORTING SCHEMAS
#  from schemas.dose_schemas import Dose, Dose_Name

notes_router = APIRouter(
    prefix="/notes",
    tags=["notes"],
)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@notes_router.get("/")
def notes_root():
    return {"notes": "root!"}


####################
#  NOTES
####################


@notes_router.get("/get_all_notes")
def get_all_notes(db=Depends(db)):
    return {"notes": "get_all_notes!"}


@notes_router.post("/filter_notes_by_content")
def filter_notes_by_content(word, db=Depends(db)):
    return {"notes": "filter_notes_by_content!"}


@notes_router.post("/filter_notes_by_id")
def filter_notes_by_id(id, db=Depends(db)):
    return {"notes": "filter_notes_by_id!"}


####################
#  TAGS
####################


@notes_router.get("/get_all_tags")
def get_all_tags(db=Depends(db)):
    return {"notes": "get_all_tags!"}


@notes_router.post("/add_new_tag")
def add_new_tag(word, db=Depends(db)):
    return {"notes": "add_new_tag!"}


@notes_router.post("/filter_tags")
def filter_tags(word, db=Depends(db)):
    return {"notes": "filter_tags!"}
