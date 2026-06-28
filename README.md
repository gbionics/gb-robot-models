# Generative Bionics Robot Models

This repository includes model for robots created by [Generative Bionics](https://gbionics.ai/).

The models contained in this package are:

| Robot Name        | URI                                                    |
|:-----------------:|:------------------------------------------------------:|
| GENE.01 1.0       | `package://gb_robot_models/robots/gene01_0/model.urdf` | 

To simplify the use of the provided models in all tools, all closed loop mechanism in the robot are represented by their serial equivalent. Contact Generative Bionics if for your use case you need a model with a representation of the closed loop mechanisms.

## No-installation demos

To visualize the robot model without installing the model explicitly, just install [uv](https://docs.astral.sh/uv/getting-started/installation/) or [pixi](https://pixi.prefix.dev/latest/installation/), and run the following commands.

### Rerun

~~~
uvx gb-robot-models show-in-rerun package://gb_robot_models/robots/gene01_0/model.urdf
~~~

### RViz (ROS 2)

~~~
pixi exec -c conda-forge -c robostack-jazzy -s gb-robot-models -s ros-jazzy-desktop ros2 launch gb_robot_models display.launch.py
~~~


## Package Installation

To simplify the use of models in existing pipelines, the Generative Bionics robot models are available in different package managers and distribution platforms. If you would like for the models to be available in a channel not mentioned here, please [open an issue](https://github.com/gbionics/gb-robot-models/issues/new).

### conda/pixi via conda-forge

~~~bash
pixi add gb-robot-models
~~~

or 

~~~bash
conda create -n gb-robot-models gb-robot-models
~~~

### pip/uv via pypi

~~~bash
uv pip install gb-robot-models
~~~

or

~~~bash
pip install gb-robot-models
~~~


### With ROS

#### Binary with apt

~~~bash
sudo apt install ros-<distro>-gb-robot-models
~~~

## Model retrieval

Regardless of how you installed the package, the models can easily be found in Python via [`resolve-robotics-uri-py`](https://github.com/gbionics/resolve-robotics-uri-py):

~~~py
absolute_path = resolve_robotics_uri_py.resolve_robotics_uri("package://gb_robot_models/robots/gene01_0/model.urdf")
~~~

or in C++ via [`resolve-robotics-uri-cpp`](https://github.com/gbionics/resolve-robotics-uri-cpp):

~~~cxx
std::optional<std::string> absolute_path = ResolveRoboticsURICpp::resolveRoboticsURI("package://gb_robot_models/robots/gene01_0/model.urdf")
~~~

or using your favorite resource retrieval system for `package://` URIs, like ROS's `ament_index_cpp` or `ament_index_py`, the files installed in gb-robot-models are installed in a way that they can be found by ROS resource retriever. If you are experiencing problem on this, [please open an issue](https://github.com/gbionics/gb-robot-models/issues/new).
