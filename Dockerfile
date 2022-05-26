# use FROM to start from a base image
FROM ubuntu

RUN mkdir -p /usr/src/app
# change to an /app directory using WORKDIR
WORKDIR /usr/src/app
# use COPY to copy files into the above directory
COPY . ./
# use VOLUME to allow the container to save data when
VOLUME /usr/src/app
# set an environment variable using ENV
ENV PYTHONPATH="/usr/src/app:${PYTHONPATH}"
RUN apt-get update && apt-get install -y git
# update the package manager and installed required packages with RUN

WORKDIR /app/assignment
RUN apt install -y python3-pip tmux htop
RUN pip install uvicorn fastapi

# use ENTRYPOINT to run a default command
ENTRYPOINT [ "uvicorn", "backend:app", "--reload", "--host", "0.0.0.0", "--port", "54321" ]
# use EXPOSE to document the port your container exposes
EXPOSE 54321
# use CMD to run another default command
CMD [ "tmux" ]


# To build this dockerfile, run the following command: docker build -t allandocker .

# To run this docker image, run the following command: docker run -it -p 54321:54321 allandocker

