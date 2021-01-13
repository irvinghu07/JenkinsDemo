FROM python:3.7-alpine
RUN ln -s -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
ENV LANG en_US.UTF-8
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR /opt/app
ADD ./requirements.txt .
RUN pip install -r requirements.txt
ADD ./*.py ./
CMD ["flask", "run", "--host", "0.0.0.0"]