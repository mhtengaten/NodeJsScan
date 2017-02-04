#!/usr/bin/env python
# -*- coding: utf_8 -*-
#Settings of NodeJSSCan
import os
import socket

# GENERAL
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULES_FILE = os.path.join(BASE_DIR, 'core', 'rules.xml')
LOG_FILE = os.path.join(BASE_DIR, 'njs-log.txt')
UPLOAD_FOLDER = os.path.join(os.path.expanduser('~'), ".NodeJsScan/")
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
SCAN_FILES_EXTENSION = [".yml", ".js", ".json", ".sh", ""]
UPLD_ALLOWED_EXTENSIONS = ['.zip']
UPLD_MIME = [
    'application/zip',
    'application/octet-stream',
    'application/x-zip-compressed',
    'binary/octet-stream',
]
HMAC_KEY = socket.gethostname() + 'set_0n3_pl3@s3'
HOST = '0.0.0.0'
PORT = 9090
DEBUG = False
# Postgres DB Connection URL
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/nodejsscan'
