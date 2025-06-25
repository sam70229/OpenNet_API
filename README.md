# Testing Target
[API Endpoint](https://thereportoftheweekapi.com/docs#/default/get_api_v1_reports_)

# Positive Test Cases
|Test Cases|
|----------|
|Normal Request without any query params|
|Normal Request with query params|

### Test Steps
|               Steps                   |       Expected Result             |
|---------------------------------------|-----------------------------------|
| Send Get Request to `/api/v1/reports` | Get HTTP Status `200`             |
|       Check Response schema           |  Response should be same as schema|

# Negative Test Cases
|Test Cases|
|----------|
|Unsupported Category|
|Max Rating bigger than 10|
### Test Steps
|               Steps                   |       Expected Result             |
|---------------------------------------|-----------------------------------|
| Send Get Request to `/api/v1/reports` | Get HTTP Status `400`             |
|       Check Response                  |  Response should have error and message|


# Validation
- ### Response
    We save api endpoint's needed data and expected response into json file,

    Each test case has its own json file, so that each test case's data is separated,

    ```json
    // file naming will be using its scenario and keep it short
    // e.g. normal_request.json
    // the data will look like this
    {
        "url": "string",
        "method": "string",
        "response_code": 200,
        "response_body": {},
        "schema" : {} // if test case need to validate schema
    }
    ```

    We can just load test data and use it everywhere when running the test.


- ### Resposne Json Schema
    We validate json response schema with 3rd-party library [jsonschema](https://python-jsonschema.readthedocs.io/en/latest/validate/#)

    with using this library, we can simply define column's type and required keys to check if it is appeared inside response

    ```json
    {
        "type": "object", // dict is an object
        "properties": {
            "parent_key": {
                "type": "array", // use array if this key is an array
                "items": {
                    "type": "object",
                    "properties": {
                        "key_n": "", // keys
                    },
                    "required": ["key_n"]
                }
            }
        },
        "required": ["parent_key"]
    }

    ```
    Note: json types can be found in [here](https://json-schema.org/understanding-json-schema/reference/type).