#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from datetime import date
from typing import Optional

from pydantic import BaseModel


class Dose(BaseModel):
    dose_number: int

    class Config:
        orm_mode = True


class Dose_Name(BaseModel):
    dose_number: int

    class Config:
        orm_mode = True


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN


from datetime import date
from typing import Optional

from pydantic import BaseModel


class Record(BaseModel):
    nombre: str
    apellido: str
    fecha_aplicacion: date
    cedula: str
    establishment: int
    dose: int
    vaccine: int
    actualizado_al: date

    class Config:
        orm_mode = True
