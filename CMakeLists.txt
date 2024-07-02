cmake_minimum_required(VERSION 3.20)
project(dummy_pkg
    LANGUAGES C CXX)
# set(CMAKE_C_STANDARD 17)
# set(CMAKE_CXX_STANDARD 20)

string (APPEND CMAKE_CXX_FLAGS_RELEASE " -O3 ")
string (APPEND CMAKE_C_FLAGS_RELEASE " -O3 ")

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()


# if(PROJECT_IS_TOP_LEVEL)
#     cmake_host_system_information(RESULT HOST QUERY HOSTNAME)
#     cmake_host_system_information(RESULT OSN QUERY OS_NAME)
#     cmake_host_system_information(RESULT OS_VERSION QUERY OS_RELEASE)
#     cmake_host_system_information(RESULT PROC QUERY PROCESSOR_DESCRIPTION)

#     message(STATUS "-------------------------------------")
#     message(STATUS "  Project: ${PROJECT_NAME}")
#     message(STATUS "  Hardware: ${PICO_BOARD}")
#     message(STATUS "  C++ ${CMAKE_CXX_STANDARD}")
#     message(STATUS "  C ${CMAKE_C_STANDARD}")
#     message(STATUS "-------------------------------------")
#     message(STATUS " ${HOST}")
#     message(STATUS " ${OSN}: ${OS_VERSION}")
#     message(STATUS " ${PROC}")
#     message(STATUS "-------------------------------------")

#     # set(BUILD_EXAMPLES ON)
# endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rclcpp REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(sensor_msgs REQUIRED)

list(APPEND node_list
    dummy_node
    transform_node
    lidar_node
)

foreach(app ${node_list})
    add_executable(${app} src/${app}.cpp)
    target_include_directories(${app} PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include/${PROJECT_NAME}>)
    target_compile_features(${app} PUBLIC c_std_17 cxx_std_20)  # Require C99 and C++17
    ament_target_dependencies(
        ${app}
        geometry_msgs
        rclcpp
        tf2
        tf2_ros
        sensor_msgs
    )

    install(TARGETS ${app}
        DESTINATION lib/${PROJECT_NAME})
endforeach()

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
