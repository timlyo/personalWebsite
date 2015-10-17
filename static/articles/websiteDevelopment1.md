---
title: Website Development Part 1 - The static pages
outline: How this website was made
date: 2015/17/10
---

# Website Development Pt 1 - The Static Pages

> You have to believe me, this was a stupid decision, but I did it with the best intentions. Some of the worst things imaginable have been done with the best intentions. You know what, Billy? As far as I'm concerned, you're no better than the people that built this place.

## The Beginning

Ignoring my previous forays into web development, this is where it all began. I was coming to the 2<sup>nd</sup> year of my university course and I needed something to present the results for a [data analysis project](https://github.com/timlyo/redditReadability). A few hours later I'd created a github pages repository; created an index page, a contact page, and a project page; mushed bootstrap on top of the entire thing and sent it in for grading.

About the only decision that I can say I was proud of is my use of haml and sass. At least maintainace was easy. This site had so little content, even a minimalist would begin quoting Oliver Twist. Yet it was mine, with my name on it and, more importantly, let me get the grade for that project.

## Unwarranted Features and Misguided Implementations 

The site had barely been up for a day and I was bored of it. If an employer saw my site they'd want to see something more than text, they want something that pops out at then. *Endquote*

A few hours, and almost that many beers later, I'd decided to make a search function. What would it search for? Well I had about 4 pages, that was a start! Having recently been impressed by it, i'd decided to try and copy the search bar from the android developers website. This was probably the best decision I had made. They had a fancy dropdown box that would display the links directly as you typed, non of that loading a new page non sense.

A textbox that captured the user input and sent it to my web server, which then polled a database for the pages of my website, ordered the information, and sent it back to be displayed. Would have been a great way to do this. But nope. I was using apache so ajax would have been awkward, and besides I want something to do now; none of that *research* stuff.

My first problem was determining the dataset to search. My solution to this was to run a [python script](https://github.com/timlyo/personalWebsite/blob/4eddcebb1a84961f249c5aa9e35281161e5f1610/setupPageList.py) when the site was being compiled. This script would go through each html file, create a key from the filename and pull a bunch of tags from the meta tags of the html file. The whole dictionary would then be saved into a [javascript](https://github.com/timlyo/personalWebsite/blob/4eddcebb1a84961f249c5aa9e35281161e5f1610/dist/javascript/pageList.js) file which would be downloaded with the page and the variable would be included globally for every function to see.

I then had another [bit of javascript](https://github.com/timlyo/personalWebsite/blob/4eddcebb1a84961f249c5aa9e35281161e5f1610/dist/javascript/search.js) that would take the value in the search box, go through all the pages in the variable, while adding any that were within a levenshtein distance of 7 from a tag in the variable. 

It worked. Well I could type in the name of a page on my website and tab down to the result that I wanted
