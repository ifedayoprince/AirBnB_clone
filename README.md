# AirBnB Clone Project

## Description

This project is a simplified clone of the AirBnB website. It is designed to help you learn and implement fundamental concepts of higher-level programming by building a web application step-by-step. The project will involve creating a command interpreter, a front-end website, a database for storing data, and an API for communication between the front-end and the database. By the end of the project, you will have a functional web application with essential features of the AirBnB platform.

## Features

- Command interpreter for data manipulation
- Static and dynamic web pages
- Persistent data storage using files and databases
- RESTful API for data manipulation
- Modular and scalable codebase

## Concepts Covered

- Unittest
- Python packages
- Serialization/Deserialization
- *args and **kwargs
- Datetime manipulation
- HTML/CSS
- MySQL storage
- Web frameworks and templating
- JQuery

## Command Interpreter

The command interpreter is a crucial part of this project. It allows you to create, read, update, and delete objects via a command-line interface without a visual interface. This is particularly useful for development and debugging.

### How to Start the Command Interpreter

To start the command interpreter, you need to run the `console.py` file. Ensure you have Python installed on your system.

```bash
$ ./console.py
```

### How to Use the Command Interpreter

Once the command interpreter is running, you can enter various commands to manipulate your data. Below are some common commands and their usage:

- `help`: Displays a list of available commands or detailed help for a specific command.
- `create <class>`: Creates a new instance of the specified class and prints its ID.
- `show <class> <id>`: Prints the string representation of an instance based on the class name and ID.
- `destroy <class> <id>`: Deletes an instance based on the class name and ID.
- `all [<class>]`: Prints all string representations of all instances or instances of a specific class.
- `update <class> <id> <attribute name> "<attribute value>"`: Updates an instance based on the class name and ID by adding or updating an attribute.

### Examples

Here are some examples to demonstrate how to use the command interpreter:

1. **Creating a new instance**:
    ```bash
    $ ./console.py
    (hbnb) create User
    d3f29b7b-7d1f-4c80-a4fb-d4825e3a5d17
    (hbnb)
    ```

2. **Showing an instance**:
    ```bash
    $ ./console.py
    (hbnb) show User d3f29b7b-7d1f-4c80-a4fb-d4825e3a5d17
    [User] (d3f29b7b-7d1f-4c80-a4fb-d4825e3a5d17) {'id': 'd3f29b7b-7d1f-4c80-a4fb-d4825e3a5d17', 'created_at': datetime.datetime(2023, 5, 17, 12, 45, 0, 0), 'updated_at': datetime.datetime(2023, 5, 17, 12, 45, 0, 0)}
    (hbnb)
    ```

3. **Updating an instance**:
    ```bash
    $ ./console.py
    (hbnb) update User d3f29b7b-7d1f-4c80-a4fb-d4825e3a5d17 name "John Doe"
    (hbnb) show User d3f29b7b-7d1f-4c80-a4fb-d4825e3a5d17
    [User] (d3f29b7b-7d1f-4c80-a4fb-d4825e3a5d17) {'id': 'd3f29b7b-7d1f-4c80-a4fb-d4825e3a5d17', 'created_at': datetime.datetime(2023, 5, 17, 12, 45, 0, 0), 'updated_at': datetime.datetime(2023, 5, 17, 12, 47, 0, 0), 'name': 'John Doe'}
    (hbnb)
    ```

4. **Destroying an instance**:
    ```bash
    $ ./console.py
    (hbnb) destroy User d3f29b7b-7d1f-4c80-a4fb-d4825e3a5d17
    (hbnb) show User d3f29b7b-7d1f-4c80-a4fb-d4825e3a5d17
    ** no instance found **
    (hbnb)
    ```

5. **Displaying all instances of a class**:
    ```bash
    $ ./console.py
    (hbnb) all User
    ["[User] (a1b2c3d4) {'id': 'a1b2c3d4', 'created_at': datetime.datetime(2023, 5, 17, 12, 50, 0, 0), 'updated_at': datetime.datetime(2023, 5, 17, 12, 50, 0, 0)}"]
    (hbnb)
    ```
