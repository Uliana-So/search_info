FROM    python:3.8

WORKDIR /opt/search_info

COPY    ./conf/requirements.txt .

RUN     pip install --upgrade pip && \
        pip install --no-cache-dir -r requirements.txt && \
        rm requirements.txt

RUN     mkdir /opt/search_info/logs && \
        chmod -R 644 .

COPY    ./flask_app/web_app .

COPY    ./conf/add_db.py .

COPY    ./conf/posts.csv .

EXPOSE  5040
