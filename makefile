all:
	cd pages; make
	cd css; make

clean:
	find . -name \*.html -type f -delete
	rm style.css
	rm -r style.css.map
