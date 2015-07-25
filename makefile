all:
	cd pages; make
	cd css; make

clean:
	find . -name \*.html -type f -delete
	find . -name \*.css -type f -delete
	find . -name \*.css.map -type f -delete
