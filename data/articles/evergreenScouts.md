# Evergreen Scouts Website Requirements

For better or for worse, I have agreed to create a website for my local scout group. It will be used to collect and share information about the group with, members and the wider community. This mean that 

* It is easier for people to discover the group
* It is easier for existing members to find out information e.g. program

This document is written to be a non technical overview of the requirements of the site. If there is anything that is unclear or not understood, feel free to contact me.

# Definitions

| -- | -- |
| Evergreens | The scout group that the website belongs to |
| Unit | Individual unit such as Scouts, Beavers |
| Group | The Evergreens group |
| Server | The hardware and software package the website is run on |
| User | A person interacting with the website, whether associated with Evergreens or not |
| Member | A user belonging to the group |
| Admin | A user with permissions to edit data |
| Data | Information stored on the server e.g. images, programs, articles |
| Metadata | Information about a file such as date, title, description |
| Article | A single written document with metadata |
| News | Collective term for all articles |
| Image | A single image file and metadata |
| Gallery | Aspect of the website that displays images |
| Album | Collection of images grouped by a user |
| Website | The package that is presented to a user |
| Program | The week by week schedule of a unit's activities |

# Requirements

Besides the site being pretty, fast, functional etc. it must also fulfill some basic requirements. The requirements listed a purely with regard to functionality, i.e. what the website should do rather than how it will do it, and how it will look. That comes later.

* Commonly accessed pages should be within 3 clicks of the homepage
* All content should be accessible by disadvantaged users as much as possible e.g. colourblind, vision deficient
* The data must only be editable by admins. Users cannot edit articles, or upload images
* The website must be usable across both mobile and desktop platforms
* Resulting documents should pass the following tests
    * https://validator.w3.org/
    * https://developers.google.com/speed/pagespeed/?hl=en
    * https://www.google.com/webmasters/tools/mobile-friendly/
    * http://wave.webaim.org/

## Unit information

Each unit needs to have it's information displayed on their page. This boils down to a couple of fields.

* Meeting times. Day of the week and time.
* Contact details. Phone, email

Some of these should be displayed on the unit's page e.g. cub leader's phone number on /cubs/contact and others such as gsl, should be displayed on a general contact page i.e. /contact. It must be easy for any user to contact an appropriate member of the site, whilst protecting the information of other members.

## Image gallery

The image gallery is designed to act as a long term store for photos that have been taken of, and by our group over the years so that they can be seen by member and used to promote our group. It must be

* Easily navigable gallery
* Allow users to upload photos
* Sort photos into albums

## Program 

The most important feature of the program is to allow users to easily find out what each group is doing on a week by week basis. It must be

* Easily editable in intuitive format
    * The user should be able to add an item to any part of the schedule
    * Reorder the schedule
    * Edit individual program items
* Clearly displayed
* Exportable to a common format, pdf or docx

## News

This will allow admins to post information about events, past or present, for users to view.

* Easily edit articles in an intuitive format
    * WYSIWYG editor. i.e. the article is displayed looking the same as it was when it was edited
    * Images can be embedded and positioned
* Access to articles can be controlled e.g. public, hidden
* Display a list of recent and relevant articles to users

## Stock management

This will make the quartermaster's work easier, and allow admins to easily check stock availability and make requests to borrow items.

* All stock items should be displayed in a table
* There should be a simple form for requesting items
* Dates that items are booked for should be displayed in a calendar format
* The system will email the quarter master with requested in a simple standardised format 