ARG ARCH
ARG PYTHON_VERSION

FROM ${ARCH}/python:${PYTHON_VERSION}

# Install dependencies for the project; add your own if you wish
RUN debian_frontend=noninteractive apt-get update && apt-get install -y \
    curl \
    gnupg \
    python3 \
    python3-pip \
    nodejs \
    npm \
    sqlite3

COPY ./backend/requirements.txt /app/backend/requirements.txt
COPY ./frontend/package.json /app/frontend/package.json

WORKDIR /app/backend/
RUN pip3 install -r requirements.txt

#node version 18.19
WORKDIR /app/frontend/
#RUN npm cache --clean 
RUN npm install 
RUN npm ci


CMD [ "bash" ]