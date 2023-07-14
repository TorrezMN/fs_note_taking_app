#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from typing import Union
import pathlib
from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/")
def read_root():
    return {"H33333333333333333333ello": "World"}


@app.get("/test")
def test_url():
    return {"H333333333333": "World"}


@app.get("/markdown")
def get_markdown():
    #  markdown_file = pathlib.Path(__file__).parent / "markdown.md"
    file_path = "some_shit.md"
    file = open(file_path, "w+")
    with file as f:
        f.write("some crazy shit!")
        f.close()
    return FileResponse(path=file_path, filename=file_path, media_type="text/markdown")
