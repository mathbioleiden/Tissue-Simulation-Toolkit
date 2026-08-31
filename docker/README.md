# Tissue Simulation Toolkit - Docker Setup

This guide describes how to build and run the Tissue Simulation Toolkit with Docker (`tst2-docker`), including X11 GUI support.

## Prerequisites

* [Docker](https://docker.com)
* X11 server (e.g., [XQuartz](https://www.xquartz.org/) on macOS, X11 on Linux)

## 1. Enable X11 Forwarding

Start your X11 server and allow connections from your local machine:

```bash
xhost + ${hostname}
```

> You might have to replace `${hostname}` with the actual hostname of your machine or you can try `localhost` or `local:docker`. 

## 2. Pull or Build the Docker Image

You can either pull a pre-built docker image, or build your own image:

To pull our pre-built docker image:

```bash
docker pull --platform linux/amd64 sbrshakibi/tst2-docker:latest
```

To build a docker image, navigate to the folder containing the Dockerfile and build the image:

```bash
DOCKER_BUILDKIT=1 docker build --platform linux/amd64 -t tst2-docker:latest .
```

> On some machines you can omit `DOCKER_BUILDKIT=1` because this is set as default.

## 3. Run the Docker Container with X11 Support

```bash
docker run -it \
  --env DISPLAY=host.docker.internal:0 \
  --volume /tmp/.X11-unix:/tmp/.X11-unix \
  --user root sbrshakibi/tst2-docker:latest
```

Replace `sbrshakibi/tst2-docker:latest` with `tst2-docker:latest` if you built the docker image yourself. This command starts the container, and the terminal session switches to an interactive shell inside it. When a GUI application is launched from the container, a new window will appear displaying the application’s interface.

## 4. Run standalone Cellular Potts Model (TST)

Inside the Docker container:

```bash
cd bin
./vessel ../data/chemotaxis.par
```

If you encounter the following error: 

`qt.qpa.screen: QXcbConnection: Could not connect to display ... Could not connect to any X display`

- If you used `local:docker` as the hostname in Step 1, try updating the display environment variable in Step 3 to `--env DISPLAY=$DISPLAY`.

- On macOS devices, ensure XQuartz has “Allow connections from network clients” enabled in `XQuartz > Preferences > Security`

## 5. Run Cellular Potts Model with Extra-Cellular Matrix (TST-MD)

To activate the Python virtual environment and run the simulation manager navigate to the main directory of Tissue-Simulation-Toolkit and run:

```bash
. venv/bin/activate
muscle_manager --start-all ymmsl/adhesions.ymmsl ymmsl/plot_state.ymmsl
```

## Notes

* Make sure `XQuartz` or another X11 server is running and accepts connections before launching the Docker container.
* When running `docker build` on an Apple Silicon Mac, the flag `--platform linux/amd64` ensures Docker builds for the Intel/AMD architecture (amd64). Without this, Docker defaults to arm64, which may not be fully supported by all dependencies or the Makefile, potentially causing build failures.