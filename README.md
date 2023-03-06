# 0x00. AirBnB clone - The console
![AirBnB Logo](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

## Description Of The Project
This Project Creates a Demo copy of The AirBnB Website 

## Description Of The Command Interpreter:
#	how to start it 
	First step in this project is to write a command interpreter to manage your AirBnB objects.
	This is the first step towards building your first full web application:  the AirBnB clone.
	This first step is very important because you will use what you build during this project with all other following projects: 
	HTML/CSS templating,
	database storage,
	API,
	front-end integration…

	TO do this, implement the following steps:
	# Create your repo on your Github Account with the name AirBnB_clone
	# Clone the repo to your local machine with the url of the repo e.g https://github.com/username/AirBnB_clone.git
	# Create all necessary directories and Files that defines the functionality of the Program
	Examples Of files to be created includes:
		models/engine/file_storage.py,
		models/engine/__init__.py,
		models/__init__.py,
		models/base_model.py,
		tests/
		console.py
		models/user.py
		

#	how to use it	
	The commandline interpreter can be executed in Interactive and Non-Interactive mode to do the following:

	Create a new object (ex: a new User or a new Place)
	Retrieve an object from a file, a database etc…
	Do operations on objects (count, compute stats, etc…)
	Update attributes of an object
	Destroy an object

#	examples

	
In Interactive Mode the Interpreter Should Work as Shown Below

```
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

In Non-Interactive Mode it should look as Displayed Below:

```

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
```
THIS PROJECT COVERS THE FOLLOWING:
cmd module,
cmd module in depth,
packages concept page,
uuid module,
datetime,
unittest module,
args/kwargs,
Python test cheatsheet,
cmd module wiki page,
python unittest.
