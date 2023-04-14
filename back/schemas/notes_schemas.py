#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from datetime import date
from typing import Optional
from pydantic import BaseModel

#  class Record(BaseModel):
#  nombre: str
#  apellido: str
#  fecha_aplicacion: date
#  cedula: str
#  establishment: int
#  dose: int
#  vaccine: int
#  actualizado_al: date
#
#  class Config:
#  orm_mode = True


class Tags(BaseModel):
    tag_name: str

    class Config:
        orm_mode = True


class Note(BaseModel):
    note_content: str
    note_date: date
    note_tags: int

    class Config:
        orm_mode = True
