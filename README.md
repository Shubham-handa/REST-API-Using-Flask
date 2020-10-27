# REST-API-Using-Flask


[![](https://img.shields.io/badge/flask-v1.1.1-blue)](https://flask.palletsprojects.com/en/1.1.x/) [![](https://img.shields.io/badge/python-v3.7-blue)](https://www.python.org/downloads/release/python-360/) [![](https://img.shields.io/badge/Postman-App-orange)](https://www.postman.com/) [![](https://img.shields.io/badge/MongoDB%20Atlas-Database-green)](https://www.mongodb.com/cloud/atlas#:~:text=MongoDB%20Atlas%20is%20the%20global,data%20security%20and%20privacy%20standards.) [![](https://img.shields.io/badge/Docker-App-blue)](https://www.docker.com/) [![](https://img.shields.io/badge/Anaconda-Spyder-red)](https://www.anaconda.com/) 




![alt text](https://miro.medium.com/max/2404/1*JUOITpaBdlrMP9D__-K5Fw.png)
===
Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers.
Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels. 
All containers are run by a single operating system kernel and therefore use fewer resources than virtual machines.

The service has both free and premium tiers. The software that hosts the containers is called Docker Engine. It was first started in 2013 and is developed by Docker.

Components
------------
The Docker software as a service offering consists of three components:

- Software: The Docker daemon, called dockerd, is a persistent process that manages Docker containers and handles container objects.
  The daemon listens for requests sent via the Docker Engine API. The Docker client program, called docker, provides a command-line interface that allows users to interact with Docker daemons.
- Registries: A Docker registry is a repository for Docker images. Docker clients connect to registries to download ("pull") images for use or upload ("push") images that they have built. 
  Registries can be public or private. Two main public registries are Docker Hub and Docker Cloud. Docker Hub is the default registry where Docker looks for images.
  Docker registries also allow the creation of notifications based on events.
- Objects: Docker objects are various entities used to assemble an application in Docker. The main classes of Docker objects are images, containers, and services
  - A Docker container is a standardized, encapsulated environment that runs applications. A container is managed using the Docker API or CLI.
  - A Docker image is a read-only template used to build containers. Images are used to store and ship applications.
  - A Docker service allows containers to be scaled across multiple Docker daemons. The result is known as a swarm, a set of cooperating daemons that communicate through the Docker API.

![alt text](https://miro.medium.com/max/1200/1*uHcHPQYNkj0lq57Dg6PAww.jpeg)
MongoDB Atlas is the global cloud database service for modern applications. Deploy fully managed MongoDB across AWS, Azure, or GCP. Best-in-class automation and proven practices guarantee availability, scalability, and compliance with the most demanding data security and privacy standards.

Why MongoDB Atlas
-----------------
- Flexible and scalable document database. Available as a fully managed service.
- Secure for sensitive data.
- Build for optimal performance

New Features
------------
- Atlas Data Lake
- Atlas Search
- MongoDB Realm

![alt text](https://4.bp.blogspot.com/-wVSij9rfStg/XG7iQvHUqpI/AAAAAAAAGwI/Eol6oonV49k6QgizI6nquU373QVBhxGigCLcBGAs/s1600/image1.png)

An application programming interface (API) is a computing interface which defines interactions between multiple software intermediaries. 
It defines the kinds of calls or requests that can be made, how to make them, the data formats that should be used, the conventions to follow, etc. 
It can also provide extension mechanisms so that users can extend existing functionality in various ways and to varying degrees. 
An API can be entirely custom, specific to a component, or it can be designed based on an industry-standard to ensure interoperability. 
Through information hiding, APIs enable modular programming, which allows users to use the interface independently of the implementation.

REST
----
Representational State Transfer is an architectural style design for Application Programming Interface which allows us to get the current state of an application.

CRUD
----

Whenever we are designing an API service, our model must include at least 4 basic types of functionalities — Create, Read, Update, Delete, or CRUD.
In the REST environment, we should use HTTP Methods to provide CRUD operation on any resource. These methods include -

- HTTP GET — This method is used to read any resource.
- HTTP POST — This method is used to write any resource.
- HTTP PUT — This method is used to update any resource.
- HTTP DELETE — This method is used to delete any resource.

![alt text](https://i.morioh.com/2019/11/21/34f9bcbd043d.jpg)

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. 
It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. 
However, Flask supports extensions that can add application features as if they were implemented in Flask itself. 
Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools.
Extensions are updated far more frequently than the core Flask program.

Working of Docker for creating localhost 
----------------------------------------

### Setting up the Docker

```bash
docker -v
```

### Pulling MongoDB image

```bash
docker pull mongo
```

### Create a container

```bash
docker create -it --name <ContainerName> -p 8000:27017 mongo
```

![alt text](https://github.com/Shubham-handa/Greendeck_Assignment_Task1/blob/main/Docker_CMD_for_creating_container.png)


### Start the Container

```bash
docker start <ContainerName>
```

### Stop the Container

```bash
docker stop <ContainerName>
```

### For create and start the different containers in docker with some configuration mentioned in yml/yaml file

```bash
docker-compose up
```

![alt text](https://github.com/Shubham-handa/Greendeck_Assignment_Task1/blob/main/Docker_compose_CMD.png)


Screenshots of Postman API requests for different methods:-
---------------------------------------------------------

GET Request
-----------
![alt text](https://github.com/Shubham-handa/Greendeck_Assignment_Task1/blob/main/GET.png)


POST Request
-----------
![alt text](https://github.com/Shubham-handa/Greendeck_Assignment_Task1/blob/main/POST.png)


- In above screenshot we can clearly see that we do not provide any information in classifiation 4 column for particular brand name.

- By using PUT operation we add some information in classification 4 column for brand item “Fast” in the database.


PUT Request
-----------
![alt text](https://github.com/Shubham-handa/Greendeck_Assignment_Task1/blob/main/PUT.png)


DELETE Request
-----------
![alt text](https://github.com/Shubham-handa/Greendeck_Assignment_Task1/blob/main/DELETE.png)


See the pdf file for more details of CRUD operation
---------------------------------------------------

https://github.com/Shubham-handa/Greendeck_Assig
