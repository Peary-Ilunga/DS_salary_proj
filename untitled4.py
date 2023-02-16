# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 19:27:18 2023

@author: Pearry
"""

import glassdoor_scraper as gs
import pandas as pd

path='C:/Users/Pearry/Desktop/DS_salary_proj/chromedriver'

df=gs.get_jobs('data scientist', 15, False,path, 15)