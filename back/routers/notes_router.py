#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
from db_engine import dose_crud as crud

#  IMPORTING SCHEMAS
from schemas.dose_schemas import Dose, Dose_Name

dose_router = APIRouter(
    prefix="/dose",
    tags=["dose"],
)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@dose_router.get("/get_all_dose")
def get_all_dose(db=Depends(db)):
    """
    Get All Dose
    ---

    Returns a list of ``all`` dose registered in the sistem.

    """

    data = crud.get_all_dose(db)
    size = len(data)
    API_RESPONSE["size"] = size
    API_RESPONSE["data"] = data
    return API_RESPONSE
