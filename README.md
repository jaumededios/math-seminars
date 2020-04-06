# Math-seminars
A list of open math seminars around the world.

I am looking for collaborators, if you want to help me mantain and expand this list, message me!

## How to contribute/suggest changes

The talks are stored in the folder `hugo_site/content/talk`, and have the following format:

```
+++
  host= "the_host"
  date = "2020-03-31T14:00:00-07:00" 
  expiryDate = "2020-03-31T14:50:00-07:00"
  title = "This is the title of the talk"
  speaker = "mathematician"
  speaker_institution = "the_university"
  URL = "url at the_host that holds"
  categories = ["AP", "CO", "NT", "anything that goes after math. in arXiv"]
  ________________________________________________=""
  hack = "The line below is a hack, working on it - do not touch it"
  publishDate = "2000-00-00T00:00:00-00:00"
+++

Here you goes the abstract abstract
single line jumps will be ommited 

Double line jumps will do a paragraph change
LaTex is OK.
```

If you send me talks in this format to `jaumededios at math dot ucla dot edu` I will add them here. The criteria that I have been using so far are:

* The talk has a page at a university research group that I can link to.
* The talk has a publicly available zoom/bluepants/other ID in that page, or the page advertises that the ID will be added at some point. 
* I am currently not posting talks where the organizers state that an ID will be given to people who email them only (unless I get explicit permission from the organizers, I don't want them to be spammed - I might change my mind on this in the future).

If you know git and want to be helpful, you can do a pull-request instead.
