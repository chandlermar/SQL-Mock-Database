FROM python:3
RUN pip install coverage pytest
ADD PA1.py Parser.py Table.py Database.py test_db.py /
CMD ["sh", "-c", "coverage run -m pytest test_db.py && coverage report > coverage.txt && python PA1.py"]
