import sys
import pytest
import requests
from flask import Flask, request, render_template

sys.path.append('../app_flask')

def test_url_up():
    assert requests.get('http://localhost:5000').status_code == 200, "The website is broken :C"
