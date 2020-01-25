#!/usr/bin/env python3
import cgi, cgitb
cgitb.enable()
import os

print("Content-Type: text/html\n")
print()
print("<!doctype html><title>Hello</title><h1>Hello World</h1>")
print("Q1-------")
print("<div><p>")
print(os.environ)
print("</p></div>")
print("Q2-------")
print("<div><p>")
print(os.environ["QUERY_STRING"])
print("</p></div>")
print("Q3-------")
print("<div><p>")
print(os.environ["HTTP_USER_AGENT"])
print("</p></div>")
