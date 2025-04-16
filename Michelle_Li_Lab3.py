# CIS-117 Lab 3
# This module reads the country_full.csv file and separates the countries by region, generating one file for each distinct region if the file does not already exist
# Michelle Li

import csv

column_names = ['name', 'region'] # the column info we want to extract
region_name = "region"

# read to file
with open('country_full.csv', mode='r') as read_file:
    csv_reader = csv.DictReader(read_file)

    for row in csv_reader:
        # only make a region file if there is a region listed
        if row[region_name] != '': 
            file_name = f"{row[region_name]}.csv"
        
            list_of_places = []
            # add country and region to list
            for column in column_names:
                list_of_places.append(row[column])
    
            try:
                f = open(file_name)
            except FileNotFoundError as FileNotFoundError:
                print(FileNotFoundError)
            except IOError as IOError:
                print(IOError)
            except PermissionError as PermissionError:
                print(PermissionError)
            except Exception as Exception:
                print(Exception)
            else:
                pass
            
            # write to file
            with open(file_name, mode='a', newline='') as write_file: 
                csv_writer = csv.writer(write_file)
                csv_writer.writerow(list_of_places)
