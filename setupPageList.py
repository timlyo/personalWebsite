#! /bin/python
import glob
import re

def getFileTags(fileName):
	with open(fileName) as file:
		text = file.read()
		tags = []
		for meta in re.findall("<meta.*name='keywords'.*>", text):
			for result in re.findall("content='[a-z, ]*'", meta):
				for tag in result.replace("content=", "").replace("'", "").replace(" ", "").split(","):
					tags.append(tag)

		return tags


files = glob.glob("dist/*.html")

with open("dist/javascript/pageList.js", "w") as output:
	output.write("var pages = {};\n")
	for file in files:
		key = file.replace(".html", "").replace("dist/", "")
		output.write("pages['" + key + "'] = '" + file.replace("dist/", "") + "';\n")
		tags = getFileTags(file)
		for tag in tags:
			output.write("pages['" + tag + "'] = '" + file.replace("dist/", "") + "';\n")
