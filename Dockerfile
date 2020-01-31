FROM python:3

RUN apt-get update && apt-get install -y libev-dev python3-dev libevdev2
RUN pip install pipenv
COPY . /app
RUN cd /app && pipenv install && pipenv install bjoern
WORKDIR /app
CMD pipenv run python app.py --environment prod