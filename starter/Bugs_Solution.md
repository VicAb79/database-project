# Bugs and Solutions

### Requirement 1
Here we are requied to ***Find up to some number of unique NEOs on a given date or between start date and end date.***

***SOLVED***

I solved Search requirement by creating two search instance methods in the NEOSeacher class; `equals_search` to search in a given date and `between_search` to search between start and end date.

 - `equals_search`: Here we pass as parameter the given date (string format) which is used to extract the corrresponding neo's from the NEODatabase object instantiated in the NEOSeacher. The result here is a list of NEO for that given date. 

- `between_search`: Here we pass as parameter a list containinig the start and end date (list of strings). We then split up the date string into a tuple to hole th year, month and day before creating a date object using the `datetime` library. Further more get the range of dates between the start and end dates which is used to extract the corrresponding neo's from the NEODatabase object instantiated in the NEOSeacher. The result here is a list of NEO between the start and end date. 


### Requirement 2
Here we are required to ***Find up to some number of unique NEOs on a given date or between start date and end date larger than X kilometers.***

I solved this requirement by modifying implementing the Filter class, creating a dictionary a in Filter.Options, with keys of filter names and values corresponding NearEarthObject or OrbitalPath  property (attribute). Also created Filter.Operators with a dictionary of key opearator symbols and corresponding operators method as value.

In the `create_filter_options` method, we read in the filter_options as a list containing different filter_options.  We split up each option, which is of the form `"filter_option:operation:value_of_option"`,  extracting the string seperated by `:`. This gives a list of 3 strings, with the first representing the filter_option, the second representing the operation and the third representing the value.

To solve this requirement, we check if the filter_option matches the string `diameter`, if so, we create a Filter instance as such `Filter(filter_option, object, operation, value)` where object represents a NearthEarthObject in this case since we need its diameter. This filter is then added to a `defaultdict`.

We then set up an `apply` method which applys the filter to NearEarthObjects and returns a list of the filtered Objects (i.e.  the filtered NearEarthObjects). The `NEOSearcher` calls the `Filter.created_filter_options`, passing in the query filters, then each filter created is applied to the resutls and a list of the final result is returned by the `get_objects` method of the `NEOSearcher`.

### Requirement 3.  
***Find up to some number of unique NEOs on a given date or between start date and end date larger than X kilometers that were hazardous.***

`Bug`:  Running the test fails at requirement 3, producing 4 Objects instead of 0. We followed the implemetaion on the previous create filter. This is noticed on `line 138` of the `search.py` file.

`Solution`: We fixed this by replcaing the filter method on `line 138`, replacing with a loop on the results and applying the filter operation to it. For this solution, on line 137 of the search.py file, we also include a variable is_hazadous, to hold a boolean value that corresponds to the string "True" or "False" held by the filter value. We then append NearEarthObjects the meet the filter criteria to a filtered list and return.

### Requirement 4.  
***Find up to some number of unique NEOs on a given date or between start date and end date larger than X kilometers that were hazardous and within X kilometers from Earth.***

I solved this requirements by adding a check for the distance property in the `create_filter_options` method. Since the distance property applies to an Orbital path, we included another key in the defaault dictionary ["ORB"] to hold filters for OrbitalPath Objects.

Furthermore, we added implementation to the `apply` method of the Filter class to filter the Orbital Paths that match the filter criteria and saved the NearEarthObjects, who's Orbital Paths meet the filter criteria, to a list.

Now in the NEOSearcher class, we included implementation to in the `get_objects` method to extract Orbital Path filters and apply to the NearEarthObjects and then return the results.
