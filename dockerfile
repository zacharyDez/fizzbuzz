FROM python
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pytest
ENTRYPOINT ["python"]
CMD ["app.py"]