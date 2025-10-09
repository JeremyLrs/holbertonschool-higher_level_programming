#!/usr/bin/python3

import requests
import csv

'''
task_02_request.py
Data from an API using Python
'''


def fetch_and_print_posts():
    '''
    fetch_and_print_posts - Fetch and print posts
    Return: Void
    '''
    req = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code:", req.status_code)
    if req.status_code == 200:
        data = req.json()
        for i in data:
            print(i['title'])
    else:
        print("Failed to fetch data")


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        posts_data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_data)

        print("Posts saved to posts.csv")
    else:
        print("Failed to fetch posts")
