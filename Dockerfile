from gofast/bigbase

ADD . /ansible
WORKDIR /ansible

RUN pip install -r requirements.txt

ENTRYPOINT []
