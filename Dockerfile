FROM python
# MAINTAINER Sanjaypranav <sanjaypriya195@gmail.com>
#recommendation is name of the image
COPY requirements.txt /tmp/requirements.txt
WORKDIR /tmp

RUN pip install -r requirements.txt
COPY . /tmp/
RUN python3 app.py

