PY = python
PYFLAGS = 
DOC = doxygen
DOCFLAGS = 
DOCCONFIG = config
SRC = src/testCircles.py
.PHONY: all prog doc clean
test: 
	python src/testCircles.py
doc: 
	doxygen config
	cd latex && $(MAKE)
all: test doc
clean:
	rm -rf html
	rm -rf latex