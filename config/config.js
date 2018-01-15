/* Magic Mirror Config Sample
 *
 * By Michael Teeuw http://michaelteeuw.nl
 * MIT Licensed.
 *
 * For more information how you can configurate this file
 * See https://github.com/MichMich/MagicMirror#configuration
 *
 */

var config = {
	address: "localhost", // Address to listen on, can be:
	                      // - "localhost", "127.0.0.1", "::1" to listen on loopback interface
	                      // - another specific IPv4/6 to listen on a specific interface
	                      // - "", "0.0.0.0", "::" to listen on any interface
	                      // Default, when address config is left out, is "localhost"
	port: 8080,
	ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1"], // Set [] to allow all IP addresses
	                                                       // or add a specific IPv4 of 192.168.1.5 :
	                                                       // ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.1.5"],
	                                                       // or IPv4 range of 192.168.3.0 --> 192.168.3.15 use CIDR format :
	                                                       // ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.3.0/28"],

	language: "en",
	timeFormat: 24,
	units: "metric",

	modules: [
		{
			module: "alert",
		},
		{
			module: "updatenotification",
			position: "top_bar"
		},
		{
			module: "clock",
			position: "top_left"
		},
		{
			module: "calendar",
			header: "UK Holidays",
			position: "top_left",
			config: {
				calendars: [
					{
						symbol: "calendar-check-o ",
						url: "webcal://www.calendarlabs.com/templates/ical/UK-Holidays.ics"
					}
				]
			}
		},
		//{
			//module: "compliments",
			//position: "lower_third"
		//},
		{
			module: "currentweather",
			position: "top_right",
			config: {
				location: "Cheddar",
				locationID: "2653281",  //ID from http://www.openweathermap.org/help/city_list.txt
				appid: "51066ee34801b02dd190929a963f35d1"
			}
		},
		{
			module: "weatherforecast",
			position: "top_right",
			header: "Weather Forecast",
			config: {
				location: "Cheddar",
				locationID: "2653281",  //ID from http://www.openweathermap.org/help/city_list.txt
				appid: "51066ee34801b02dd190929a963f35d1"
			}
		},
		{
			module: "newsfeed",
			position: "bottom_bar",
			config: {
				feeds: [
					{
						title: "BBC",
						url: "http://feeds.bbci.co.uk/news/rss.xml"
					}
				],
				showSourceTitle: true,
				showPublishDate: true
			}
		},
		{
  module: 'MMM-MyCommute',
  position: 'lower_third',
  config: {
    apikey: 'AIzaSyC_dkNUTgwmzPNUiiV13bc2qhvuFNW3tQA',
    origin: '65 Front St W, Toronto, ON M5J 1E6',
    startTime: '00:00',
    endTime: '23:59',
    hideDays: [0,6],
    destinations: [
      {
        destination: '14 Duncan St Toronto, ON M5H 3G8',
        label: 'Air Canada Centre',
        mode: 'walking',
        color: '#82E5AA'
      },
      {
        destination: '317 Dundas St W, Toronto, ON M5T 1G4',
        label: 'Art Gallery of Ontario',
        mode: 'transit'
      },
      {
        destination: '55 Mill St, Toronto, ON M5A 3C4',
        label: 'Distillery District',
        mode: 'bicycling'
      },
      {
        destination: '6301 Silver Dart Dr, Mississauga, ON L5P 1B2',
        label: 'Pearson Airport',
        avoid: 'tolls'
      }
    ]
  }
}
	]

};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") {module.exports = config;}
