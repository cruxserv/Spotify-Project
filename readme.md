DJ Stream (Spotify Clone)
This is a file streaming service for DJs with edits that can be used for performances.

API Reference Table
(/) Gets main home page, where the dj mp3 files can be streamed from, must be logged in to access
(/login) login page Gets information from user for gaining access to system after signup, Posts send user input to db for verification, page is hidden from those logged in
(/sign_up) sign up page, Gets all necessary information in form for user input, as well as Posts to create db entry with info

Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
What things you need to install the software and how to install them: requirements.txt

- git clone https://github.com/cruxserv/Spotify-Project
- Create an empty database named "dj-stream"
- Import the sql file included in the repo
  Deployment

Built With

Python
Flask
SQLite - Test DB
PostgreSQL - Relational DB

Authors

CruxServ - John-Carlos Sanabria

# Spotify-Project
