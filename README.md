# run-MySQL-in-Docker
*Install MySQL in docker container*

Here we will see how we can run MySQL in a docker container with volumns and how to access it through terminal as well through python.

## Command to run MySQL container
```
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=rootpassword -e MYSQL_DATABASE=mydatabase -v mysql_data:/var/lib/mysql -p 3306:3306 -d mysql:latest

```

* **--name mysql-container**: Names the container *mysql-container*. You can replace this with any name you prefer. **(optional)**
* **-e MYSQL_ROOT_PASSWORD=rootpassword**: Sets the root password for the MySQL instance. You can replace *rootpassword* with your own password.
* **-e MYSQL_DATABASE=my_database**: Automatically creates a database named my_database when the container starts. **(optional)**
* **-v mysql_data:/var/lib/mysql**: Mounts a volume to make data persistent. You can replace *mysql_data* with your local directory path to store MySQL data on your host machine but *mysql_data* will work perfectly.
  * (**note**: Use only if you want to store your data (like tables and records) permanently, else you can remove it.)*
* **-p 3306:3306**: Maps port 3306 on the container to port 3306 on your host, so you can connect to the MySQL server externally. Necessary in order to access MySQL from anywhere.
* **-d**: Runs the container in detached mode. **(optional)**
* **mysql:latest**:  Use the latest MySQL image. Intead of *latest*, you can specify any version.


## Check MySQL container is running
```
docker ps
```
## Access MySQL through terminal
```
docker exec -it mysql-container mysql -u root -p

```
* You can raplace *mysql-container* with your MySQL container id/ container name. In this case, *mysql-container* will work perfectly.
* **-u root**: for *root* user.
* **-p** : for password promt.

After running above command, terminal will ask for password. Put your password that you have used previously.

Great, now you access MySQL.

## Access MySQL through Python
Install the MySQL driver for Python.
```
pip install mysql-connector-python
```
Code is present in this repository.

## Documentation
For more information: 

[MySQL](https://hub.docker.com/_/mysql)

## If you liked this repository

* Dont't forget to give this repository a 🌟
