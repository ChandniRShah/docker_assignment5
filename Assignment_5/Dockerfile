FROM python
ADD . /myapp
WORKDIR /myapp
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python","app.py"]