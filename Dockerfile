FROM python:3-slim

COPY loopmsg.py  /

CMD ["python", "/loopmsg.py"]

