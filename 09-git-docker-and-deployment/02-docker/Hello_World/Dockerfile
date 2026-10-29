#Linux image is base image
FROM python:3.7 
# copy fille from my local repository to app. this app will get created in the container 
COPY . /app
# setup working directory
WORKDIR /app
# install all the dependicies
RUN pip install -r requirements.txt
# Command to run : python app.py
CMD ["python","app.py"]