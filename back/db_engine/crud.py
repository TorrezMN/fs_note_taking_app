#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from db_engine import models

#  from schemas.dose_schemas import Dose
#  IMPORTING SCHEMAS
#  from schemas.vaccine_schemas import Vaccine
from sqlalchemy.orm import Session


#  def get_all_notes(db: Session, rec: Record):
def get_all_notes(db: Session, rec):
    print("CRUD -> get_all_notes!")
    #  rec = models.Person_Record(**rec.dict())
    #  db.add(rec)
    #  db.commit()
    #  db.refresh(rec)
    #  return (rec)
