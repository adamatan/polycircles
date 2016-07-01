clean:
	rm -rf dist polycircles/test/kmls
pypi:
	python setup.py sdist upload --sign
