#! /bin/python
import glob
import re

def getFileTags(fileName):
	with open(fileName) as file:
		text = file.read()
		tags = []
		for meta in re.findall("<meta.*name='keywords'.*>", text):
			for result in re.findall("content='[a-zA-Z, ]*'", meta):
				for tag in result.replace("content=", "").replace("'", "").replace(" ", "").split(","):
					tags.append(tag)

		return tags

# execution point
files = glob.glob("dist/*.html")

with open("dist/javascript/pageList.js", "w") as output:
	output.write("var pages = {};\n")
	output.write("//Tag = Page\n")
	for file in files:
		key = file.replace(".html", "").replace("dist/", "")
		tags = getFileTags(file)
		if "noSearch" in tags:
			continue
		output.write("pages['" + key + "'] = '" + file.replace("dist/", "") + "';\n")
		for tag in tags:
			output.write("pages['" + tag + "'] = '" + file.replace("dist/", "") + "';\n")
