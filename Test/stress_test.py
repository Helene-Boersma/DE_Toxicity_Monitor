import requests
import time
from flask import Flask, request, render_template
import pytest

def test_stress_requests():
    start = time.time()
    for i in range(1000):
        requests.get("http://localhost:5000")

    end = time.time() - start
    assert (end / 1000) < 100, "stress not passed"