# Package installation from source

If the `gb-robot-models` is not available in your preferred package manager or distribution channel, you can also install it from source.

## Install via pip/uv

The `gb-robot-models` is a regular Python package, so it can be installed from source with the following command:

~~~bash
python -m pip install "git+https://github.com/gbionics/gb-robot-models.git"
~~~

or 

~~~bash
uv add "git+https://github.com/gbionics/gb-robot-models.git"
~~~

## Instal via CMake

The `gb-robot-models` is a regular CMake package, so it can be installed from source with the following command:

~~~bash
git clone https://github.com/gbionics/gb-robot-models
cd gb-robot-models
cmake -Bbuild -S. -DCMAKE_INSTALL_PREFIX=<desired_install_prefix>
~~~

## Install via CMake in a colcon/ROS 2 workspace

As `gb-robot-models` is a regular CMake package equipped with a `package.xml`, so it can be built as part of regular colcon/ROS 2 workspace, for example on Linux:

~~~bash
mkdir -p ~/gb_robot_models_ws/src
cd ~/gb_robot_models_ws
git clone https://github.com/gbionics/gb-robot-models src/gb-robot-models
colcon build
~~~

### Use directly from source repo

To use the models directly from the source repo, just add the repository folder to the `AMENT_PREFIX_PATH` environment variable, for example on Linux:

~~~bash
git clone https://github.com/gbionics/gb-robot-models
export AMENT_PREFIX_PATH=${AMENT_PREFIX_PATH}:$(pwd)/gb-robot-models
~~~