# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 16:29:05 2025

Generate the MyST Markdown formatted cards from the community member data on
PFHub (_data/community.yaml)

@author: Phil Staublin
"""

import yaml

with open("_data/community.yaml", "r") as f:
    community_members = yaml.safe_load(f)

print("::::{grid}")
print(":gutter: 3")

for member in community_members:
    if member is None or "name" not in member.keys():
        print("!!!!!! Incorrectly formatted member !!!!!!")
        print(member)
        continue
    if "home" in member.keys() and member['home'] is not None:
        home = member['home']
    else:
        home = "https://github.com/usnistgov/pfhub"
    print(":::{{grid-item-card}} [{:s}]({:s})".format(member['name'], home))
    print(":img-top: {:s}".format(member['avatar']))
    print("{:s}".format(member['text']))
    print("+++")
    # Check each optional included link, and create the clickable icons
    if "email" in member.keys():
        print('<a href="mailto:{:s}'.format(member['email']))
        print('   target="blank_"')
        print('   title="email">')
        print('   <i class="small material-icons">')
        print('     email')
        print('   </i>')
        print('</a>"')
    print(":::\n")

print("::::")
