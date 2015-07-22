FROM python:2.7.9

RUN apt-get update && apt-get -y install default-jre unzip socat

ADD requirements.txt /src/
RUN cd /src && pip install -r requirements.txt

RUN wget http://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/3.2.1/flyway-commandline-3.2.1.zip && unzip flyway-commandline-3.2.1.zip -d /opt && chmod a+x /opt/flyway-3.2.1/flyway
ENV PATH $PATH:/opt/flyway-3.2.1

ADD ./sql /opt/flyway-3.2.1/sql/
ADD . /src/
WORKDIR /src

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:api"]

EXPOSE 5000
