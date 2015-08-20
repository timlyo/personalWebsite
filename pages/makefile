directory = ../dist

all:
	cd partials; make
	haml contact.haml ${directory}/contact.html
	haml index.haml ${directory}/index.html
	haml projects.haml ${directory}/projects.html
	haml usefulLinks.haml ${directory}/usefulLinks.html

	haml tutorials/tutorials.haml ${directory}/tutorials.html
	haml tutorials/C++/thread/threading.haml ${directory}/threading.html
	haml tutorials/C++/thread/thread1.haml ${directory}/thread1.html
	haml tutorials/C++/thread/thread2.haml ${directory}/thread2.html
