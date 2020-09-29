#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:19:51 2020

@author: safir
"""

from pymongo import MongoClient
from config import Config

class Blog:
    def __init__(self):
        self.C = Config()
        self.client = MongoClient(self.C.mongo_client)
        self.db = self.client.get_database('blog_db')
        self.records = self.db.blog_records
        print(self.records.count_documents({}))
        
    def insert(self):
        data = {
        'name': 'Safir',
        'roll_no': '2175052'}
        self.records.insert_one(data)