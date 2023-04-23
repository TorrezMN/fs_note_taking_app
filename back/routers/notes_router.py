#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
from db_engine import notes_crud as crud

#  IMPORTING SCHEMAS
from schemas.notes_schemas import Note
from schemas.base_schema import API_RESPONSE


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


@notes_router.post("/add_new_note")
def add_new_note(n: Note, db=Depends(db)):
    API_RESPONSE["data"] = crud.new_note(db, n)
    return API_RESPONSE


@notes_router.get("/get_all_notes")
def get_all_notes(db=Depends(db)):
    API_RESPONSE["data"] = crud.get_all_notes(db)
    return API_RESPONSE


@notes_router.post("/filter_notes_by_content")
def filter_notes_by_content(word: str, db=Depends(db)):
    API_RESPONSE["data"] = crud.filter_note(db, word)
    return API_RESPONSE


@notes_router.post("/filter_notes_by_id")
def filter_notes_by_id(id: int, db=Depends(db)):
    API_RESPONSE["data"] = crud.filter_note_id(db, id)
    return API_RESPONSE


@notes_router.post("/get_n_notes")
def get_n_notes(n: int, db=Depends(db)):
    API_RESPONSE["data"] = crud.get_n_notes(db, n)
    return API_RESPONSE


@notes_router.get("/get_latest_note")
def get_latest_note(db=Depends(db)):
    API_RESPONSE["data"] = crud.get_latest_note(db)
    return API_RESPONSE


@notes_router.get("/get_random_note")
def get_random_note(db=Depends(db)):
    API_RESPONSE["data"] = crud.get_random_note(db)
    return API_RESPONSE


@notes_router.get("/delete_note")
def get_random_note(note_id: int, db=Depends(db)):
    API_RESPONSE["data"] = crud.delete_note_by_id(db, note_id)
    return API_RESPONSE
