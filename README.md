<h1 align="center">Final Project - Data Engineering - M2</h1>


<div align="center">
    <a> By : Jaouen Guillaume - Boersma Hélène - Courtois Quentin </a>
</div>

## Purpose of the project

As a part of the curriculum of the Master 2 (M2) course entitled “Data Engineering II”, the students will complete a team project work. Each team is composed of 3 members, and the members will take care of dividing the tasks equally between them. The purpose of this project is to combine all the skills collected throughout the entire course, and to provide a solid example of real-life application development in a DevOps environment.   

The following sections provide necessary information about the description of the application  to be created.

Supervised by **Khodor Hammoud**

## Steps to run the application using Docker
---

1. Git clone the project : https://github.com/Helene-Boersma/DE_Toxicity_Monitor.git

2. Enter this command : *cd DE_Toxicity_Monitor*

3. Run the application with docker : *docker-compose up*

All the ports of the project :

  * http://localhost:5000 to access the *webserver*
  * http://localhost:8080 to access the *jenkins*
  * http://localhost:9090 to access *promotheus*
  * http://localhost:3000 to access *grafana*

## Docker image on docker hub

Adress : https://hub.docker.com/r/guillaumeefrei/final_project_dataengineering/tags

You can also run this command : docker pull guillaumeefrei/final_project_dataengineering:latest

<div align="center">
<a href="https://www.efrei.fr/" target="_blank"><img src="https://www.efrei.fr/wp-content/uploads/2022/01/LOGO_EFREI-PRINT_EFREI-WEB.png" width="270" height="100"></a>
</div>