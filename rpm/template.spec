Name:           ros-indigo-hector-pose-estimation-core
Version:        0.2.1
Release:        1%{?dist}
Summary:        ROS hector_pose_estimation_core package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hector_pose_estimation_core
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-indigo-geographic-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-rosconsole
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rostime
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf
BuildRequires:  eigen3-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-geographic-msgs
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-rosconsole
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rostime
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf

%description
hector_pose_estimation_core is the core package of the hector_localization
stack. It contains the Extended Kalman Filter (EKF) that estimates the 6DOF pose
of the robot. hector_pose_estimation can be used either as a library, as a
nodelet or as a standalone node.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Nov 08 2015 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.2.1-1
- Autogenerated by Bloom

* Sun Nov 08 2015 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.2.1-0
- Autogenerated by Bloom

* Sun Feb 22 2015 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.2.0-0
- Autogenerated by Bloom

