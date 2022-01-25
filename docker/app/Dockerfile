FROM python:3.8-alpine

WORKDIR /app
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY --chown=appuser:appgroup requirements.txt .
RUN \
    pip3 install -U pip \
    && pip3 install -r requirements.txt

COPY --chown=appuser:appgroup . . 
EXPOSE 5000
USER appuser

ENTRYPOINT ["gunicorn"]
CMD ["wsgi:app", "-w", "2", "--threads", "2", "--bind", "0.0.0.0:5000"]