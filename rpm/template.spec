%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-rqt-rviz
Version:        0.6.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rqt_rviz package

License:        BSD
URL:            http://wiki.ros.org/rqt_rviz
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python3-devel
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-rqt-gui
Requires:       ros-noetic-rqt-gui-cpp
Requires:       ros-noetic-rviz
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-rqt-gui
BuildRequires:  ros-noetic-rqt-gui-cpp
BuildRequires:  ros-noetic-rviz
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
rqt_rviz provides a GUI plugin embedding RViz. Note that this rqt plugin does
NOT supersede RViz but depends on it.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Tue May 12 2020 Louise Poubel <louise@osrfoundation.org> - 0.6.1-1
- Autogenerated by Bloom

