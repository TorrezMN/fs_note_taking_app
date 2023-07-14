# DOCKERFILE API



FROM python:3.9

WORKDIR /code/back

COPY requirements.txt ./

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN apt-get update && apt-get -y install cron && apt-get -y install htop
RUN apt-get install libpq-dev python3-dev -y


COPY . /code/back
# ==========================




RUN pwd
RUN echo 
RUN echo 
RUN echo 
RUN ls 




ENTRYPOINT ["sh", "entry.sh"]



