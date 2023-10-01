"""
blocklist.py

This file just contains the blocklist of the JWT tokens. It will be imported by
app and the logout resource so that tokens can be added to the blocklist when the
user logs out.

figure out how to use redis to store my blocklist
"""

BLOCKLIST = set()