# Harvard Open Data Project: Propublica Data Scraper

## Overview

The Propublica Data Scraper is a python script that automates the collection of
non-profit data using the Propublica API. The API retrieves data in csv format
on any list of non-profit US organizations.

Currently the script is extracts data based on a list of organzations in a file
called "list_of_orgs.csv". Organizations are found based off of their
ProPublica number, which can be found the the ProPublica website.

Due to speed of propublica's API, each organization will take around 2-5
seconds resulting in a total of a couple of minutes depending on the number of
organizations you input. The results will be stored in a file called
final_data.csv.

To find out more, go to Propublica's Nonprofit Explorer API here:
<https://projects.propublica.org/nonprofits/api>

## Getting started

Once one has downloaded this directory, they simply need to populate the
list_of_orgs.csv with a list the desired organizations' ProPublica numbers. An
organization's ProPublica number can be found
[here](https://projects.propublica.org/nonprofits/). In order to obtain the
ProPublica number, one must search for the desired non-profit, go to the
page for the desired org, and then copy down the number at the end of the url.
(e.g. Oxfam-America Inc.'s number is 237069110).

To run the script, one simply has to execute `python propublica.py -a`. The
`-a` option means that the script will record data for every field that it can.
If one would like to record data for only specific fields, one can omit the
`-a` option and specify particular fields. For example, running `python
propublica.py -tr` will tell the script to only scrape for the total revenue of
the specified organizations. For a comprehensive list of options, execute
`python propublica.py -h`

## About

This is a project of the [Harvard Open Data Project](http://harvard-open-data-project.github.io/),
a student-faculty collaboration dedicated to opening and analyzing Harvard data
to empower our community members to improve campus life.

##TODO

- Add pictures to 'Getting Started' so that the directions are clearer. 
- Update and integrate Jupyter/iPython notebook for easier prototying
- Figure out a way to search for orgs without ProPublica numbers
