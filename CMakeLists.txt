cmake_minimum_required(VERSION 3.10)

project(gb-robot-models VERSION 0.1.0 LANGUAGES NONE)

# GNUInstallDirs warns with LANGUAGES NONE unless LIBDIR already has a value.
if(NOT DEFINED CMAKE_INSTALL_LIBDIR)
  set(CMAKE_INSTALL_LIBDIR "lib" CACHE PATH "Object code libraries")
endif()
include(GNUInstallDirs)

# Install the entire share directory tree into the install prefix.
# The share/ folder is already structured as <prefix>/share/ so
# installing it to CMAKE_INSTALL_DATAROOTDIR produces the correct layout,
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/share/
        DESTINATION ${CMAKE_INSTALL_DATAROOTDIR})

# installs the required package.xml file
# to ensure that gb_robot_models can be found by ros2 pkg,
# this is not already in the share folder as for colcon build from
# source
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/package.xml
        DESTINATION share/gb_robot_models)
