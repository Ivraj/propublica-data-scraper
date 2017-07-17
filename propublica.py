#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Creates a csv file containing the financial data of specified organizations
using ProPublica.

Inputs:
LIST_OF_ORGS_FILE (the list of propublica numbers)

Output:
final_data.csv (data autograbbed from the API merged with manual data)
"""

from __future__ import print_function
import argparse
import csv
import json
import time
import urllib2

# Specifies deafault file paths
LIST_OF_ORGS_FILE = "list_of_orgs.csv"
OUTPUT_FILE = "final_data.csv"

DESCRIPTION = """
Welcome to the Propublica Data Scraper! 

This is a python script that allows you to programmatically scrape financial
data about non-profits from ProPublica's Non-Profit Explorer.\n 

In order to run this script, one simply has to execute 'python propublica.py'
with the appropriate args. Below is a list of the various arguments one can
pass. One can specify as many as they like. If one would like to run the script with the default settings and collect
all the data possible, simply run 'python propublica.py -a'. Running '-a' will
cause the script to ignore args for other fields.\n 

One can also choose to change the default name or location of the file with the
list of organizations as well as the output file.\n
"""

def get_args():
    """Gets args specified by user"""
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("-i", "--input", help="Will specify the location of "
                        "the file with the list of organzation number. The "
                        "default location is list_of_orgs.csv in the current "
                        "directory", default=LIST_OF_ORGS_FILE)
    parser.add_argument("-o", "--output", help="Will specify the location of "
                        "the output file. Default location is final_data.csv "
                        "in the current directory", default=OUTPUT_FILE)
    parser.add_argument("-tr", "--totalrev", help="Will scrape for Total"
                        "Revenue", action="store_true")
    parser.add_argument("-te", "--totalexp", help="Will scrape for Total"
                        "Expenses", action="store_true")
    parser.add_argument("-ni", "--netinc", help="Will scrape for Net"
                        "Income", action="store_true")
    parser.add_argument("-ta", "--totalass", help="Will scrape for Total"
                        "Assets", action="store_true")
    parser.add_argument("-tl", "--totallia", help="Will scrape for Total"
                        "Liabilities", action="store_true")
    parser.add_argument("-na", "--netass", help="Will scrape for Net"
                        "Assets", action="store_true")
    parser.add_argument("-a", "--all", help="Will scrape for Net"
                        "Assets", default=True, action="store_true")
    args = parser.parse_args()
    if not (args.totalrev or args.totalexp or args.netinc or args.totalass or
            args.totallia or args.netass):
        args.all = True
    return args

def create_header(args):
    """Constructs the header row for the csv"""
    header = ["Propublica Number", "Org Name", "Tax Year", "Data Source",
              "PDF URL"]
    if args.totalrev:
        header.append("Total Revenue")
    if args.totalexp:
        header.append("Total Functional Expenses")
    if args.netinc:
        header.append("Net Income")
    if args.totalass:
        header.append("Total Assets")
    if args.totallia:
        header.append("Total Liabilities")
    if args.netass:
        header.append("Net Assets")
    if args.all:
        header = ["Propublica Number", "Org Name", "Tax Year", "Data Source",
                  "PDF URL", "Total Revenue", "Total Functional Expenses",
                  "Net Income", "Total Assets", "Total Liabilities", "Net"
                  "Assets"]
    return header

def get_list_of_orgs(list_of_orgs_file):
    """Returns list of orgs. Assumes first column is the ProPublica numbers."""
    org_nums = []
    with open(list_of_orgs_file, "r") as csv_file:
        reader = csv.reader(csv_file)
        # Avoid header row
        next(reader)
        for row in reader:
            org_nums.append(row[0])
    return org_nums

def lookup_org(org_num):
    """Looks up org by ProPublica num. Returns json from ProPublica"""
    url = "https://projects.propublica.org/nonprofits/api/v2/organizations/"+org_num+".json"
    org_json = json.loads(urllib2.urlopen(url).read())
    return org_json

def parse_org_data(org_json):
    """Turns json w/org data into dict for csv"""
    org_data = {}
    org_data["official_name"] = org_json["organization"]["name"]
    org_data["pronum"] = org_json["organization"]["id"]
    org_data["filings"] = {}
    for filing in org_json["filings_with_data"]:
        filing_data = {}
        # TODO: Somehow factor out the fields
        # TODO: Make is so it only searchs for fields specified. 
        filing_data["source"] = "Auto"
        filing_data["year"] = filing["tax_prd_yr"]
        filing_data["pdfurl"] = filing["pdf_url"]
        filing_data["totrev"] = filing["totrevenue"]
        filing_data["totexp"] = filing["totfuncexpns"]
        filing_data["netinc"] = filing["totrevenue"] - filing["totfuncexpns"]
        filing_data["totass"] = filing["totassetsend"]
        filing_data["totlia"] = filing["totliabend"]
        filing_data["netass"] = filing["totassetsend"] - filing["totliabend"]
        org_data["filings"][filing_data["year"]] = filing_data
    for filing in org_json["filings_without_data"]:
        filing_data = {}
        filing_data["source"] = "Manual"
        filing_data["year"] = filing["tax_prd_yr"]
        filing_data["pdfurl"] = filing["pdf_url"]
        filing_data["totrev"] = "NA"
        filing_data["totexp"] = "NA"
        filing_data["netinc"] = "NA"
        filing_data["totass"] = "NA"
        filing_data["totlia"] = "NA"
        filing_data["netass"] = "NA"
        org_data["filings"][filing_data["year"]] = filing_data
    return org_data

def write_org_data(org_data, args, write_function):
    """Takes a dict of org filings and writes it to csv"""
    for filing_year in org_data["filings"]:
        write_data = []
        filing_data = org_data["filings"][filing_year]
        write_data.extend([org_data["pronum"], org_data["official_name"],
                           filing_data["year"], filing_data["source"],
                           filing_data["pdfurl"]])
        if args.totalrev:
            write_data.append(filing_data["totrev"])
        if args.totalexp:
            write_data.append(filing_data["totexp"])
        if args.netinc:
            write_data.append(filing_data["netinc"])
        if args.totalass:
            write_data.append(filing_data["totass"])
        if args.totallia:
            write_data.append(filing_data["totlia"])
        if args.netass:
            write_data.append(filing_data["netass"])
        if args.all:
            write_data = ([org_data["pronum"], org_data["official_name"],
                           filing_data["year"], filing_data["source"],
                           filing_data["pdfurl"], filing_data["totrev"],
                           filing_data["totexp"], filing_data["netinc"],
                           filing_data["totass"], filing_data["totlia"],
                           filing_data["netass"]])
        write_function(write_data)

def main():
    """Compiles data into csv file"""
    overall_start_time = time.time()
    print("Starting script...")

    args = get_args()
    header = create_header(args)
    org_nums = get_list_of_orgs(args.input)

    incomplete_data = []

    with open(args.output, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        # TODO: Find a way to better ensure header is synced with manualdata.csv
        writer.writerow(header)

        for org_num in org_nums:
            start_time = time.time()
            try:
                org_json = lookup_org(org_num)
                org_data = parse_org_data(org_json)
                write_org_data(org_data, args, writer.writerow)
            # TODO: Make error handler more specific.
            except Exception as err:
                raise
                error_message = "Error occurred with "+org_num+":"+str(err)
                incomplete_data.append(error_message)
            end_time = time.time()
            print("Completed "+org_data["official_name"]+" in "+
                  str(round((end_time - start_time), 2))+"s")

    overall_end_time = time.time()
    # TODO: Improve formatting of incomplete entries
    print("Incomplete entries:")
    for filing in incomplete_data:
        if filing:
            print(filing)
    print(incomplete_data)
    print ("Total time: "+str(round((overall_end_time - overall_start_time),
                                    2)) + "s")

if __name__ == "__main__":
    main()
