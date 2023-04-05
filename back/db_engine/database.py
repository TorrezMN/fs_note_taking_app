#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


POSTGRESQL_DATABASE_URL = "postgresql://username:password@db:5433/note_taking_db"


engine = create_engine(POSTGRESQL_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
