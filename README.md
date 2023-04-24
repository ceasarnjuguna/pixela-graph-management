**Pixela Graph Management**

This is an example script that demonstrates how to use the Pixela API to create, update, and delete pixels on a graph. 
The script is written in Python and uses the requests library to interact with the Pixela API.

**Getting Started**

To run the script, you'll need to set up a few things first.

**Prerequisites**

You'll need to have Python 3 installed on your system. You can download it from the official website:
https://www.python.org/downloads/.

You'll also need to install the requests library. You can do this using pip:

_pip install requests_

**Setting Up the Environment Variables**

The script uses environment variables to store sensitive information such as your Pixela 
username and API token. Before running the script, you'll need to set these environment variables.

1.Create a file named .env in the root directory of the project.
2.Add the following lines to the file, replacing the placeholders with your actual values:

_PIXELA_USERNAME=your_username_
_PIXELA_TOKEN=your_token_
_PIXELA_GRAPH_ID=your_graph_id_

**Running the Script**

To run the script, simply execute the following command in the root directory of the project:

_python pixela.py_

The script will create a graph, add a pixel to the graph, update the pixel, and delete the pixel. You can comment out any of these actions by commenting out the corresponding lines of code.

**License**

This project is licensed under the MIT License. See the LICENSE file for details.

