from django.shortcuts import render
from django.http import HttpResponse
import os

import requests
import json
import pandas as pd

def display_tags(request, api_key = os.environ['CK_API']):
    # ping CK API to retrieve all the tags
    tag_request = requests.get('https://api.convertkit.com/v3/tags?api_key=' + api_key)
    tags = json.loads(tag_request.content.decode(tag_request.encoding))['tags']

    # create a dictionary list with two base cases
    # all: all subscribers, regardless of tags
    # export_all: download all individual tags and the full list
    tagList = [
        {'id': 0,
        'name': 'All subscribers'},
        {'id': 1,
        'name': 'Export all'
        }]
    
    # loop through the tags and populate dictionary list
    [tagList.append({'id': tag['id'], 'name': tag['name']}) for tag in tags]

    return render(request, 'subscriber_export/tag-display.html', {'taglist': tagList})

def json_to_df(sub_data, df, subcol, statuscol):
    """
    Helper function to turn JSON data into data frame.
    """
    try:
        sub_df = pd.DataFrame(sub_data)[subcol]
        sub_df = pd.json_normalize(sub_df)
        # filter for active subscribers only
        sub_df = sub_df[sub_df[statuscol] == 'active']
        df = df.append(sub_df)
        return df
    except:
        raise Exception('No subscribers found!')

def download_tag_subs(request, tag, api_secret = os.environ['CK_SECRET']):
    # ping CK API to retrieve tag data
    tag_sub_request = requests.get('https://api.convertkit.com/v3/tags/' + str(tag) + '/subscriptions?api_secret=' + api_secret)
    tag_sub_data = json.loads(tag_sub_request.content.decode(tag_sub_request.encoding))
    print(tag_sub_data)

    # loop to retrieve all subscribers belonging to the tag
    # this is necessary because the data is paginated, so it only shows 50 entries at a time
    tag_df = pd.DataFrame()
    for i in range(1, tag_sub_data['total_pages']+1):
        # requesting subscriber data from page i
        tag_sub_request = requests.get('https://api.convertkit.com/v3/tags/' + str(tag) + '/subscriptions?api_secret=' + api_secret + '&page=' + str(i))
        tag_sub_data = json.loads(tag_sub_request.content.decode(tag_sub_request.encoding))
        tag_df = json_to_df(tag_sub_data, tag_df, subcol = 'subscriptions', statuscol = 'subscriber.state')
    
    title = ('tag_' + str(tag) + '.csv').replace(' ', '_').replace(':', '').replace('/', '').lower()
    
    # create HttpResponse and add the data to it
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename =' + title},
    )

    tag_df.to_csv(response, index=False)
    
    return response

def download_all_subs(api_secret = os.environ['CK_SECRET']):
    all_request = requests.get('https://api.convertkit.com/v3/subscribers?api_secret=' + api_secret)
    all_subs = json.loads(all_request.content.decode(all_request.encoding))

    all_subs_df = pd.DataFrame()
    for i in range(1, all_subs['total_pages']+1):
        print(i)
        all_sub_request = requests.get('https://api.convertkit.com/v3/subscribers?api_secret=' + api_secret + '&page=' + str(i))
        all_sub_data = json.loads(all_sub_request.content.decode(all_sub_request.encoding))
        all_subs_df = json_to_df(all_sub_data, all_subs_df, subcol = 'subscribers', statuscol = 'state')

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename = "all_subscribers.csv"'},
    )

    all_subs_df.to_csv(response, index=False)
    
    return response