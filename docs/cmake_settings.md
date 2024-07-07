# CMake Settings

```cmake
# default C99 C++17
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 17)
endif()
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 20)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic -Wshadow)
endif()

...

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)
install(DIRECTORY
  config
  DESTINATION share/${PROJECT_NAME}
)

install(
  DIRECTORY include/
  DESTINATION include/${PROJECT_NAME}
)

install(
  TARGETS my_library
  EXPORT export_${PROJECT_NAME}
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib
  RUNTIME DESTINATION bin
)

ament_export_targets(export_${PROJECT_NAME} HAS_LIBRARY_TARGET)
ament_export_dependencies(some_dependency)
```

- [ros2 how-to params](https://docs.ros.org/en/jazzy/How-To-Guides/Ament-CMake-Documentation.html)
- [roboticsbackend.com params](https://roboticsbackend.com/ros2-yaml-params/)

## Linting

```cmake
find_package(ament_lint_auto REQUIRED)
ament_lint_auto_find_test_dependencies()
```

This will run linters as defined in the package.xml. It is recommended to use the set of linters defined by the package ament_lint_common. The individual linters included there, as well as their functions, can be seen in the ament_lint_common docs.

Linters provided by ament can also be added separately, instead of running ament_lint_auto. One example of how to do so can be found in the ament_cmake_lint_cmake documentation.