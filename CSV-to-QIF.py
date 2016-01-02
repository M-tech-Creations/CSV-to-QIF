#**************************************************************************/
#
#    @file    CSV_to_QIF.py
#    @author   Mario Avenoso (M-tech Creations)
#    @license  MIT (see license.txt)
#
#    Program to convert from a CSV to a QIF file using a definitions
#    to describe how the CSV is formatted
#
#    @section  HISTORY
#
#    v0.1 - First release 1/1/2016 beta release
#
#**************************************************************************/


import os
import sys
import re
import csv

#
#     @brief  Takes given CSV and parses it to be exported to a QIF
#
#     @params[in] inf_
#     File to be read and converted to QIF
#     @params[in] outf_
#     File that the converted data will go
#     @params[in] deff_
#     File with the settings for converting CSV
#
#
def readCsv(inf_,outf_,deff_): #will need to receive input csv and def file

    csvdeff = csv.reader(deff_, delimiter=',')

    next(csvdeff,None)



    for settings in csvdeff:
        date_= int(settings[0])  #convert to int
        amount_ = int(settings[2])  #How much was the transaction
        memo_ = int(settings[3])  #discription of the transaction
        payee_ = int(settings[4])  #Where the money is going
        deli_ = settings[5] #How the csv is separated
        header_ = int(settings[6])  #Set if there is a header to skip

    csvIn = csv.reader(inf_, delimiter=deli_)  #create csv object using the given separator

    if header_ >= 1: #If there is a header skip the fist line
        next(csvIn,None)  #skip header

    for row in csvIn:
        writeFile(row[date_],row[amount_],row[memo_],row[payee_],outf_)  #export each row as a qif entry





#
#     @brief Receives data to be written to and its location
#
#     @params[in] date_
#     Data of transaction
#     @params[in] amount_
#     Amount of money for transaction
#     @params[in] memo_
#     Description of transaction
#     @params[in] payee_
#     Transaction paid to
#     @params[in] filelocation_
#     Location of the Output file
#
#
# https://en.wikipedia.org/wiki/Quicken_Interchange_Format
#
def writeFile(date_,amount_,memo_,payee_, filelocation_):
    outFile = open(filelocation_,"a")  #Open file to be appended
    outFile.write("!Type:Cash\n")  #Header of transaction, Currently all set to cash
    outFile.write("D")  #Date line starts with the capital D
    outFile.write(date_)
    outFile.write("\n")

    outFile.write("T")  #Transaction amount starts here
    outFile.write(amount_)
    outFile.write("\n")

    outFile.write("M")  #Memo Line
    outFile.write(memo_)
    outFile.write("\n")

    outFile.write("P")  #Payee line
    outFile.write(payee_)
    outFile.write("\n")

    outFile.write("^\n")  #The last line of each transaction starts with a Caret to mark the end
    outFile.close()
def convert():


     error = 'Input error!____ Format [import.csv] [output.csv] [import.def] ____\n\n\
                 [import.csv] = File to be converted\n\
                 [output.qif] = File to be created\n\
                 [import.def] = Definition file describing csv file\n'

     if (len(sys.argv) != 4):  #Check to make sure all the parameters are there
            print error
            exit(1)

     if os.path.isfile(sys.argv[1]):
         fromfile = open(sys.argv[1],'r')
     else:
         print '\nInput error!____ import.csv: ' + sys.argv[1] + ' does not exist / cannot be opened !!\n'
         exit(1)

     try:
         tofile   = open(sys.argv[2],'a')
     except:
         print '\nInput error!____ output.csv: ' + sys.argv[2] + ' cannot be created !!\n'
         exit(1)

     if os.path.isfile(sys.argv[3]):
         deffile = open(sys.argv[3],'r')
     else:
         print '\nInput error!____ import.def: ' + sys.argv[3] + ' does not exist / cannot be opened !!\n'
         exit(1)

     tofile = sys.argv[2]
     readCsv(fromfile,tofile,deffile)

     fromfile.close()
     deffile.close()



convert()#Start