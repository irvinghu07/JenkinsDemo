FROM python:3.7-alpine
RUN ln -s -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
ENV LANG en_US.UTF-8
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV FLASK_APP=app
ENV FLASK_ENV=development
WORKDIR /opt/app
ADD ./requirements.txt .
RUN python -m pip install --upgrade pip \
    pip install -r requirements.txt
ADD ./*.py ./
EXPOSE 80
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "80"]