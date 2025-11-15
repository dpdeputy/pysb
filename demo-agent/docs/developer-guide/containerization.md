
This guide explains how to build and run the project using containers.

## Building the Docker Image

To build the Docker image for this project, run the following command from the root of the repository:

```bash
docker build -t demo-agent .
```

## Running the Project with Docker

Once the image is built, you can run the project in a Docker container:

```bash
docker run -it --rm demo-agent
```
