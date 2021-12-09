Instructions to run through Docker 
1.Download and install docker desktop(instructions for windows and mac found here https://www.docker.com/products/docker-desktop )
2.Upon installing docker desktop open it and run it to be ready to use docker to open the project
3.Clone this repository
      a.Seed SQL for the database can be found in the SQL-for-database folder under the file release_sql_for_database.sql within the project to confirm the database sql
4.Open a browser
5.Open a terminal
6.Move to the directory containing ElectriciansDatabaseProject1 min your machine
        a.The command to move through directories is ‘cd /path/to/the/project/ElectriciansDatabaseProject1’ where ‘/path/to/the/project/ElectriciansDatabaseProject1’ is the full path to the ElectriciansDatabaseProject1 directory on your machine
7. Enter ‘docker-compose up --build’ and press enter (note: Docker sometimes has an error that is closing the database after opening the first time which doesn’t allow the flask portion to read from or write to it.)
              a.If the jobs, inventory, or electricians lists do not show when clicking the links and the terminal you ran the command is still up press ctrl-c, 3 times in the terminal you ran the command in re-enter ‘docker-compose up --build’ and press enter in the same terminal
              b.If the jobs, inventory, or electricians lists do not show when clicking the links and you have already closed the terminal
                      I.Open a terminal
                      II.Enter  ‘cd /path/to/the/project/ElectriciansDatabaseProject1’ and press enter
                      III.Enter ‘docker-compose stop’ and press enter
                      IV.Enter ‘docker-compose up’ and press enter
8.The program should run on localhost:3000 in the browser and may take a few minutes to build
9.Any subsequent runs should use 'docker-compose up' instead of 'docker-compose up --build' when performing the start up command on your machine
