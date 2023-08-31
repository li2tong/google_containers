FROM ubuntu:22.04
RUN apt update -yq && apt install -y python3 && pip install seamless_communication
ADD runner.py /runner.py
RUN python3 /runner.py
CMD ["tail -f /dev/null"]