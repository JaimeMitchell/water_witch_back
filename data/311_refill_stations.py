from geopy.geocoders import BatchGeocoder


addresses = ["PS 188 at 442 E. Houston St.", "MS 54 at 103 W. 107th St.", "PS 149 at 34 W. 118th St.",
             "PS 50 at 433 E. 100th St.", "PS 123 at 301 W. 140th St.", "George Washington HS at 549 Audubon Ave.",
             "Dry Dock Playground at Szold Pl. between 10th St and Ave. D", "The Battery Oval between State St. and Battery Pl.",
             "Plaza De Las Americas on 175th St. between Broadway and Wadsworth Ave.",
             "P.S. 33 at 70 Tompkins Avenue", "M.S. 50 at 183 South 3rd Street", "M.S. 71 at 215 Heyward Street",
             "M.S. 320 at 46 McKeever Place", "M.S. 390 at 1224 Park Place", "M.S. 232 at 905 Winthrop Street",
             "M.S. 117 at 300 Willoughby Avenue", "M.S. 291 at 231 Palmetto Street", "Boys and Girls H.S. at 1700 Fulton Street",
             "Automotive H.S. at 50 Bedford Avenue", "South Shore H.S. at 6565 Flatlands Avenue", "Franklin K. Lane H.S. at 999 Jamaica Avenue",
             "Betsy Head Playground between Dumont Avenue and Thomas S. Boyland Street", "Cooper Park on Maspeth Avenue and Sharon Street, between Olive Street and Morgan Avenue",
             "Coffey Park on Verona Street, between Richard and Dwight Streets", "Paerdegat Park on Albany Ave and 40th Street, between Farragut Road and Foster Avenue",
             "St. Johns Recreation Center at 2151 Prospect Place", "Lindower Park at Strickland Avenue, between Miller Avenue and East 60th Place",
             "Fox Square on Fulton Street and Flatbush Avenue Extension", "Humboldt Plaza on Humboldt Street between Moore and Varet Streets",
             "Knickerbocker Plaza on Myrtle Avenue, between Knickerbocker and Greene Avenues",
             "M.S. 147 at 1600 Webster Avenue", "Herbert H. Lehman HS at 3000 East Tremont Avenue", "James Monroe H.S. at 1300 Boynton Avenue",
             "William Taft HS at 240 East 172nd Street", "Theodore Roosevelt H.S. at 500 East Fordham Road", "Dewitt Clinton H.S. at 100 West Mosholu Parkway",
             "Ferry Point Park, comfort station on Schley Avenue and the LI Sound between Westchester Creek and Balcom Avenue",
             "Flushing HS at 35-01 Union St.", "Martin Van Buren HS at 230-17 Hillside Ave.", "August Martin HS at 156-10 Baisley Blvd.",
             "Richmond Hill HS at 89-30 114th St.", "John Adams HS at 101-01 Rockaway Blvd.", "MS 8 at 108-35 167th St.",
             "Ravenswood Library at 35-32 21st Street", "Little Bay Park parking lot on Cross Island Pkwy. between Utopia Pkwy. and Totten Ave.",
             "Flushing Meadows Corona Park in Field One", "Rockaway Beach and Boardwalk: Roller Hockey Rink at Beach 109th St and Shore Front Pkwy.",
             "Rockaway Beach and Boardwalk: From Beach 3rd St. to Beach 153rd St.", "Beach 20th Plaza on Beach 20th St. between Beach 21st St. and Mott Ave Queens",
             "Staten Island Museum Snug Harbor at 1000 Richmond Terr.", "Ocean Breeze Athletic Complex at 599 Father Capodanno Blvd."]

# loop through the list of addresses
refill_stations = []
geocoder = BatchGeocoder(addresses)

for location in geocoder:
    refill_stations.append(
        {'address': location.address, 'latitude': location.latitude, 'longitude': location.longitude})
    print(refill_stations)
