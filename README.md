# swagger_client
Unofficial RepositPower External API This API is built by hand from the description at https://api.repositpower.com/docs/ It should not be mistaken for official in any way shape or form, it's simply my attempt to document the API and build some client libraries from that.  This API is demonstrably wrong around authentication - please read the official docco at the link above for accurate details. It will login, but all the login options are not captured - I wasn't clear how to write up both basic and token login being available on all URLs (ie. how to make auth an either/or rather than a both).  This API is also not completed yet. I've note tested a bunch of 200 responses, and some that I have don't have accurate enums in them because I don't know all the possible values. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'
# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # return access token upon successful basic auth
    api_response = api_instance.auth_login_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->auth_login_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.repositpower.com/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**auth_login_get**](docs/DefaultApi.md#auth_login_get) | **GET** /auth/login | return access token upon successful basic auth
*DefaultApi* | [**auth_login_post**](docs/DefaultApi.md#auth_login_post) | **POST** /auth/login | return access token (session id) upon successful basic or html auth (use username/password, or use basic auth) 
*DefaultApi* | [**auth_logout_get**](docs/DefaultApi.md#auth_logout_get) | **GET** /auth/logout | de-authenticate the token (always returns success)
*DefaultApi* | [**deployments_userkey_battery_capacity_get**](docs/DefaultApi.md#deployments_userkey_battery_capacity_get) | **GET** /deployments/{userkey}/battery/capacity | battery capacity in kWh
*DefaultApi* | [**deployments_userkey_battery_historical_soc_get**](docs/DefaultApi.md#deployments_userkey_battery_historical_soc_get) | **GET** /deployments/{userkey}/battery/historical/soc | state of charge of a battery in kWh
*DefaultApi* | [**deployments_userkey_components_get**](docs/DefaultApi.md#deployments_userkey_components_get) | **GET** /deployments/{userkey}/components | installed components and their overall status
*DefaultApi* | [**deployments_userkey_cost_historical_get**](docs/DefaultApi.md#deployments_userkey_cost_historical_get) | **GET** /deployments/{userkey}/cost/historical | energy cost in $
*DefaultApi* | [**deployments_userkey_generation_historical_p_get**](docs/DefaultApi.md#deployments_userkey_generation_historical_p_get) | **GET** /deployments/{userkey}/generation/historical/p | solar generation data as negative real_power in kW
*DefaultApi* | [**deployments_userkey_gridcredits_historical_get**](docs/DefaultApi.md#deployments_userkey_gridcredits_historical_get) | **GET** /deployments/{userkey}/gridcredits/historical | earned gridcredits
*DefaultApi* | [**deployments_userkey_house_historical_get**](docs/DefaultApi.md#deployments_userkey_house_historical_get) | **GET** /deployments/{userkey}/house/historical | house consumption in kW
*DefaultApi* | [**deployments_userkey_inverter_historical_p_get**](docs/DefaultApi.md#deployments_userkey_inverter_historical_p_get) | **GET** /deployments/{userkey}/inverter/historical/p | the battery inverter data as real_power in kW
*DefaultApi* | [**deployments_userkey_meter_historical_p_get**](docs/DefaultApi.md#deployments_userkey_meter_historical_p_get) | **GET** /deployments/{userkey}/meter/historical/p | real power measurements in kW at the grid connection
*DefaultApi* | [**userkeys_get**](docs/DefaultApi.md#userkeys_get) | **GET** /userkeys/ | all userkeys/battery system identifiers for the current user


## Documentation For Models

 - [AuthParams](docs/AuthParams.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2003Data](docs/InlineResponse2003Data.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [TimestampMeter](docs/TimestampMeter.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

## basic

- **Type**: HTTP basic authentication


## Author

kevin@littlejohn.id.au

