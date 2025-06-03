FROM python:3.11-buster

ARG stage
ARG service

LABEL maintainer="harshit.sharma@finbox.in"
LABEL com.datadoghq.tags.env="${stage}"
LABEL com.datadoghq.tags.service="${service}"

# Upgrade pip to latest version
RUN pip install --upgrade pip

# Set working directory
WORKDIR /app

# Copy project requirements
COPY requirements.txt .

# Install required python dependencies
RUN pip install -r requirements.txt

# ----------------------------------------------------------
# Security Steps
# ----------------------------------------------------------
# Secure docker container to mount only specific directories

# Add entry point script
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# Make entrypoint script executable
RUN chmod +x /usr/local/bin/entrypoint.sh

# Secure docker file to prevent shell access

# Install dash
RUN apt-get update && apt-get install -y dash

# Remove other shells
RUN rm /bin/bash && rm /bin/rbash
RUN rm /bin/cat /bin/cp /bin/ls /bin/more /bin/nisdomainname
RUN rm /bin/egrep /bin/fgrep /bin/zgrep /bin/bzgrep /bin/findmnt
RUN rm /bin/tar /bin/gzip /bin/gunzip /bin/bzip2 /bin/bunzip2
RUN rm /bin/bzcat /bin/bzexe /bin/bzmore /bin/bzless /bin/bzip2recover
RUN rm /bin/zcat /bin/zcmp /bin/zdiff /bin/zegrep /bin/zfgrep
RUN rm /bin/zforce /bin/zless /bin/zmore /bin/znew /bin/rmdir
RUN rm /bin/readlink /bin/touch /bin/mkdir /bin/chgrp
RUN rm /bin/dd /bin/sync /bin/chmod /bin/chown /bin/echo
RUN rm /bin/hostname /bin/domainname /bin/dnsdomainname /bin/tempfile
RUN rm /bin/ypdomainname /bin/login /bin/su /bin/ps /bin/stty 
RUN rm /bin/run-parts

# Create a symbolic link for /bin/sh to use dash
RUN ln -sf /bin/dash /bin/sh

# Rename dash to dash-only-for-finbox
RUN mv /bin/dash /bin/dash-only-for-finbox

# -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x

COPY . .

# Set healthcheck path and properties
HEALTHCHECK --interval=10s --timeout=10s --start-period=5s --retries=10 \
  CMD curl -f http://localhost:8080/health || exit 1

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]