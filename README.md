# Wiki BFS

Breadth first search between two Wikipedia entries. Distributed systems homework.

- [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/) are required to run the workers.
- [Python 3](https://www.python.org/downloads/) is required to run the master

### To run this project:

1. `git clone https://github.com/SamiKoh/wikibfs.git`
2. `cd wikibfs`
3. `docker-compose build`
4. `docker-compose up`
5. `python master/master.py cat dog en`

### Notes:

- UI works, but couldn't make master run as a server because server implementation uses similar process pool approach than my `master.py` and daemonic processes cannot create new child processes in python's multiprocessing library
- To increase build time, UI is disable because master does not work on HTTP server
