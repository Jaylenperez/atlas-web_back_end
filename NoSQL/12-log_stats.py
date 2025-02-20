#!/usr/bin/env python3
"""Provide stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx

    print(logs.count_documents({}), 'logs')
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        print(f'\tmethod {method}:', logs.count_documents({'method': method}))
    print(logs.count_documents(
        {'method': 'GET', 'path': '/status'}), 'status check')