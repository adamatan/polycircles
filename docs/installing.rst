.. _installing:

Installing and testing
======================

Installing
----------

The following command:

.. code:: bash

	pip install polycircles

Will install polycircles and all its dependencies.

Testing
-------

First, clone the `git repo <https://github.com/adamatan/polycircles>`_.

.. code:: bash

	git clone https://github.com/adamatan/polycircles.git

Unit tests
~~~~~~~~~~

.. code:: bash

	python setup.py test

BDD tests
~~~~~~~~~

I use `behave <http://pythonhosted.org/behave/>`_ for BDD tests.

.. code:: bash

	pip install -r test_requirements.txt
	behave

Travis builds
`````````````

The package is `built and tested in travis-ci <https://travis-ci.org/adamatan/polycircles>`_ for every commit.

|buildStatus|

.. |buildStatus| image:: https://travis-ci.org/adamatan/polycircles.svg?branch=master
   :alt: Build Status - master branch
   :target: https://travis-ci.org/adamatan/polycircles

