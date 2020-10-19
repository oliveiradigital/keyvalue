# Key Value API

This project allow you to run a API to store values by key.

You can subscribe and create account with no data with: `curl -X POST https://keyvalue.oliveiradigital.com.br/accounts/user/`. This will return a Token to be used on the system.

## Store and get values

### Store value

`curl -X POST https://keyvalue.oliveiradigital.com.br/data/<key> -d "value=Somevalueasstringhere"`.

At this point, the value sent as POST, will be available on `<key>`. To retrieve:

### Get value

`curl -X GET https://keyvalue.oliveiradigital.com.br/data/<key>`. This will return the value like: `{success: True, value: "Somevalueasstringhere"}`.