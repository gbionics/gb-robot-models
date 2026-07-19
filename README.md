# Generative Bionics Robot Models

This repository includes model for robots created by [Generative Bionics](https://gbionics.ai/).

The models contained in this package are:

| Robot Name        | URI                                                    |
|:-----------------:|:------------------------------------------------------:|
| GENE.01 1.0       | `package://gb_robot_models/robots/gene01_0/model.urdf` | 

To simplify the use of the provided models in all tools, the provided models have been simplified and all closed loop mechanism in the robot are represented by their serial equivalent. [Contact Generative Bionics](https://gbionics.ai/contact/) (including `gb-robot-models` in the request text) if for your use case you need a model with a representation of the closed loop mechanisms or more information.

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

> [!WARNING]
> Supporting the installation of models with `sudo apt install ros-<distro>-gb-robot-models` is tracked in https://github.com/gbionics/gb-robot-models/issues/3 .

Even if `gb-robot-models` still needs to be packaged as `apt` binary package, as `gb-robot-models` is a regular CMake package equipped with a `package.xml`, so it can be built from source as part of regular colcon/ROS 2 workspace, for example on Linux:

~~~bash
mkdir -p ~/gb_robot_models_ws/src
cd ~/gb_robot_models_ws
git clone https://github.com/gbionics/gb-robot-models src/gb-robot-models
colcon build
~~~

### From source

If the `gb-robot-models` is not available in your preferred package manager or distribution channel, you can also install it from source, following the documentation available in [`install_from_source.md`](./install_from_source.md)


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

## License

This repository is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International (CC-BY-NC-4.0)](https://spdx.org/licenses/CC-BY-NC-4.0.html) license. See the [LICENSE](LICENSE) file for the full license text.

[Contact Generative Bionics](https://gbionics.ai/contact/) (including `gb-robot-models` in the request text) if for your use case you need a model with a different license.
