#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from datetime import date
from typing import Optional
from pydantic import BaseModel
from typing import List


class Topics(BaseModel):
    topic_name: str

    class Config:
        orm_mode = True


class Tags(BaseModel):
    tag_name: str

    class Config:
        orm_mode = True


class Note(BaseModel):
    note_content: str
    note_date: date
    tags: List[int]

    class Config:
        orm_mode = True
