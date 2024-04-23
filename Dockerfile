FROM python:3-alpine3.15

RUN pip install nltk

WORKDIR /app
COPY stopworods.py ./
COPY paragraphs.txt ./

EXPOSE 300

CMD [ "python3","./stopworods.py" ]