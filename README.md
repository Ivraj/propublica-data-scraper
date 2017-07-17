# Harvard Open Data Project: Propublica Data Scraper

## Overview

The Propublica Data Scraper is a python script that automates the collection of
non-profit financial data using the Propublica API. 

Currently the script, by default, extracts data based on a list of organzations
in a file called `list_of_orgs.csv`. Organizations are queried based off of
their ProPublica number, which can be found the the ProPublica Non-Profit
Explorer.

Due to speed of ProPublica's API, each organization will take around 2-5
seconds resulting in a total of a couple of minutes depending on the number of
organizations you input. The results will, by default, be stored in a file
called `final_data.csv`. 

To find out more, check out [Propublica's Nonprofit Explorer API](https://projects.propublica.org/nonprofits/api)

## Getting started

Once you've downloaded this directory, you simply need to populate the
list_of_orgs.csv file with the ProPublica numbers of your desired
organizations.  To obtain the ProPublica number, you must search for the
desired non-profit in ProPublica's Non-Profit Explorer, go to the page for the
desired org, and then copy down the number at the end of the url.  For example,
Oxfam-America Inc.'s number is 237069110. The Non-Profit Explorer can be found
[here](https://projects.propublica.org/nonprofits/). 

Once that's done, you can run the script by simply executing the following line...

```
python propublica.py
``` 

By default the script will use a file called `list_of_orgs.csv` from the
current working directory as the source of ProPublica numbers. By default, the
ouput of will be stored in a file called `final_data.csv` in the current
working directory. However, these default locations can be changed with the use
of the `-i` and `-o` flags respectively, as shown in the following...

```
python propublica.py -i my_new_list.csv -o some_dir/my_new_output.csv
```

Note that all file paths will be relative to the current working directory.

By default the script will record data for every field currently supported.  If
you'd like to record data for only specific fields, you can specify the desired
fields with other args. For example, running `python propublica.py -tr` will
tell the script to only scrape for the total revenue of the given
organizations. For a comprehensive list of field options, execute `python
propublica.py -h`

One can test the script by running it with the example list included in this
directory. Simply run the following command...

```
python propublica.py -i example_list_of_orgs.csv -o example_final_data.csv
```

If the script runs without error, you should have a file called
`example_final_data.csv` populated with the financial data of Oxfam-America,
the American Red Cross, and Amnesty International-USA.  

Now add the ProPublica numbers of your own orgs to list_of_orgs.csv, or specify
your own files. Have fun scraping!

## About

These script were a part of the Harvard Open Data Project's Final Club Finances
Project. The [Harvard Open Data Project](http://harvard-open-data-project.github.io/),
is a student-faculty collaboration dedicated to opening and analyzing Harvard
data to empower our community members to improve campus life.

## TODO

- Add pictures to 'Getting Started' so that the directions are clearer. 
- Make Error Handling more specific in Main().
- Improve the formatting of incomplete entries.
- Update and integrate Jupyter/iPython notebook for easier prototying.
- Figure out a way to search for orgs without ProPublica numbers.
