# meridian
A RESTful home automation framework

### Objective
Meridian aims to make home automation and remote access more accessible. It accomplishes this by defining "Responders" in the plugins directory. Each Responder is loaded into memory dynamically, and the initialization code (if any) is run for that plugin. Then, when a GET or POST request is made to ```http://server.com:8080/pluginname```, the processing code for the appropriate plugin's Responder is run. The goal is to be as extensible and easy to understand as possible.

### Warning
Meridian currently does not perform any authentication. This means, at this time, any users with access to port 8080 on the machine it runs on can perform operations. A particularly dangerous plugin for this is the shell plugin.

### Running
Install the required modules using [pip](https://pip.pypa.io/en/latest/installing.html):
```
pip install -r requirements.txt
```

Start the Meridian server on your host machine:
```
python meridian.py
```

Once started, connect to [http://localhost:8080/sample](http://localhost:8080/sample) to view how various routes can be defined.

### Plugins
Not all plugins will be detailed here, but some notable ones to test out shall be.

#### ping
The ping plugin wil return 200 OK.
```
curl -D - http://localhost:8080/ping
```

#### shell
The shell plugin will execute a shell command from the "cmd" parameter. An example of this is below. It also keeps track of the curent directory, and using "cd" will affect subsequent requests to this plugin.
eg. [http://localhost:8080/shell?cmd=echo hello there](http://localhost:8080/shell?cmd=echo%20hello%20there)


### Other Plugins
Check the appropriate config directory for detailed information on a specific package:

- [japanese](https://github.com/vgmoose/meridian/tree/master/config/japanese/)
