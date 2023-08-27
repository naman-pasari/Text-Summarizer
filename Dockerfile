FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install cudatoolkit=11.8
RUN pip install cudnn=8.9.2
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app