rx
==

This is a fork of rx for using rxbag with rxbag_plugins on hydro (i.e. being able to plot data from a rosbag without playing and watching the images published).
More info on rxbag_plugins: http://wiki.ros.org/rxbag_plugins

This is because rqt_bag, for now, can't do these things as stated in this issue: https://github.com/ros-infrastructure/rospkg/issues/59

rx and all it's contents are officialy deprecated in hydro.

Got rid of rxtools (rxconsole, rxloggerlevel...) as they depended on swig-wx and I found it problematic to package.

Be warned that a "not-so-clean-trick" was used to load the rxbag_plugins:
https://github.com/awesomebytes/rx/blob/hydro-devel/rxbag/src/rxbag/plugins.py#L104-L123

