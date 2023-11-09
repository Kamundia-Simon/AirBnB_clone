# AirBnB_clone - The Console

![alt](img/hbnb.png)
---
## Description

This team project is part of the alx Full-Stack Software Engineer program. It's the first step towards building a first full web application: an AirBnB clone. This first step (back-end) consists of a custom command-line interface for data management, and the base classes for the storage of this data to be used for the development of the application.

---
## Files and Directories

* models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
* tests directory will contain all python unit tests.
* console.py file is the entry point of our command interpreter.
* models/base_model.py file is the base class of all our models. It contains common elements:
    * attributes: id, created_at and updated_at
    * methods: save() and to_json()
    * models/engine directory will contain all storage classes (using the same prototype). For the moment I will have only one: file_storage.py
---
|Command | Description |
|--------|-------------|
|Run the console|`./console.py` |
|Quit the console| `(hbnb) quit` |
|Display command help| `(hbnb) help <command>` |
|Create an object |	`(hbnb) create <class>`|
|Show an object | `(hbnb) show <class> <id> or (hbnb) <class>.show(<id>)` |
|Destroy an object | `(hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>)` |
|Show all objects / all instances of a class | `(hbnb) all or (hbnb) all <class>` |
|Update an attribute of an object | `(hbnb) update <class> <id> <attribute name> "<attribute value>" or (hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")`|
---
Execution in interactive mode 
``` cmd
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
---
Non_interactive mode

``` cmd 
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$ 
