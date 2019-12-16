# cloud-sql-pyodbc
This repo contains a notebook covering [Getting started with pyodbc and Cloud SQL for SQL Server](https://medium.com/@dmahugh_70618/using-pyodbc-with-cloud-sql-for-sql-server-602fb7a1be1b). See the [blog post](https://medium.com/@dmahugh_70618/using-pyodbc-with-cloud-sql-for-sql-server-602fb7a1be1b) for more information.

You can browse [the notebook](https://github.com/dmahugh/cloud-sql-pyodbc/blob/master/pyodbc_snippets.ipynb) on GitHub, or you can clone this repo and run the notebook locally while connected to your own Cloud SQL for SQL Server instance. If you want to run the notebook locally, here are the setup instructions (which are also included in the notebook itself):

* Create a Cloud SQL for SQL Server instance and service account, then configure a local proxy connection as covered in [Cloud SQL Setup](https://medium.com/@dmahugh_70618/cloud-sql-setup-4fc72d3f33db).
* Clone the [GitHub repo](https://github.com/dmahugh/cloud-sql-pyodbc) to a local folder, and edit the ```config.py``` file to enter your project and Cloud SQL settings. (See the **ODBC Drivers** section below for information about how to set the ```driver``` setting.)
* Install the ```pyodbc``` package in your notebook environment. The way to do this can vary depending on which notebook software you're running, but in most cases you can simply do a ```!pip install pyodbc``` command in a notebook cell.

![using the Cloud SQL Proxy](https://github.com/dmahugh/cloud-sql-pyodbc/raw/master/images/notebook_proxy.png)
