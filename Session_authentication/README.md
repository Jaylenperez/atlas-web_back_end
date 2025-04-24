# <p align="center">Session Authentication</p>

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

In this project, you will implement session-based authentication from scratch, without installing any external modules. Building on your Basic authentication work, you’ll first add a `/users/me` endpoint that returns the currently authenticated user. Then you’ll create a full SessionAuth mechanism that:

- Issues and stores session IDs (UUIDs) in memory
- Sends and reads session IDs in cookies
- Protects API endpoints via a Flask `@before_request` hook

## :wrench: <span id="installation">Installation</span>

**Clone the repository**

`git clone https://github.com/Jaylenperez/Session_authentication.git`

## :sparkles: <span id="authors">Authors</span>

**Jaylen Perez**

- Github: [@Jaylenperez](https://github.com/Jaylenperez)
