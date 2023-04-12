#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from typing import Union

from fastapi import FastAPI

#  IMPORTING ROUTERS
from routers import notes_router

app = FastAPI()


#  INCLUDING ROUTERS
app.include_router(notes_router.notes_router)


@app.get("/")
def read_root():
    return {"H3": "World"}


@app.get("/test")
def test_url():
    return {"H333333333333": "World"}
