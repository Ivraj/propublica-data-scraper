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
list_of_orgs.csv file with the ProPublica numbers of the desired organizations.
In order to obtain the ProPublica number, one must search for the desired
non-profit in ProPublica's Non-Profit Explorer, go to the page for the desired
org, and then copy down the number at the end of the url.  For example,
Oxfam-America Inc.'s number is 237069110. The Non-Profit Explorer can be found
[here](https://projects.propublica.org/nonprofits/). 

To run the script, one simply has to execute the following line...

```
python propublica.py
```. 

By default the script will use a file called `list_of_orgs.csv` from the
current directory as the source of ProPublica numbers. By default, the ouput of
will be stored in a file called `final_data.csv`. However, these default
locations can be changed with the use of the `-i` and `-o` flags respectively,
as shown in the following...

```
python propublica.py -i my_new_list.csv -o some_dir/my_new_output.csv
```

Note that all file paths will be relative to the current working directory.

By default the script will record data for every field currently supported.  If
one would like to record data for only specific fields, one can specify the
desired fields with other args. For example, running `python propublica.py -tr`
will tell the script to only scrape for the total revenue of the given
organizations. For a comprehensive list of options, execute `python
propublica.py -h`

One can test the script by running it with the given example list. Simply run the
following command...

```
python propublica.py -i example_list_of_orgs.csv -o example_final_data.csv
```

Now add the ProPublica numbers of your own orgs to list_of_orgs.csv, or specify
your own files. Have fun scraping!

## About

These script were a part of the Harvard Open Data Project's Final Club Finances
Project. The [Harvard Open Data Project](http://harvard-open-data-project.github.io/),
is a student-faculty collaboration dedicated to opening and analyzing Harvard
data to empower our community members to improve campus life.

##TODO

- Add pictures to 'Getting Started' so that the directions are clearer. 
- Make Error Handling more specific in Main().
- Improve the formatting of incomplete entries.
- Update and integrate Jupyter/iPython notebook for easier prototying.
- Figure out a way to search for orgs without ProPublica numbers.
