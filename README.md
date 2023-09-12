# The Casting Agency Project with it's API Documentation

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. I'm an Executive Producer within the company and am creating a system to simplify and streamline my process.

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/).

## Getting Started

### Pre-requisites and Local Development

Developers using this project should already have Python3 and pip installed on their local machines.

## Backend

Set up a virtual environment by running this command `python -m venv env`, then to activate the virtual environment by running this command `.\env\Scripts\activate`.  

From the main directory run `pip install -r requirements.txt`. All required packages are included in the requirements.txt file.

To run the application run the following commands:

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
set FLASK_DEBUG=true
flask run --reload
```

The application is running on `http://127.0.0.1:5000/` by default.

### Tests

In order to run tests, open new terminal and make sure you are in the main directory in front of `test
_app.py` file  run the following command:

```bash
python test_app.py
```

All tests are kept in that file and should be maintained as updates are made to app functionality.

## Our Roles

- Casting Assistant
  - Can view actors and movies
  - email: <casting_assistant@gmail.com>
  - password: Testing_1234$
- Casting Director
  - All permissions a Casting Assistant has and…
  - Add or delete an actor from the database
  - Modify actors or movies
  - email: <casting_director@gmail.com>
  - password: Testing_1234$
- Executive Producer
  - All permissions a Casting Director has and…
  - Add or delete a movie from the database
  - email: <executive_producer@gmail.com>
  - password: Testing_1234$

### Auth0 url to login with the pervious emails to generate the token for each role

```bash
https://dev-8npu8gdx5eo4rogq.us.auth0.com/authorize?
  audience=agency&
  response_type=token&
  client_id=Fm6abzxDrnUfYvG61vdm0kWxcFlfbJ9P&
  redirect_uri=https://127.0.0.1:8080/login-results
```

## API Reference

### Getting Started with API Documentation

- Base URL: This app can only be run locally and globally. The backend app is hosted at the URL, `http://127.0.0.1:5000/`.
- Authentication: This version of the application equires authentication.

### Error Handling

Errors are returned as JSON objects in the following format:

```bash
{
  "success": False, 
  "error": 400,
  "message": "bad request"
}
```

The API will return four error types when requests fail:

- 400: Bad Request
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable

### Endpoints

#### GET /actors

- General:
  - Returns a list of actors objects, success value and total actors.
  
- Sample: `curl http://127.0.0.1:5000/actors`

```json
{
  "actors": [
    {
      "age": 32,
      "gender": "male",
      "id": 1,
      "name": "John Doe"
    },
    {
      "age": 45,
      "gender": "male",
      "id": 2,
      "name": "Tom Corose"
    },
    {
      "age": 65,
      "gender": "male",
      "id": 3,
      "name": "Adam Sandler"
    },
    {
      "age": 55,
      "gender": "female",
      "id": 4,
      "name": "Nicole Kidman"
    },
    {
      "age": 73,
      "gender": "female",
      "id": 5,
      "name": "Meryl Streep"
    },
    {
      "age": 42,
      "gender": "female",
      "id": 6,
      "name": "Jessica Alba"
    },
    {
      "age": 45,
      "gender": "male",
      "id": 8,
      "name": "Tom Hardy"
    }
  ],
  "success": true,
  "total_actors": 7
}
```

#### GET /actors/{actor_id}

- General:
  - Returns a specific actor and success value.
  
- Sample: `curl http://127.0.0.1:5000/actors/1`

```json
{
  "actor": {
    "age": 32,
    "gender": "male",
    "id": 1,
    "name": "John Doe"
  },
  "success": true
}
```

#### POST /actors

- General:
  - Creating a new actor.

  - Returns a list of actors, the Id of the created actor, success value and total actors.

- `curl -X POST -H "Content-Type: application/json" -d "{\"age\": 18, "gender\": \"male\", \"name\":\"John Mark\"}" /actors`

```json
{
  "actors": [
    {
      "age": 32,
      "gender": "male",
      "id": 1,
      "name": "John Doe"
    },
    {
      "age": 45,
      "gender": "male",
      "id": 2,
      "name": "Tom Corose"
    },
    {
      "age": 65,
      "gender": "male",
      "id": 3,
      "name": "Adam Sandler"
    },
    {
      "age": 55,
      "gender": "female",
      "id": 4,
      "name": "Nicole Kidman"
    },
    {
      "age": 73,
      "gender": "female",
      "id": 5,
      "name": "Meryl Streep"
    },
    {
      "age": 42,
      "gender": "female",
      "id": 6,
      "name": "Jessica Alba"
    },
    {
      "age": 45,
      "gender": "male",
      "id": 8,
      "name": "Tom Hardy"
    },
    {
      "age": 18,
      "gender": "male",
      "id": 12,
      "name": "John Mark"
    }
  ],
  "created": 12,
  "success": true,
  "total_actors": 8
}
```

#### PATCH /actors/{actor_id}

- General:
  - Updating a specific actor.

  - Returns the id of the updated actor and success value.

- `curl -X PATCH -H "Content-Type: application/json" -d "{\"age\": 20, "gender\": \"male\", \"name\":\"John Mark\"}"" http://127.0.0.1:5000/actors/12`

```json
{
  "id": 12,
  "success": true
}
```

#### DELETE /actors/{actor_id}

- General:
  - Deletes a specific actor of the given Id if it exists.

  - Returns the id of the deleted actor, success value, total actors, and actors list.

- `curl -X DELETE http://127.0.0.1:5000/actors/12`

```json
{
  "actors": [
    {
      "age": 32,
      "gender": "male",
      "id": 1,
      "name": "John Doe"
    },
    {
      "age": 45,
      "gender": "male",
      "id": 2,
      "name": "Tom Corose"
    },
    {
      "age": 65,
      "gender": "male",
      "id": 3,
      "name": "Adam Sandler"
    },
    {
      "age": 55,
      "gender": "female",
      "id": 4,
      "name": "Nicole Kidman"
    },
    {
      "age": 73,
      "gender": "female",
      "id": 5,
      "name": "Meryl Streep"
    },
    {
      "age": 42,
      "gender": "female",
      "id": 6,
      "name": "Jessica Alba"
    },
    {
      "age": 45,
      "gender": "male",
      "id": 8,
      "name": "Tom Hardy"
    }
  ],
  "deleted": 12,
  "success": true,
  "total_actors": 7
}
```

#### GET /movies

- General:
  - Returns a list of movies objects, success value and total movies.
  
- Sample: `curl http://127.0.0.1:5000/movies`

```json
{
  "movies": [
    {
      "actors": [
        "Meryl Streep",
        "Jessica Alba"
      ],
      "id": 1,
      "release_date": "Wed, 20 Sep 2023 00:00:00 GMT",
      "title": "Updated Movie Title"
    },
    {
      "actors": [
        "Jessica Alba",
        "Adam Sandler"
      ],
      "id": 2,
      "release_date": "Wed, 20 Sep 2023 00:00:00 GMT",
      "title": "Updated Movie2 Title"
    },
    {
      "actors": [],
      "id": 3,
      "release_date": "Mon, 11 Sep 2023 00:00:00 GMT",
      "title": "Updated Example3 Movie"
    }
  ],
  "success": true,
  "total_movies": 3
}
```

#### GET /movies/{movie_id}

- General:
  - Returns a specific movie and success value.
  
- Sample: `curl http://127.0.0.1:5000/movies/1`

```json
{
  "movie": {
    "actors": [
      "Meryl Streep",
      "Jessica Alba"
    ],
    "id": 1,
    "release_date": "Wed, 20 Sep 2023 00:00:00 GMT",
    "title": "Updated Movie Title"
  },
  "success": true
}
```

#### POST /movies

- General:
  - Creating a new movie.

  - Returns a list of movies, the Id of the created movie, success value and total movies.

- `curl -X POST -H "Content-Type: application/json" -d "{
    \"actors\": [
      \"Meryl Streep\",
      \"Jessica Alba\"
    ],
    \"release_date\": \"Wed, 20 Sep 2023 00:00:00 GMT\",
    \"title\": \"New Movie Title\"
}" /movies`

```json
{
  "created": 6,
  "movies": [
    {
      "actors": [
        "Meryl Streep",
        "Jessica Alba"
      ],
      "id": 1,
      "release_date": "Wed, 20 Sep 2023 00:00:00 GMT",
      "title": "Updated Movie Title"
    },
    {
      "actors": [
        "Jessica Alba",
        "Adam Sandler"
      ],
      "id": 2,
      "release_date": "Wed, 20 Sep 2023 00:00:00 GMT",
      "title": "Updated Movie2 Title"
    },
    {
      "actors": [],
      "id": 3,
      "release_date": "Mon, 11 Sep 2023 00:00:00 GMT",
      "title": "Updated Example3 Movie"
    },
    {
      "actors": [],
      "id": 6,
      "release_date": "Wed, 20 Sep 2023 00:00:00 GMT",
      "title": "New Movie Title"
    }
  ],
  "success": true,
  "total_movies": 4
}
```

#### PATCH /movies/{movie_id}

- General:
  - Updating a specific movie.

  - Returns the id of the updated movie and success value.

- `curl -X PATCH -H "Content-Type: application/json" -d ""{
    \"actors\": [
      \"Meryl Streep\",
      \"Jessica Alba\"
    ],
    \"release_date\": \"Wed, 20 Sep 2023 00:00:00 GMT\",
    \"title\": \"Updated New Movie Title\"
}" /movies/6`

```json
{
  "id": 6,
  "success": true
}
```

#### DELETE /movies/{movie_id}

- General:
  - Deletes a specific movie of the given Id if it exists.

  - Returns the id of the deleted movie, success value, total movies, and movies list.

- `curl -X DELETE http://127.0.0.1:5000/movies/6`

```json
{
  "deleted": 6,
  "movies": [
    {
      "actors": [
        "Meryl Streep",
        "Jessica Alba"
      ],
      "id": 1,
      "release_date": "Wed, 20 Sep 2023 00:00:00 GMT",
      "title": "Updated Movie Title"
    },
    {
      "actors": [
        "Jessica Alba",
        "Adam Sandler"
      ],
      "id": 2,
      "release_date": "Wed, 20 Sep 2023 00:00:00 GMT",
      "title": "Updated Movie2 Title"
    },
    {
      "actors": [],
      "id": 3,
      "release_date": "Mon, 11 Sep 2023 00:00:00 GMT",
      "title": "Updated Example3 Movie"
    }
  ],
  "success": true,
  "total_movies": 3
}
```

## Deployment N/A

## Authors

Yours truly, Software Developer Muhammad Galhoum

## Acknowledgements N/A
