FROM python:3.12

COPY . /Z_YouTube_Downloader_bot

WORKDIR /Z_YouTube_Downloader_bot

RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN chmod 755 .

CMD [ "python", "main.py    " ]
