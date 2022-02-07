FROM python:3.8-slim

WORKDIR /app
RUN useradd appuser


COPY --chown=appuser requirements.txt .
RUN \
    pip3 install -U pip \
    && pip3 install -r requirements.txt

COPY --chown=appuser . . 
EXPOSE 5000
USER appuser

ENTRYPOINT ["gunicorn"]
CMD ["wsgi:app", "-w", "2", "--threads", "2", "--bind", "0.0.0.0:5000"]
