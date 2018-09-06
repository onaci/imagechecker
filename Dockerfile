FROM python:alpine

COPY requirements.txt /
RUN pip install -r requirements.txt

ENV REG_SHA256="58df4554daddbcfcb157778e28f249b1873ae978abfcc7a6bcf33581b4eae944"
RUN apk add --no-cache curl \
        && curl -fSL "https://github.com/genuinetools/reg/releases/download/v0.15.5/reg-linux-amd64" -o "/usr/local/bin/reg" \
	&& echo "${REG_SHA256}  /usr/local/bin/reg" | sha256sum -c - \
	&& chmod a+x "/usr/local/bin/reg"

COPY check_images.py /
WORKDIR /data
ENTRYPOINT ["python", "/check_images.py"]
