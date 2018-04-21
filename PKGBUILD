# Script generated with Bloom
pkgdesc="ROS - hector_pose_estimation provides the hector_pose_estimation node and the hector_pose_estimation nodelet."
url='http://ros.org/wiki/hector_pose_estimation'

pkgname='ros-kinetic-hector-pose-estimation'
pkgver='0.3.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-hector-pose-estimation-core'
'ros-kinetic-message-filters'
'ros-kinetic-nav-msgs'
'ros-kinetic-nodelet'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
)

depends=('ros-kinetic-geometry-msgs'
'ros-kinetic-hector-pose-estimation-core'
'ros-kinetic-message-filters'
'ros-kinetic-nav-msgs'
'ros-kinetic-nodelet'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=hector_pose_estimation
source=()
md5sums=()

prepare() {
    cp -R $startdir/hector_pose_estimation $srcdir/hector_pose_estimation
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

