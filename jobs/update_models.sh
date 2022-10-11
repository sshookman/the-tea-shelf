#!/bin/bash

cd app && python3 manage.py makemigrations shelf && python3 manage.py migrate
