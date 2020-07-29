# Vernacular_ai_Assignment
Vernacular.ai Interview Assignment - Kartikeya P Malimath

## Docker

The Django app has been developed with Dockefile

Size of the Docker file is 132kB
Size of the docker image is approximately **982 MB**

* **Steps :**

1. Download the project file and cd into the project directory **km_vernaculalrai**
2. Run the below commands
    ``` docker-compose build ```
3. Post building of docker-image run the below command to run the image
    ``` docker-compose up ```

The docker image runs on port 8000

## Django REST APIs

1. **POST API to validate a slot with a finite set of values**

* ``` http://localhost:8080/vernacular/fvalues ```

2. **POST API to validate a slot with a numeric value extracted and constraints on the value extracted**

* ``` http://localhost:8080/vernacular/nconstraints ```


### Built with :heart: by Kartikeya P. Malimath
