FROM ubuntu:latest
LABEL authors="JE-Chen"
ARG DEBIAN_FRONTEND=noninteractive
# Copy whole project to image
COPY . /ReEdgeGPT_Flask
# You need put your bing_cookies.json to Dockerfiles/Flask dir
COPY Dockerfiles/Flask/bing_cookies.json /ReEdgeGPT_Flask
# You need put your bing_cookies.txt to Dockerfiles/Flask dir
COPY Dockerfiles/Flask/bing_cookies.txt /ReEdgeGPT_Flask
# Flask init
COPY Dockerfiles/Flask/re_edge_gpt_blueprint.py /ReEdgeGPT_Flask
# Swagger
COPY Dockerfiles/Flask/swagger_config.py /ReEdgeGPT_Flask
# Flask
COPY Dockerfiles/Flask/docs /ReEdgeGPT_Flask/docs
# Flask
COPY Dockerfiles/Flask/main_flask.py /ReEdgeGPT_Flask
# Workdir
WORKDIR /ReEdgeGPT_Flask
# Install dependency
RUN apt-get update && \
    apt-get install -y python3.10 python3-pip python3.10-venv && \
    python3 -m venv venv && \
    . venv/bin/activate && \
    pip install -r requirements.txt
# Os path
ENV PATH="/venv/bin:$PATH"
# Open port 8888
EXPOSE 8888
# Start Gunicorn and Flask server
ENTRYPOINT ["/bin/bash", "-c", "source venv/bin/activate && \
gunicorn --bind :8888 --workers=4 main_flask:app"]