#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.package import parse_package_for_distutils

d = parse_package_for_distutils()
d['packages'] = ['rxbag', 'rxbag.plugin', 'rxbag.util']
d['package_dir'] = {'': 'src'}
d['scripts'] = ['scripts/rxbag']
d['requires'] = ['rospkg']

setup(**d)