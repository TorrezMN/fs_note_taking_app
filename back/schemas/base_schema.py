#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from time import gmtime, strftime

API_RESPONSE = {
    "version": "0.0.1",
    "date_time": strftime("%Y-%m-%d %H:%M:%S", gmtime()),
}
