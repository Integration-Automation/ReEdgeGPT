FROM ubuntu:latest
LABEL authors="JE-Chen"
ARG DEBIAN_FRONTEND=noninteractive
# Copy
COPY re_edge_gpt /ReEdgeGPT_Flask
COPY docker-requirements.txt /ReEdgeGPT_Flask
# Auth file
COPY bing_cookies.json /ReEdgeGPT_Flask
COPY bing_cookies.txt /ReEdgeGPT_Flask
# Swagger
COPY /Dockerfiles/Flask/re_edge_gpt_blueprint.py /ReEdgeGPT_Flask
COPY /Dockerfiles/Flask/swagger_config.py /ReEdgeGPT_Flask
# Flask
COPY /Dockerfiles/Flask/docs /ReEdgeGPT_Flask/docs
COPY /Dockerfiles/Flask/main_flask.py /ReEdgeGPT_Flask
# Workdir
WORKDIR /ReEdgeGPT_Flask
# Install dependency
RUN apt update -y && apt upgrade -y && \
    apt-get install -y python3 python3-pip python3-venv && \
    python3 -m venv venv && . venv/bin/activate && \
    pip install -r docker-requirements.txt
# Os path
ENV PATH="/venv/bin:$PATH"
# Open port 7935
EXPOSE 7935
# Start Gunicorn and Flask server
ENTRYPOINT ["/bin/bash", "-c", "source venv/bin/activate && \
gunicorn --bind :7935 --workers=4 main_flask:app"]
