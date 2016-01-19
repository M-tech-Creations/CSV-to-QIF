#CSV to QIF Converter#

This is a Python program to take a CSV file and convert it to a QIF file. QIF is an 
open specification for reading and writing financial data. This is a working Beta release.
Find my wirte up Here
    ------> http://mario.mtechcreations.com/programing/csv-to-qif-python-converter/

## About this Program ##

The way you use the converter is by passing it a file to convert, the file name and path
to convert to and the definition file describing the csv file. 

## Exaple Usage and File ##

Example of converting a file stored in the same directory as the program.

python CSV-to-QIF.py [file-to-convert.csv] [export-file.qif] [csv-discription.def]

The definition file is a csv that is setup with the properties of the csv to convert.
The format is as follows (also see the example .def file)

Date,Date Format,Amount,Memo,Payee,Separator,Header
0,not used,4,1,2,",",0

The first row, or header, lists the type of information the converter is going to use to create the QIF file. 
The second row has the cell number (starting at 0) of the requested data from the CSV file to be converted. 
Meaning if the transaction amount is in the first cell you would put a 0 under amount. 

Currently the date format cell does not do anything, the means that in order for the QIF to be valid, the date in 
the CSV needs to be in MM/DD/YYYY format. This is a feature I hope to implement in the future.

The Payee cell is used to mark the Payeee. If there is no Payee use -1 to ignore it.

There are two other cell’s to make note of, Separator and Header.  Separator refers to how the file is separated. 
CSV files can be split in different ways,  with the two most common being a semicolon or a comma. 
In this field place the type of Separator used (ie. “;”). The header cell is used to tell the program 
if it needs to skip the first row or not. Most times this first row just holds the names of each column and 
needs to be skipped. If so Place a 1 in the cell, otherwise place a 0.


Written by Mario Avenoso of mtechcreations.com
MIT license, check license.txt for more information


## Wish List ##

Add option for reconciling transactions
