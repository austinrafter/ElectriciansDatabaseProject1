#!/bin/bash
set -e
service mysql start
mysql < C:\Users\Austin\PycharmProjects\ElectriciansDatabaseProject1\SQL-for-database\release_sql_for_database.sql
service mysql stop