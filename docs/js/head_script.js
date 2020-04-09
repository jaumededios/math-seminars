
var monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

var timezoneNames = {
	'-07:00':' (Los Angeles, PDT)',
	'-04:00':' (New York, EDT)',
	'+02:00':' (Barcelona, Paris, CEST)'
}

function parseISOString(s) {
  var b = s.split(/\D+/).map(Number);
  return new Date(Date.UTC(b[0], b[1], b[2], b[3], b[4]));
}


function doublezero(i){
	return (i<10)?'0'+parseInt(i):parseInt(i)
}

function offset_string(offset){
	sgn = (offset>0)?'-':'+' 
	offset = Math.abs(offset)
	base = sgn+doublezero(offset/60)+":"+doublezero(offset%60)
	extra = timezoneNames[base]
	extra = (extra == undefined)?'':extra
	return 'UTC '+base+extra
}

function nicestring(d){
	month = monthNames[d.getMonth()-1];
	day = d.getDate();
	year = d.getFullYear();
	hour = d.getHours();
	ampm = ['am','pm'][parseInt((hour+1)/12)];
	hour = (hour-1)%12+1;
	minute = d.getMinutes();
	minute = (minute<10)?'0'+minute:minute;
	hourmin = hour+':'+minute+ampm;
	if(hourmin=='12:00pm') hourmin='12:00 (noon)';
	if(hourmin=='12:00am') hourmin='12:00 (midnight)';
	offset_value = offset_string(d.getTimezoneOffset());
	return month+' '+day+', '+year+' '+hourmin+' '+offset_value
}


function starter (){
	var timedom, date
	d = document.getElementsByClassName('time-USER')
	for(var i = 0; i<d.length;i++){
			timedom = d[i].getElementsByTagName('time')[0];
			date = parseISOString(timedom.dateTime.slice(0,-10));
			timedom.innerHTML = nicestring(date);
		try{}
		catch(err){
		}
	}
};

window.onload = starter;

(function(f, a, t, h, o, m){
a[h]=a[h]||function(){
(a[h].q=a[h].q||[]).push(arguments)
};
o=f.createElement('script'),
m=f.getElementsByTagName('script')[0];
o.async=1; o.src=t; o.id='fathom-script';
m.parentNode.insertBefore(o,m)
})(document, window, 'https://cdn.usefathom.com/tracker.js', 'fathom');
fathom('set', 'siteId', 'PILBPKTH');
fathom('trackPageview');