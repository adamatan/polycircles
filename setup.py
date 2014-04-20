from setuptools import setup
from setuptools_behave import behave_test

setup(name='polycircles',
      version='0.1',
      description='Polycircles: WGS84 Circle approximations using polygons',
      url='http://github.com/vioozer/servers',
      author='Adam Matan',
      author_email='adam@matan.name',
      license='MIT',
      packages=['polycircles'],
      include_package_data=True,
      install_requires=['geographiclib'],
      tests_require=['geopy >= 0.99', 'nose >= 1.3.0'],
      test_suite='polycircles.test',
      zip_safe=False)