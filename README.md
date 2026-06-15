<center>
<img src="https://github.com/marjuanm/awtly/blob/main/images/pet.jpg" style="width: 100%; max-width: 600px; height: auto;" alt="Awtly's pet" border="0">
<br>
<img src="https://www.busquedaweb.com/openprojects/awtly/release.png" style="width: 100%; max-width: 94px; height: auto; padding-right: 10px; padding-bottom: 10px;" alt="Release version" border="0">
<a href="https://github.com/marjuanm/awtly/archive/refs/heads/main.zip"><img src="https://www.busquedaweb.com/openprojects/awtly/download.png" style="width: 100%; max-width: 94px; height: auto; padding-right: 10px; padding-bottom: 10px;" alt="Download current version" border="0"></a>
<a href="https://github.com/marjuanm/awtly/blob/main/LICENSE"><img src="https://www.busquedaweb.com/openprojects/awtly/license.png" style="width: 100%; max-width: 94px; height: auto; padding-right: 10px; padding-bottom: 10px;" alt="Project's license" border="0"></a>
</center>

# Awtly
Awtly is an ongoing project still in a very preliminary version.

The goal is create a programming language that is very easy to learn, inspired by Python, Lua, and others, which will allow creating PHP projects from simple to complex with instructions and methodologies that are easy to understand.

The goal is someday to be able create complex applications for PHP, perhaps competing with what is seen in Laravel but without its complexity, through a language that is easy to maintain. I don't know if I will achieve this or not, but I will try.

# Updates for the latest version (0.1.25):

Requirements: Python or superior, download from https://www.python.org/downloads/. On Windows open Command Prompt, navigate to the Awtly folder, and run the command "python awtly.py", on Linux terminal type "python3 awtly.py".

If we don't specify any parameter, we will get the following message: "Invalid number of parameters." Possible parameters (this may change in the future):

* python awtly.py new projectname
  It will create a new Awtly project in the current folder, in future versions we will be able to specify the path where to create the project and perhaps in the future Awtly can be used with the system PATH variable so as not to depend on the installation folder to run the IDE.

The system now checks if the project to be created exists in the local folder, allowing the user to proceed or not. For now, it continues to display the message "I will create the project 'projectname'" if the user wishes to continue.

* python awtly.py delete projectname
It will delete an Awtly project in the current folder; in future versions, we will be able to specify the path from which to delete the project, and perhaps in the future Awtly can be used with the system PATH variable so as not to depend on the installation folder to run the IDE.

For now we will only receive the message "I will delete the project 'projectname'".

* python awtly.py build projectname
It will convert an Awtly project in the current folder to its PHP equivalent, allowing with a simple language to create websites and applications without getting into many complications of some PHP frameworks.

In future versions, we will be able to specify the path where to compile the project, and perhaps in the future Awtly can be used with the system PATH variable so as not to depend on the installation folder to run the IDE.

For now we will only receive the message "I will convert the project 'projectname' into its PHP equivalent".

* python awtly.py help ("/?" and "-h" are possible variations)
This will display specific help if you type the name of a command after the command "help" or "-h" (for example, "awtly help new" or "awtly -h new").

If you only type "help", "/?", or just "-h", it will display general help for all commands supported by Awtly.

* python awtly.py -v
This will display information about the current version of the Awtly IDE.
