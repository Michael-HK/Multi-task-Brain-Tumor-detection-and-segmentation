FROM python:latest
WORKDIR /root/Project/Docker
COPY main.py /root/Project/Docker
COPY utils.py /root/Project/Docker
COPY Seg_multi-task-v2.hdf5 /root/Project/Docker

RUN pip install --upgrade pip
COPY requirments.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ENTRYPOINT 8080
CMD ["python", "/root/Project/Docker/main.py"]
