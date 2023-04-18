import os
from fastapi import FastAPI, Depends, Request, HTTPException
from db_engine.database import SessionLocal, engine
from sqlalchemy.orm import Session
from db_engine import models
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

#  IMPORTING ROUTERS
from routers import notes_router
from routers import tags_router
from routers import topics_router


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Note Taking API",
    #  description="A small api to explore COVID data of Paraguay..",
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  INCLUDING ROUTERS
app.include_router(notes_router.notes_router)
app.include_router(tags_router.tags_router)
app.include_router(topics_router.topics_router)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"H3": "World"}
