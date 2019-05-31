FROM python:3.7-slim

#==========
# Arguments
#==========
ARG UID=1000
ARG GID=1000
ARG USER=test-user
ARG GROUP=test-user

#==================
# Add user to Group
#==================
RUN getent group ${GID} || groupadd ${GROUP} --gid 1000 && \
    useradd --create-home --shell /bin/bash ${USER} --uid ${UID} --gid ${GID}

#============================
# Install Python Dependencies
#============================
COPY requirements.txt /home/${USER}/
RUN pip install -r /home/${USER}/requirements.txt
