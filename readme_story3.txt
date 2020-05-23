Story 3 is about that How many tweets mentioned COVID-19 or financial pressure or pressure and are these clustered in certain areas.
e.g. Area's population influcences the low income households    
       Households in which state is experiencing greater financial pressure during the COVID-19
The MapReduce Query can return the total numbers of low income households in each state.
The data of low income households is now sorted by states, but in database, their local government areas are also recorded. So if you 
want, you can also sort them by LGA. 

tweets_harvester3.py - upload aurin and tweets data to the database. Twitter API is StreamingAPI. The
                                     filter keywords are "financial pressure", "pressure" and "covid-19".
dataProcess.py -           add my MapReduce query part

flaskPart.py -                add a GainData3part to display my results sorted by states.
                                     The URL is "/travis_app/gain_data/<region>"
