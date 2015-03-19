test:
	python -m unittest discover

clean:
	rm -rfv build dist *.egg-info

.PHONY: test clean
