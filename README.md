# Generative Bionics Robot Models

This repository includes model for robots created by [Generative Bionics](https://gbionics.ai/).

The models contained in this package are:

| Robot Name        | URI                                                    |
|:-----------------:|:------------------------------------------------------:|
| GENE.01 1.0       | `package://gb_robot_models/robots/gene01_0/model.urdf` | 

To simplify the use of the provided models in all tools, the provided models have been simplified and all closed loop mechanism in the robot are represented by their serial equivalent. [Contact Generative Bionics](https://gbionics.ai/contact/) (including `gb-robot-models` in the request text) if for your use case you need a model with a representation of the closed loop mechanisms or more information.

## Package installation from source

If the `gb-robot-models` is not available in your preferred package manager or distribution channel, you can also install it from source.

### Install via pip/uv

The `gb-robot-models` is a regular Python package, so it can be installed from source with the following command:

~~~bash
python -m pip install "git+https://github.com/gbionics/gb-robot-models.git"
~~~

or 

~~~bash
uv add "git+https://github.com/gbionics/gb-robot-models.git"
~~~

### Instal via CMake

The `gb-robot-models` is a regular CMake package, so it can be installed from source with the following command:

~~~bash
git clone https://github.com/gbionics/gb-robot-models
cd gb-robot-models
cmake -Bbuild -S. -DCMAKE_INSTALL_PREFIX=<desired_install_prefix>
~~~

### Install via CMake in a colcon/ROS 2 workspace

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
