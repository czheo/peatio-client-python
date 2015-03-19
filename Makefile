test:
	unit2 discover

clean:
	rm -rfv build dist *.egg-info .eggs

.PHONY: test clean
