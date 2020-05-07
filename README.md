# ccc_2020

## It is a nginx-uwsgi-flask framework program
### When the environment is well prepared, you can follow the steps to run
1. run the tweets harvester program. It will create two databases and gain real time tweets
2. run unswgi `uwsgi uwsgi5001.ini`
3. run nginx `nginx -c './nginx.conf'`
4. the restful api frame **http://127.0.0.1:5001/starry_app/gain_data/<region name>**
region [nsw, vic, tas, wd, sa, nt, act, qld]

### whether there are some relations bwtween age distribution and keywords 'bar'&'nightclub'
### can only run flaskPart.py to test the program! the address will be 127.0.0.1:5000


