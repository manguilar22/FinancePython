FROM python:3.7-slim 

LABEL mantainer="manguilar22@gmail.com"  

WORKDIR /app 

COPY . . 

RUN pip install --trusted-host pypi.python.org --requirement requirements.txt 

EXPOSE 5000 

CMD [ "python", "app.py" ] 
