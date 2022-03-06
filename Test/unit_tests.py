import sys
import pytest
import requests
from flask import Flask, request, render_template
from model.model_toxicity import detoxify
sys.path.append('../app_flask')

def test_url_up():
    assert requests.get('http://localhost:5000').status_code == 200, "The website is broken :C"
    
def test_model():
    result_model = detoxify('I love you')
    if result_model == "This sentence is not toxic" :
        assert False
    else : assert True
