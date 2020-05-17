Story 2 is How many tweets mention Covid-19 or coronavirus and are these clustered in certain areas,	
e.g. rich vs poor suburbs or in	statistical areas where	there are more/less hospitals etc? 

The MapReduce Query can return the total numbers of hopsitals, the median/mean income in each state.
The hopsitals is now sorted by states, but in database, their suburbs are also recorded. So if you 
want, you can also sort them by suburbs. However, I think it is much easier to sorted by states.

Besides, hospitals are sorted by size(bed nums) and category(public/private). Maybe there exist some
relationships between tweets count and hospital size/category.

tweets_harvester2.py - upload aurin and tweets data to the database. Twitter API is StreamingAPI. The
                       filter keywords are "covid-19" and "coronavirus".
dataProcess.py - add my MapReduce query part

flaskPart.py - add a GainData2 part to display my results sorted by states.
               The URL is "/charlie_app/gain_data/<region>"
