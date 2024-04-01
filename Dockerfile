FROM python:3.9

WORKDIR /git_action

COPY ./requirements.txt /git_action/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /git_action/requirements.txt

COPY ./main.py /git_action/main.py