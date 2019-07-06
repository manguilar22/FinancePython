FROM python:slim-3.7 

WORKDIR /app 

COPY . . 

RUN pip install --trusted-host pypi.python.org  -r requirements.txt 

EXPOSE 5000 

CMD [ "python", "app.py" ] 