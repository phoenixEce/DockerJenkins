FROM python:3.13.0-alpine3.20

WORKDIR /app

RUN pip install sphinx

COPY sum.py /app

RUN sphinx-quickstart -q -p "Documentation de sum en python" -a "Sandrine" -v "1.0" --sep --ext-autodoc --ext-viewcode --makefile --no-batchfile

RUN echo "sum.py.........." >> /app/source/index.rst

# COPY conf.py /app/source

# COPY index.rst /app/source

RUN sphinx-build -b html /app/source /app/build

CMD ["tail", "-f", "/dev/null"]




