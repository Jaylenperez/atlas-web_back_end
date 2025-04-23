# <p align="center">Basic Authentication</p>

## :bookmark: Table of Contents

<details>
        <summary>
        CLICK TO ENLARGE
        </summary>
        :memo: <a href="#description">Description</a>
        <br>
        :wrench: <a href="#installation">Installation</a>
        <br>
        :sparkles: <a href="#authors">Authors</a>
</details>

## :memo: <span id="description">Description</span>

In this project, you’ll learn how HTTP Basic Authentication works under the hood by building it step-by-step on a simple Flask API. Although in production you’d use a library (e.g. Flask-HTTPAuth), here you will manually:

- Add custom error handlers for 401 and 403 statuses
- Define which routes require authentication
- Extract and decode Base64 credentials from the `Authorization` header
- Look up and validate users against a file-based store
- Plug your authentication class into Flask’s `before_request` hooks

## :wrench: <span id="installation">Installation</span>

**Clone the repository**

`git clone https://github.com/Jaylenperez/basic_authentication.git`

## :sparkles: <span id="authors">Authors</span>

**Jaylen Perez**

- Github: [@Jaylenperez](https://github.com/Jaylenperez)
