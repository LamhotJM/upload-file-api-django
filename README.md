## Status
[![Build Status](https://api.travis-ci.org/LamhotJM/upload-file-api-django.svg)](https://travis-ci.org/LamhotJM/upload-file-api-django)

## Deploy
https://mysterious-garden-78512.herokuapp.com/api/comments/

## Comment API
1. CRUD API
2. Uploading File
3. Unit Testing
4. Migration file
5. CI using travis

## Installing 
```
- django-admin startproject {$project-name}
- env\Scripts\activate
- $ pip install -r requirements.txt
- python manage.py makemigrations commentengine (create migration file)
- python manage.py migrate commentengine 0001_initial
- python manage.py runserver
- python manage.py test
```

## Request
`headers = { 'content-type': "multipart/form-data;}`
