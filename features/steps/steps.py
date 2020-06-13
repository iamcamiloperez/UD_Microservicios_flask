from behave import *
import requests
import json

@given('a {values} to add')
def step_impl(context, values):
    context.api_url = 'http://localhost:41000/api/sumar'
    context.value = values.split(',')
    print('url :'+context.api_url)

@when('the add the values')
def step_impl(context):    
    print(context.value)
    dataJson = '{"numbers": [{{numbersJson}}]}'
    numbersJson = ""

    for value in context.value:
        numbersJson += '{"number": "' + value + '"},'
    
    numbersJson=numbersJson[:len(numbersJson) - 1]
    dataJson=dataJson.replace("{{numbersJson}}", numbersJson)
    print(dataJson)
    
    response = requests.post(context.api_url, json=json.loads(dataJson))
  
    context.result = json.loads(response.text)['result']

@then('the {total:d} of add is correct')
def step_impl(context, total):
    assert (context.result == total)

@given('a {values} to subtract')
def step_impl(context, values):
    context.api_url = 'http://localhost:41010/api/restar'
    context.value = values.split(',')
    print('url :'+context.api_url)

@when('the subtract the values')
def step_impl(context):    
    print(context.value)
    dataJson = '{"numbers": [{{numbersJson}}]}'
    numbersJson = ""

    for value in context.value:
        numbersJson += '{"number": "' + value + '"},'
    
    numbersJson=numbersJson[:len(numbersJson) - 1]
    dataJson=dataJson.replace("{{numbersJson}}", numbersJson)
    print(dataJson)
    
    response = requests.post(context.api_url, json=json.loads(dataJson))
  
    context.result = json.loads(response.text)['result']

@then('the {total:d} of subtract is correct')
def step_impl(context, total):
    assert (context.result == total)


@given('a {values} to multiply')
def step_impl(context, values):
    context.api_url = 'http://localhost:41020/api/multiplicar'
    context.value = values.split(',')
    print('url :'+context.api_url)

@when('the multiply the values')
def step_impl(context):    
    print(context.value)
    dataJson = '{"numbers": [{{numbersJson}}]}'
    numbersJson = ""

    for value in context.value:
        numbersJson += '{"number": "' + value + '"},'
    
    numbersJson=numbersJson[:len(numbersJson) - 1]
    dataJson=dataJson.replace("{{numbersJson}}", numbersJson)
    print(dataJson)
    
    response = requests.post(context.api_url, json=json.loads(dataJson))
  
    context.result = json.loads(response.text)['result']

@then('the {total:d} of multiply is correct')
def step_impl(context, total):
    assert (context.result == total)

@given('a {values} to divide')
def step_impl(context, values):
    context.api_url = 'http://localhost:41030/api/dividir'
    context.value = values.split(',')
    print('url :'+context.api_url)

@when('the divide the values')
def step_impl(context):    
    print(context.value)
    dataJson = '{"numbers": [{{numbersJson}}]}'
    numbersJson = ""

    for value in context.value:
        numbersJson += '{"number": "' + value + '"},'
    
    numbersJson=numbersJson[:len(numbersJson) - 1]
    dataJson=dataJson.replace("{{numbersJson}}", numbersJson)
    print(dataJson)
    
    response = requests.post(context.api_url, json=json.loads(dataJson))
  
    context.result = json.loads(response.text)['result']

@then('the {total:d} of divide is correct')
def step_impl(context, total):
    assert (context.result == total)
    