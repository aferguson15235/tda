FROM python:3.8-slim


WORKDIR /heart_model

COPY . /heart_model


RUN pip install -r requirements.txt


## default port for streamlit is 8501

EXPOSE 8501


CMD ["streamlit", "run", "heart_model.py"]


## docker build -t heart_pred .

## docker images

## docker run -p 8501:8501 heart_pred

## docker login

## docker image rm -f heart_pred

## docker build -t abayomibello/heart_pred .