#!/usr/bin/python
import sqlite3
from models.base_model import BaseModel

class FileStorage:
    """FileStorage class"""
    __file_path = "file.db"
    __objects = {}
