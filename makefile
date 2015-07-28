all:
	+cd pages; make
	+cd sass; make

clean:
	find . -name \*.html -type f -delete
	find . -name \*.css -type f -delete
	find . -name \*.css.map -type f -delete

install: all
	cp -r dist/* ~/remotePi/http/
