#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"H33333333333333333333ello": "World"}


@app.get("/test")
def test_url():
    return {"H333333333333": "World"}
