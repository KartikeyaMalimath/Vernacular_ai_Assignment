# Vernacular_ai_Assignment
Vernacular.ai Interview Assignment - Kartikeya P Malimath

## Docker

The Django app has been developed with Dockefile

Size of the Docker file is 132kB
Size of the docker image is approximately **982 MB**

* **Steps :**

1. Download the project file and cd into the project directory **km_vernaculalrai**
2. Run the below commands
    * ``` docker-compose build ```
3. Post building of docker-image run the below command to run the image
    * ``` docker-compose up ```

The docker image runs on port 8000

## Django REST APIs

1. **POST API to validate a slot with a finite set of values**

* ``` http://localhost:8080/vernacular/fvalues ```

2. **POST API to validate a slot with a numeric value extracted and constraints on the value extracted**

* ``` http://localhost:8080/vernacular/nconstraints ```


### 1. API - 1 
* Sample Request
```
{
  "invalid_trigger": "invalid_ids_stated",
  "key": "ids_stated",
  "name": "govt_id",
  "reuse": true,
  "support_multiple": true,
  "pick_first": false,
  "supported_values": [
    "pan",
    "aadhaar",
    "college",
    "corporate",
    "dl",
    "voter",
    "passport",
    "local"
  ],
  "type": [
    "id"
  ],
  "validation_parser": "finite_values_entity",
  "values": [
    {
      "entity_type": "id",
      "value": "college"
    }
  ]
}
```

* Sample Response
```
{
    "filled": true,
    "partially_filled": false,
    "trigger": '',
    "parameters": {
        "ids_stated": ["COLLEGE"]
    }
}
```

### 2. API - 2

* Sample Request
```
{
  "invalid_trigger": "invalid_age_stated",
  "key": "age_stated",
  "name": "age",
  "reuse": true,
  "pick_first": true,
  "type": [
    "number"
  ],
  "validation_parser": "numeric_values_entity",
  "constraint": "x>=18 and x<=30",
  "var_name": "x",
  "values": [
    {
      "entity_type": "number",
      "value": 23
    }
  ]
}
```

* Sample Response

```
{
    "filled": true,
    "partially_filled": false,
    "trigger": '',
    "parameters": {
        "age_stated": 23
    }
}
```

## Built with :heart: by Kartikeya P. Malimath
