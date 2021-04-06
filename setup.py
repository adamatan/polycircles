import sys
from setuptools import setup

if sys.version_info >= (3,5):
    geopy = 'geopy >= 2'
else:
    geopy = 'geopy == 1.0'

setup(name='polycircles',
      version='0.3',
      description='Polycircles: WGS84 Circle approximations using polygons',
      long_description=open('README.md').read(),
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.3",
          "Topic :: Scientific/Engineering :: GIS",
          "Topic :: Software Development :: Libraries",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "Intended Audience :: Information Technology",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"
      ],
      url='http://polycircles.rtfd.org',
      author='Adam Matan',
      author_email='adam@matan.name',
      license='MIT',
      packages=['polycircles'],
      include_package_data=True,
      install_requires=['geographiclib'],
      tests_require=[
          geopy,
          'nose >= 1.3.0',
          'simplekml >= 1.3.0',
          'behave >= 1.2.6'
      ],
      test_suite='polycircles.test',
      zip_safe=False)
from setuptools import setup

