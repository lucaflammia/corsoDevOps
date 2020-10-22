from behave import *
import requests

@given('build e run del container avviato')
def step_impl(context):
    pass

@when("chiamiamo con una get l'endpoint /")
def step_impl(context):
    url = 'http://localhost/'
    res = requests.get(url)
    assert res.status_code == 200

@then("l'api ci saluta correttamente")
def step_impl(context):
    url = 'http://localhost/'
    res = requests.get(url)
    expected = {'hello': 'DevOps'}
    assert expected == res.json()