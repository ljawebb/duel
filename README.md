# Duel Candidate Take-Home Task

Welcome to my submission for the take home task.
The submission includes two main services in data_processing and data_visualization.
The data processing application is a Python Flask app which ingests user files, normalizes the data and serves via an API.
The data visualization application interacts with the above API to display user information.

## Goals and Approach

- Process data provided and attempt to "fix" erroneous data where possible
- Normalize data to allow for further evaluation and querying of data
- Serve data via an API for simple user queries
- Display some interesting user data
- Allow app to be deployed easily and repeatedly

### Tools used

Technology selection:
- Python used for main data processing and handling of json data.
- Flask used as a Python API to serve data produced by data processing.
- Simple Angular app created to visualize user data.

## Challenges and Assumptions

### Data Processing

Here's an overview of the thought process taken when working with the dataset:

- Not all files where valid .json, apply known fix if possible otherwise discard. Problems found:
    - Missing closing brackets - add where found and attempt to reload
- What constitutes valid data and what data should be normalized? The following assumptions have been made in order to remove "bad" data:
    - user_id, task_id and program_id must be a valid v4 UUIDs
    - Names must be alpha characters and can contain spaces
    - An email must be a string separated into two parts by the @ symbol and include a domain
    - User handles must pass validation requirements per TikTok/Instagram handle rules
    - Join dates / timestamps should conform to ISO date formats
    - Brand names should consist of alphanumeric characters and allow special characters
    - Likes, shares, reach, comments should be positive integers
    - Sales attributed should be a positive float value

### API - Data processing http://localhost:5000/

Although the data doesn't necessarily reflect this, endpoints serving data assume that there could be multiple programs/tasks per user.
All processed data is served as JSON.

Consists of 3 endpoints:

`/`                     - root level api which serves all data processed by the data_processor

`/user/<user_id>/`      - allows lookup of a single user by user_id

`/top_users`            - sorts users by considering all total_sales_attributed associated with the user

### Front End - Data visualization http://localhost:4200/

Single page application showing the Top Users using the /top_users endpoint
Maps data from API to following interface / component hierarchy User -> Advocacy Program -> Task

## Setup

### Requirements

For docker:

- Docker: [Download Docker](https://www.docker.com/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

For local development:

- Python 3.13 or higher: [Download Python](https://www.python.org/downloads/release/python-3130/)
- pip: [Install pip](https://pip.pypa.io/en/stable/installation/)
- Node.js 18 or higher: [Download Node.js](https://nodejs.org/)

### Running the application

1. Copy the unzipped user data into the data_processing/user_data directory such that:

```
project
└───data_processing
│   └───user_data
│       │   user_0.json
│       │   user_1.json
│       │   ...
```

2. Run using docker compose from the project root using docker compose
`docker compose up`

alternatively, run each application individually

Data Processing - from the `data_processing` directory

`pip install -r requirements.txt`
`python3 src/app.py`

Data Visualization - from the `data_visualization` directory

`npm install`
`npm run start`

3. Once both applications have started, visit
http://localhost:5000/ - Data Processing API
http://localhost:4200/ - Data Visualization Angular App


### Future Work / Improvements

- Data is relational and has possible one-to-many relations between users, programs, tasks. Would be good to move towards using a relational database such as PostgreSQL for better data storage and querying, assuming that future data could be more complicated, e.g. multiple programs/tasks per user [PostgreSQL](https://www.postgresql.org/download/)
- Additional API work to expose more interesting metrics e.g. top brands / top tasks etc.
- Introduce some kind of reliability score for users, users with less information or single handle might be less reliable than users with full contact details for example
- Clean up user representation in front end - map json fields correctly to camelCase variable names
- Tidy up what user information should be displayed - missing fields, show single Alias, format data provided by API
- Currently light on front-end/API testing