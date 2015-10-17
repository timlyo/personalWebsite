all:
	+cd sass; make

install: all
	cp -r dist/* ~/remotePi/http/; \
