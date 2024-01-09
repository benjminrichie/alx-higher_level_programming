#!/usr/bin/python3
"""This func defines a string-to-JSON"""
import json


def to_json_string(my_obj):
    """to return the JSON representation of a string object."""
    return json.dumps(my_obj)
