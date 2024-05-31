# Scenarize with python and yaml

## Some history

During my year in escape game development I built a system with a scenario for the game master that could get data from the different electronic puzzles around the room and pilot them in a friendly way. unfortunately, leaving this industry cut on the time I could work on it.

Recently I was working on some unit testing for an on premise gitlab and got the idea that it would be nice to find a way to be able to create different scenarios for my tests and even allow some less technical people manage the scenarios.

Getting my inspiration from the .gitlab-ci.yml and some plugin work I did earlier, I narrowed it to this current version. The actions available are really basic and serve as example more thant aynthing else as my work on gitlab cannot really be shared at the moment.

I plan to later on develop the action catalog and I am always open to suggestion for new actions or improvment.


## How the example work

Basicaly you will write a yaml file like the following then run the program.
Each action is a python class than you can use independantly.

``` yaml
variables:
  API_URL: "https://dummyjson.com/"
  DEBUG_MODE: True

actions:
  - fetch_data: # will load fake data from dummyjson about a product and save it in var1
    params:
      api_call: "products/1"
    artifact: 
      var1:
        - data
  - process_data: # will fetch id title and brand from the data and store them in the variable var2
    params:
      data: "$var1.data"
    artifact: 
      var2:
        - id
        - title
        - brand
  - save_data_to_file: # will save the whole content of var2 in a file
    params:
      data: "$var2"
      file_name: "output.json"
```

This simple example will gather some data, process them and save them


# how to run the example

Create a python virtual environement
> python -m virtualenv .

Activate it (example on windows)
>./Scripts/activate

Install yaml module
> pip install PyYAML

Install requests module
> pip install requests

Run the program
> python.exe .\scenarize.py