FastAPI Hello World
Follow the first part of this tutorial:

https://neon.tech/blog/deploy-a-serverless-fastapi-app-with-neon-postgres-and-aws-app-runner-at-any-scale

Create Project:

poetry new fastapi-helloworld
Change directory to project:

cd fastapi-helloworld 
Add dependecies:

poetry add fastapi "uvicorn[standard]"
Add poetry virtualenv interpreter in VSCode

Write fastapi_helloworld/main.py

Run project in Poetry Envirnoment:

poetry run uvicorn fastapi_helloworld.main:app --host 0.0.0.0 --port 8000

or

poetry run uvicorn fastapi_helloworld.main:app --reload


Open in Browser:


http://127.0.0.0.0:8000/

http://127.0.0.1:8000/docs



http://127.0.0.0.0:8000/openapi.json
Publish on the Web while running locally


git init

git add .
or
git diff main.py

git commit -m "my first commit"

git remote add origin https://github.com/Asifalishaikh/poetry-micro-services

git branch -M main

git push -u orogin main