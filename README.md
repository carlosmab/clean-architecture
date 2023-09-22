# Rentomatic

A demo implementation of a clean architecture in Python.

The goal of the "Rent-o-Matic" project is to create a simple search engine for a room renting company. Objects in the dataset (rooms) are described by some attributes and the search engine shall allow the user to set some filters to narrow the search. The system exposes a REST API and works with three types of storage system: in-memory database, Postgres, MongoDB.

This is a companion repository for the book "Clean Architectures in Python" by Leonardo Giordani, published by Leanpub.

You can download the book [here](https://leanpub.com/clean-architectures-in-python).

The repository contains the **code for the second edition** of the book. If for some reasons you are still following the first edition you can find the code in the branch `first-edition`. The tags mentioned in the first edition still exists in that branch.

## Configure test environment

- In terminal use "python -m pytest"
  - In VS code Testing extension
    - Create .env file in root folder with PYTHONPATH (root folder path) var
    - Modify .vscode/settings.json file

      ```
        {
          "python.testing.pytestArgs": [
            "-svv"
          ],
          "python.testing.unittestEnabled": false,
          "python.testing.pytestEnabled": true,
          "python.envFile": "${workspaceFolder}/.env"
        }
      ```

## Implementation

  1. Implementing Domain
      Domain: "Business language reflect in code"
      using dataclass and json.JSONEncoder

      1.1 Entities
        - Test if Room object can be created
        - Test if Room object can be created from dictionary
        - Test if dict can be created from Room object
        - Test if Room object can json serialized

  2. Implementing Use Cases
      Using pytest.fixture and unittest.mock
      2.1 List
        - Test if room's list can be retrieved

  3. Implementing Repository
      3.1 Repo list
        - Test if repo returns data as a list of Rooms

  4. Implementing HTTP endpoint
      4.1 Get room list
        - Test if endpoint returns a list of Rooms

      4.2 Creating WSGI
        - wsgi.py
