all:
	cd pages; make
	cd css; make

clean:
	rm *.html
	rm style.css
	rm -r style.css.map
