# Calculate Distances Between Locations #

This is an extremely simple script to calculate geographic distances between cities.  Notes about the code are in the file.

If you don't have mathematica, you can look at the code with CDF Player:

http://www.wolfram.com/products/player/


# Google Apps Scripts #

In addition to the mathematica file, there are two sets of simple Google Apps Scripts that can be used as spreadsheet functions in Google Sheets.  Copy and paste the functions into the script editor of the sheet that you wish to use the custom functions.   "AppsScript-LatLng" takes the origin and destination as latitude and longitude.   "AppsScript-Text" takes origin and destination as a text address.  Here are some example calls for AppsScript-LatLng:

	=WalkTime(A2, B2, C2, D2)
	=WalkDistance(A2, B2, C2, D2)
	=DriveTime(A2, B2, C2, D2)
	=DriveDistance(A2, B2, C2, D2)

Where A2 is origin latitude, B2 is origin longitude, C2 is destination latitude and D2 is destination longitude.

Similarly, AppsScript-Text calls might look like this:

	=WalkTime(A2, B2)
	=WalkDistance(A2, B2)
	=DriveTime(A2, B2)
	=DriveDistance(A2, B2)

Where A2 is a text origin address and B2 is a text destination address.
 