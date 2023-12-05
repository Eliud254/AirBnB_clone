# AirBnB Clone - The Console

## Project Description
Welcome to the AirBnB clone project! In this project, we'll be building the first step towards creating a full web application - an AirBnB clone. The primary focus of this phase is to develop a command-line interface (CLI) or command interpreter to manage AirBnB objects. This includes creating classes for various entities like User, State, City, Place, etc., and implementing a simple flow of serialization/deserialization.

## Command Interpreter
The command interpreter is a CLI tool that allows you to interact with the AirBnB objects. Here's a brief overview:

### How to Start
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the command interpreter script.

```bash
$ ./console.py
```

### How to Use
Once the command interpreter is running, you can use various commands to manage AirBnB objects. Here are some basic commands:

- **create**: Create a new object (User, Place, etc.).
  ```bash
  (hbnb) create User
  ```

- **show**: Display information about a specific object.
  ```bash
  (hbnb) show User 1234-5678
  ```

- **update**: Update attributes of an object.
  ```bash
  (hbnb) update Place 8765-4321 name "Cozy Apartment"
  ```

- **destroy**: Remove an object.
  ```bash
  (hbnb) destroy State 9999-8888
  ```

- **all**: Display information about all objects or all objects of a specific type.
  ```bash
  (hbnb) all
  (hbnb) all User
  ```

- **quit/EOF**: Exit the command interpreter.
  ```bash
  (hbnb) quit
  ```

### Examples
Here are some examples of using the command interpreter:

```bash
$ ./console.py
(hbnb) create User
6b6d4e4d-0d85-4c8b-a21b-75723d5b0aeb
(hbnb) show User 6b6d4e4d-0d85-4c8b-a21b-75723d5b0aeb
[User] (6b6d4e4d-0d85-4c8b-a21b-75723d5b0aeb) {'id': '6b6d4e4d-0d85-4c8b-a21b-75723d5b0aeb', 'created_at': '2023-12-04T06:00:00', 'updated_at': '2023-12-04T06:00:00'}
(hbnb) update User 6b6d4e4d-0d85-4c8b-a21b-75723d5b0aeb first_name "John"
(hbnb) show User 6b6d4e4d-0d85-4c8b-a21b-75723d5b0aeb
[User] (6b6d4e4d-0d85-4c8b-a21b-75723d5b0aeb) {'id': '6b6d4e4d-0d85-4c8b-a21b-75723d5b0aeb', 'created_at': '2023-12-04T06:00:00', 'updated_at': '2023-12-04T06:00:00', 'first_name': 'John'}
(hbnb) quit
```

## Unit Testing
Unit tests are crucial to ensuring the correctness of your implementation. The tests are organized into the `tests` folder, following the same structure as the project. You can execute all tests using the following command:

```bash
$ python3 -m unittest discover tests
```

## Documentation
Make sure to provide comprehensive documentation for your code. This includes docstrings for modules, classes, and functions. To check the documentation for a module, class, or function, you can use the following commands:

```bash
$ python3 -c 'print(__import__("my_module").__doc__)'
$ python3 -c 'print(__import__("my_module").MyClass.__doc__)'
$ python3 -c 'print(__import__("my_module").my_function.__doc__)'
$ python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
```

## Conclusion
By the end of this project, you should have a solid understanding of creating Python packages, building a command interpreter using the cmd module, implementing unit tests, and working with serialization/deserialization of objects. Good luck with your project!
