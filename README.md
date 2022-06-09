# AirBnB clone - The console
## Description
AirBnB is a complete web application, integrating database storage, a back-end API, and front-end interfacing in the clone of [AirBnB](https://www.airbnb.com/)

The project currently only implement the back-end console.

## Classes
This program utilizes the following classes:
|     | BaseModel | FileStorage | User | State | City | Amenity | Place | Review |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| **PUBLIC INSTANCE ATTRIBUTES** | `id`<br>`created_at`<br>`updated_at` | | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` |
| **PUBLIC INSTANCE METHODS** | `save`<br>`to_dict` | `all`<br>`new`<br>`save`<br>`reload` | "" | "" | "" | "" | "" | "" |
| **PUBLIC CLASS ATTRIBUTES** | | | `email`<br>`password`<br>`first_name`<br>`last_name`| `name` | `state_id`<br>`name` | `name` | `city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` | 
| **PRIVATE CLASS ATTRIBUTES** | | `file_path`<br>`objects` | | | | | | |

## Storage
This project supports the serialization and deserialization of simple data sets using a simple file storage mechanism. The data sets are serialized to a JSON file format for the purpose of simplicity.
The program initializes an instance of `FileStorage` called `storage` every time the backend is initialized.  As class instances are 
created, updated, or deleted, the `storage` object is used to register 
corresponding changes in the `file.json`.

## Console
The console is a command line interpreter that allows the manipulation of all classes utilized by the application by making calls on the `storage` object defined above.

## Using the console
The command interpreter can be started by running `./console.py` in your terminal.
```
$ ./console.py
(hbnb)
```
To quit the console, enter the command `quit`, or input an EOF signal (`ctr-D`)
```
$ ./console.py
(hbnb) quit
$
```
```
$ ./console.py
(hbnb) EOF
```
## The Console Commands
- ### create
  - Usage: `create <class>

Creates a new instance of a given class. The ID of the created instance is printed and instance is saved to `file.json`.
```
$ ./console.py
(hbnb) create BaseModel
ecbf544f-649b-477f-a88f-c69abf904948
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.ecbf544f-649b-477f-a88f-c69abf904948": {"id": "ecbf544f-649b-477f-a88f-c69abf904948", "created_at": "2022-06-09T19:55:16.143429", "updated_at": "2022-06-09T19:55:16.143437", "__class__": "BaseModel"}}
```
* ### show
  * Usage: `show <class> <id> or <class>.show(id)`

Prints the string repesentation of an instance based on the class name and id
 ```
$ ./console.py
(hbnb) create User
90665eb5-b6eb-4777-b1bb-2cf0e8233f6e
(hbnb) 
(hbnb) show User 90665eb5-b6eb-4777-b1bb-2cf0e8233f6e
[User] (90665eb5-b6eb-4777-b1bb-2cf0e8233f6e) {'id': '90665eb5-b6eb-4777-b1bb-2cf0e8233f6e', 'created_at': datetime.datetime(2022, 6, 9, 20, 4, 51, 116437), 'updated_at': datetime.datetime(2022, 6, 9, 20, 4, 51, 116442)}
(hbnb)
(hbnb) User.show(90665eb5-b6eb-4777-b1bb-2cf0e8233f6e)
[User] (90665eb5-b6eb-4777-b1bb-2cf0e8233f6e) {'id': '90665eb5-b6eb-4777-b1bb-2cf0e8233f6e', 'created_at': datetime.datetime(2022, 6, 9, 20, 4, 51, 116437), 'updated_at': datetime.datetime(2022, 6, 9, 20, 4, 51, 116442)}
(hbnb)
```
* ### destroy
  * Usage: `destroy <class> <id> or <class>.destroy(<id>)`

Deletes an instance based on the class name and id (saves the change into the JSON file)
 ```
$ ./console.py
(hbnb) create City
29977f37-38da-4461-a1f5-ceeadcb6aebc
(hbnb) create Place
f2d996d4-5e1f-416a-8c3a-bc2de9fd49b2
(hbnb) destroy City 29977f37-38da-4461-a1f5-ceeadcb6aebc
(hbnb) Place.destroy(f2d996d4-5e1f-416a-8c3a-bc2de9fd49b2)
```
* ### all
  * Usage: `all or all <class> or <class>.all()`

Prints all string representation of all instances based or not on the class name.
```
$ ./console.py
(hbnb) create BaseModel
5156be80-1c2d-490c-a00d-7dba39ffa652 
(hbnb) create BaseModel
4bd6266f-25de-41e6-8605-2639f8785719
(hbnb) create User
64b0693d-c571-4811-b328-b88e27141184
(hbnb) create User
854da6b1-2c09-4cbc-8352-c7249618021b
(hbnb)
(hbnb) all BaseModel
[BaseModel] (5156be80-1c2d-490c-a00d-7dba39ffa652) {'id': '5156be80-1c2d-490c-a00d-7dba39ffa652', 'created_at': datetime.datetime(2022, 6, 9, 20, 23, 32, 595393), 'updated_at': datetime.datetime(2022, 6, 9, 20, 23, 32, 595409)}
[BaseModel] (4bd6266f-25de-41e6-8605-2639f8785719) {'id': '4bd6266f-25de-41e6-8605-2639f8785719', 'created_at': datetime.datetime(2022, 6, 9, 20, 23, 42, 417303), 'updated_at': datetime.datetime(2022, 6, 9, 20, 23, 42, 417309)}
(hbnb)
(hbnb) User.all()
[User] (64b0693d-c571-4811-b328-b88e27141184) {'id': '64b0693d-c571-4811-b328-b88e27141184', 'created_at': datetime.datetime(2022, 6, 9, 20, 23, 49, 454662), 'updated_at': datetime.datetime(2022, 6, 9, 20, 23, 49, 454668)}
[User] (854da6b1-2c09-4cbc-8352-c7249618021b) {'id': '854da6b1-2c09-4cbc-8352-c7249618021b', 'created_at': datetime.datetime(2022, 6, 9, 20, 23, 50, 769454), 'updated_at': datetime.datetime(2022, 6, 9, 20, 23, 50, 769463)}
(hbnb)
(hbnb) all
[BaseModel] (5156be80-1c2d-490c-a00d-7dba39ffa652) {'id': '5156be80-1c2d-490c-a00d-7dba39ffa652', 'created_at': datetime.datetime(2022, 6, 9, 20, 23, 32, 595393), 'updated_at': datetime.datetime(2022, 6, 9, 20, 23, 32, 595409)}
[BaseModel] (4bd6266f-25de-41e6-8605-2639f8785719) {'id': '4bd6266f-25de-41e6-8605-2639f8785719', 'created_at': datetime.datetime(2022, 6, 9, 20, 23, 42, 417303), 'updated_at': datetime.datetime(2022, 6, 9, 20, 23, 42, 417309)}
[User] (64b0693d-c571-4811-b328-b88e27141184) {'id': '64b0693d-c571-4811-b328-b88e27141184', 'created_at': datetime.datetime(2022, 6, 9, 20, 23, 49, 454662), 'updated_at': datetime.datetime(2022, 6, 9, 20, 23, 49, 454668)}
[User] (854da6b1-2c09-4cbc-8352-c7249618021b) {'id': '854da6b1-2c09-4cbc-8352-c7249618021b', 'created_at': datetime.datetime(2022, 6, 9, 20, 23, 50, 769454), 'updated_at': datetime.datetime(2022, 6, 9, 20, 23, 50, 769463)}
(hbnb)
```

* ### count
  * Usage: `count <class> or <class>.count()`

Retrieves the number of instances of a given class.
```
(hbnb) create BaseModel
952c8aed-061f-4851-8292-1d478f7c7aa0
(hbnb) create BaseModel
b6ae2de6-9bad-48ca-b7e3-bc573cfd62aa
(hbnb) create BaseModel
1f34c43e-31c6-4a15-89f1-9ff2735c51ac
(hbnb) create User
91b88604-74ce-40ea-b41c-006a95794524
(hbnb) create User
e36222ff-7717-44d8-a88c-011de3e411fd
(hbnb)
(hbnb) count BaseModel
3
(hbnb) User.count()
2
(hbnb) 
```
* ### update
  * Usage: `update <class> <id> <attribute name> "<attribute value>" or <class>.update(<id>, <attribute name>, <attribute value>) or <class>.update( <id>, <attribute dictionary>)`

Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pairs. If update is called with a single key/value attribute pair, only "simple" attributes can be updated (ie. not id, created_at, and updated_at). However, any attribute can be updated by providing a dictionary.
```
$ ./console.py
(hbnb) create User
6f74c68f-97d0-42a5-9c3b-cc06e665d6c4
(hbnb) 
(hbnb) update User 6f74c68f-97d0-42a5-9c3b-cc06e665d6c4 last_name "Betty"
(hbnb) show User 6f74c68f-97d0-42a5-9c3b-cc06e665d6c4
[User] (6f74c68f-97d0-42a5-9c3b-cc06e665d6c4) {'id': '6f74c68f-97d0-42a5-9c3b-cc06e665d6c4', 'created_at': datetime.datetime(2022, 6, 9, 20, 51, 38, 583962), 'updated_at': datetime.datetime(2022, 6, 9, 20, 51, 38, 583979), 'last_name': 'Betty'}
(hbnb) 
(hbnb) User.update(6f74c68f-97d0-42a5-9c3b-cc06e665d6c4, email, "betty@example.com")
(hbnb) show User 6f74c68f-97d0-42a5-9c3b-cc06e665d6c4
[User] (6f74c68f-97d0-42a5-9c3b-cc06e665d6c4) {'id': '6f74c68f-97d0-42a5-9c3b-cc06e665d6c4', 'created_at': datetime.datetime(2022, 6, 9, 20, 51, 38, 583962), 'updated_at': datetime.datetime(2022, 6, 9, 20, 51, 38, 583979), 'last_name': 'Betty', 'email': 'betty@example.com'}
(hbnb) 
(hbnb) User.update(6f74c68f-97d0-42a5-9c3b-cc06e665d6c4, {"address": "57 Ikenga BQ"})
(hbnb) show User 6f74c68f-97d0-42a5-9c3b-cc06e665d6c4
[User] (6f74c68f-97d0-42a5-9c3b-cc06e665d6c4) {'id': '6f74c68f-97d0-42a5-9c3b-cc06e665d6c4', 'created_at': datetime.datetime(2022, 6, 9, 20, 51, 38, 583962), 'updated_at': datetime.datetime(2022, 6, 9, 20, 51, 38, 583979), 'last_name': 'Betty', 'email': 'betty@example.com', 'address': '57 Ikenga BQ'}
(hbnb)
```

# Testing
Unittest for this progrem are defined in the [test](https://github.com/iChigozirim/AirBnB_clone/tree/master/tests) folder. To run the entire test suite simultaneously, execute the following command:
```
$ python3 unittest -m discover tests
```
Alternatively, you can specify a single test file to run at a time:
```
$ python3 -m unittest tests/test_models/test_engine/test_file_storage.py
```
