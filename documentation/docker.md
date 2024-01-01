# Docker instructions

> Note that these instructions are for my Mac M1.  I haven't tested on my Windows machine just yet. See the [build.sh](python-dev/build.sh) shell script for more information and sense of how to create a windows powershell equivalent.

## Prerequisites
As a one-time setup you'll need to build the docker image that will be used to run the project.  To do this, run the following command from the root of the project:

```bash
cd python-dev
./build.sh
```

## Launching the dev environment
To launch the dev environment, simply run the following command from the root of the project:

```bash
cd scripts
./startup.sh
```

This will launch a docker stack with a single container, python-dev.  The container will have all the necessary dependencies installed to run the project.  It will also mount the project directory as a volume so that any changes made to the code will be reflected in the container.

### Running the project
Once the dev environment is up and running, you can run the project by running the following command from the root of the project:

```bash
cd scripts
./shell.sh
```

That will allow you to enter the docker container.  Once inside the container, you can run the project by running the following command:

```bash
python3 simulation_tester.py
```

While that works just fine, I prefer to launch VSCode and connect to the running container.  To do this, you'll need to install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.  Once installed, you can launch VSCode and connect to the running container by clicking the green icon in the bottom left corner of the VSCode window.  This will open a menu with a list of options.  Select the "Remote-Containers: Attach to Running Container..." option.  This will open a new VSCode window that is connected to the running container.  

## Shutting down the dev environment
To shut down the dev environment, simply run the following command from the root of the project:

```bash
cd scripts
./shutdown.sh
```

