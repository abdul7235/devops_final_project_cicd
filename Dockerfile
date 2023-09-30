FROM python:latest

ADD . /devops_final_project_cicd

WORKDIR /devops_final_project_cicd

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
