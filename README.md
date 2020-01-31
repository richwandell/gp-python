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
using the bjoern server for faster response times. A docker compose file is 
provided which can be used to map the containers port 80 to the host port 8080 by 
running `docker-compose up`.

## Tests
Test are created for each flask route using the python `unittest` package.
A `setUp` method is used to create a mock flask client and configure flask for testing.
```python
    def setUp(self) -> None:
        app.config['TESTING'] = True
        with app.test_client() as client:
            self.client = client
```
Tests call the flask routes using parameters.
```python
    def test_multiply(self):
        res: Response = self.client.get("/multiply/5/5")
        self.assertEqual(25, int(res.get_data()))
```
 
Test can be run using the `test.py` file by running `python test.py`.

## Routes
* /multiply/\<int:num1>/\<int:num2> - Multiplies two numbers and returns the result.
* /display - Displays static text
* /display/\<sometext> - Displays the text passed as a route parameter.
* /getjson - Displays a dictionary as a JSONApi response. 
 

[Pipenv]:https://github.com/pypa/pipenv
[bjoern]:https://github.com/jonashaag/bjoern