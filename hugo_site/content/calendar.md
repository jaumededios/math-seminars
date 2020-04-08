+++
  title = "Calendar View"
  type = "about"
  hidden = "true"
  Kind="about"
  URL = "calendar"
  ________________________________________________=""
  hack = "The line below is a hack, working on it"
  publishDate = "2000-01-01T00:00:00-00:00"
+++
<script type="text/javascript">
	var urlstr = '<iframe id = "CalendarFrame" src="https://calendar.google.com/calendar/embed?height=600&amp;wkst=2&amp;bgcolor=%23ffffff&amp;ctz={}&amp;src=a2EwN2xjc2FucWhhbnJpa2ppMjZ2OXJibXNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&amp;color=%23D50000&amp;mode=WEEK"style="border:solid 1px #777" width="800" height="600" frameborder="0" scrolling="no"></iframe>'

	offset = -(new Date()).getTimezoneOffset()/60

	tzstr = {
		"-7" : "America%2FLos_Angeles",
		"-6" : "America%2FCosta_Rica",
		"-5" : "America%2FChicago",
		"-4" : "America%2FNew_York",
		"1" : "Europe%2FLondon",
		"2" : "Europe%2FMadrid"
	}

	

	changer = function(){
		str = tzstr[String(offset)]
		console.log(str)
		if (str !== undefined){
			document.getElementById('CalHolder').innerHTML = urlstr.replace('{}', str)
		}
	}
	window.onload = changer

</script>
<div id = 'CalHolder'>
<iframe id = 'CalendarFrame' src="https://calendar.google.com/calendar/embed?height=600&amp;wkst=2&amp;bgcolor=%23ffffff&amp;ctz=America%2FLos_Angeles&amp;src=a2EwN2xjc2FucWhhbnJpa2ppMjZ2OXJibXNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&amp;color=%23D50000&amp;mode=WEEK" style="border:solid 1px #777" width="800" height="600" frameborder="0" scrolling="no"></iframe>
</div>