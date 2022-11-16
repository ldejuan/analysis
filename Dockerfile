FROM python:3.9.15

RUN mkdir -p /inputdir && \
	mkdir -p /outputdir

ADD requirements.txt /
RUN pip install -r /requirements.txt

ADD *.py /
ADD conf /conf

