# Script generated with Bloom
pkgdesc="ROS - The hector_localization stack is a collection of packages, that provide the full 6DOF pose of a robot or platform. It uses various sensor sources, which are fused using an Extended Kalman filter. Acceleration and angular rates from an inertial measurement unit (IMU) serve as primary measurements. The usage of other sensors is application-dependent. The hector_localization stack currently supports GPS, magnetometer, barometric pressure sensors and other external sources that provide a geometry_msgs/PoseWithCovariance message via the poseupdate topic."
url='http://ros.org/wiki/hector_localization'

pkgname='ros-kinetic-hector-localization'
pkgver='0.3.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-hector-pose-estimation'
'ros-kinetic-hector-pose-estimation-core'
'ros-kinetic-message-to-tf'
)

conflicts=()
replaces=()

_dir=hector_localization
source=()
md5sums=()

prepare() {
    cp -R $startdir/hector_localization $srcdir/hector_localization
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

