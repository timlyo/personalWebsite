directory = static

all:
	sass --watch sass/style.sass:${directory}/css/style.css --style compressed &
	sass --watch sass/articleStyle.sass:${directory}/css/articleStyle.css --style compressed &
	sass --watch sass/codeStyle.sass:${directory}/css/codeStyle.css --style compressed &
