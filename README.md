# GP Python
This app demonstrates using flask as a single file python web api.
## Development 
The app can be run by first installing the dependencies using [Pipenv]
by running `pipenv install` in the application directory. 

Once the dependencies are installed the app can be run in development mode 
by using the flask cli.

1. Windows
    ```bash
    pipenv shell
    set FLASK_APP=app.py; set FLASK_ENV=development; flask run
    ```
2. OSX / Linux
    ```bash
   pipenv shell
   export FLASK_APP=app.py && export FLASK_ENV=development && flask run 
   ```
## Production
A dockerfile is provided which will install the application requirements
as well as the [bjoern] server. The docker container will run the application 
using the bjoern server for faster response times.  

## Tests
Test can be run using the `test.py` file by running `python test.py`.

[Pipenv]:https://github.com/pypa/pipenv
[bjoern]:https://github.com/jonashaag/bjoern