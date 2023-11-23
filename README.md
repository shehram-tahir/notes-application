
This is a note creation application integrated with Langchain to summarize notes.
## Installation


```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Configuration
Create and then add your  **OPENAI_API_KEY** in **note_applications/.env**

## Basic Setup

### Run Django Server

Run migrations:
```bash
python manage.py migrate
```
Create a superuser for JWT authentication generation:
```bash
python manage.py createsuperuser
```
Run Django Server:
```bash
python manage.py runserver
```

### Endpoints for JWT Token Creation
Token creation
```bash
Method: POST
Endpoint: /token/
Body: {
    "username": "",
    "password": ""
}
````
Use this token in subsequent requests with header **Authorization: Bearer "token"**

### Endpoints for Note operations
Note creation
```bash
Method: POST
Endpoint: /api/notes/
Body: {
    "title": "",
    "content": "",
}
```
Note deletion
```bash
Method: DELETE
Endpoint: /api/notes/<id>/
```
Note listing
```bash
Method: GET
Endpoint: /api/notes/
```
Note update
```bash
Method: PATCH
Endpoint: /api/notes/<id>/
Body: {
    "title": "",
    "content": "",
}
```
### Endpoints for Note summarization through Langchain integration with GPT-3.5 Turbo
Note summarization
```bash
Method: POST
Endpoint: /api/summarize/note/<id>/
```
## Run Tests
Test coverage is not complete yet
```bash
pyest --create-db
```

### Challenges faced?
The latest version of library openai is incompatible with current latest version of Langchain, 
so I had to shift openai version to an earlier version.

### Thanks!


