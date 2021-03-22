FROM python:alpine3.8
COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
