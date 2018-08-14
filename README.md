# Custom Service Area
Repository to store all fonts used in project.

# Goals and challenge
As Mozio expands internationally, we have a growing problem that many shuttle suppliers we'd like to integrate cannot give us concrete zipcodes, cities, etc that they serve. To combat this, we'd like to be able to define custom polygons as their "service area" and we'd like for the owners of these shuttle companies to be able to define and alter their polygons whenever they want, eliminating the need for mozio employees to do this boring grunt work.

We'd like you to build a working prototype of a solution to this problem. It does not need to be responsive, just make it look good on a desktop computer and work well in chrome. You will be building 2 basic web pages and a small django backend to support them. Create a Github account if you do not have one already and put all of your source code on github.

The first page should contain a large interactive google map. You should be able to create polygons with an arbitrary number of points to define a "service area". Make it as easy to use and as editable as possible. I'd like you to shade or at least draw the box on the map so that I can see exactly the area that has been covered. There should be a way for me to view the exact lat/lng values of all my points, as well as a clear and submit a button. On submit, the data should be sent to the backend and stored. The most recent data should also be retrieved when I load the page next.

The second page should also contain a large google map. I should be able to click anywhere on the map and be told whether that point is within the bounding box or not. You may cache data on the fronted, but be sure to actually use the django backend here to store the data permanently in a database

Build your backend using Django and MySQL or postgres. Figure out a way to store that data such that lookups are FAST. Mozio has thousands of providers who each serve many different areas, so the lookup needs to be quick. Deploy your app entirely using AWS and write up some basic API docs on how to use it. Mozio will pay any server costs that you may incur while doing this. COMMENT YOUR CODE and make the code as pretty and easy to understand as possible.

Plus - If you'd like to go above and beyond, here are some suggestions:
 - support multiple bounding boxes and do lookup in all of them when I request an address
 - Instead of polygons, allow users to draw freely on the map.