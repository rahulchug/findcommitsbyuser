#!/usr/bin/env python3

import os
import requests
import json
import pandas as pd
import datetime as dt
import numpy as np

username = ''
token = ''

# function to get user input from the terminal to capture Github Username and Token
def getUserInput():

    global username # global variable
    global token    # global variable

    while True:
        try:
            username = input("Enter the github username: ")
            if len(username) == 0:
                raise Exception("Username cannot be empty")
        except: 
            print(" Username cannot be empty, Please re-enter username ")
            continue
        else:
            break

    while True:
        try:
            token = input("Enter the GitHub token: " )
            if len(token) == 0:
                raise Exception("Token cannot be empty")
        except: 
            print("Token cannot be empty, Please re-enter Token ")
            continue
        else:
            break


def getcommits():

    # **Note:** - please note that using the PAT (personal access token) you can make 30 calls in a minute
    #link - https://docs.github.com/en/rest/reference/search#search-commits
    # Setting headers and preparing the API call params to get Commits by the user 
    headers = {
    'user-agent': 'someagent_to_uniquely_identify_you',
    'accept': 'application/vnd.github.cloak-preview', # gave me a hard time since this is a preview and I somehow missed this (small text) on Github API documentation
    'Content-Type': 'application/json',
    }

    params = (
        ('access_token', token),
        ('q', 'committer:' + username),
        ('sort', 'committer-date'),
        ('order', 'desc'),
        ('per_page', 60),               # setting it to 60
    )
    
    response = requests.get('https://api.github.com/search/commits', headers=headers, params=params)
    
    try:        
        if response is not None and response != '':
           data = response.json()
           
        if data['items'] is not None:
           return data
    except: 
        print('Response object from Github is empty')
        raise ValueError('Response object from Github is empty, please double check the username and token ')

'''
    Write the date records to csv, some file operations over here.
    To make life easy, I used panda dataframe
'''
def writetocsv(data):
    records = []
    
    try:
        for d in data['items']:
            datefromcommit = d['commit']['committer']['date']
            records.append(datefromcommit) # appending to the list  
        #print(records)
        time_pd = pd.to_datetime(records)                   # converting list to pandadatetimelist    
        time_np = time_pd.astype(np.int64)                  # converting to integer
        average_time_np = np.mean(time_np)                  # finding mean in the datatest
        average_time_pd = pd.to_datetime(average_time_np)   # converting back to the time

        #wrting the csv file with header row names as 'Commit Time'
        dir_path = os.path.dirname(os.path.realpath(__file__))
        pd.DataFrame(records,columns=['Commit Time']).to_csv( os.path.join(dir_path, "commitdates.csv"),index=False)
        print('The mean time of commits by user ' + username + ' is: ' + str(average_time_pd))
    except:
        print(' some issue occurred ')    


# Start of sequence
getUserInput()
data = getcommits()
writetocsv(data)