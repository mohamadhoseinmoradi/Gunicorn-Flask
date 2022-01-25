FROM python:3.8-alpine

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
WORKDIR /app
COPY --chown=appuser:appgroup requirements.txt /app

RUN \
    pip3 install -U pip \
    && pip3 install -r requirements.txt

COPY --chown=appuser:appgroup . /app 
EXPOSE 5000
USER appuser

CMD ["gunicorn", "wsgi:app", "-w", "2", "--threads", "2", "--bind", "0.0.0.0:8000"]