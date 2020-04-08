+++
  host= "MIT"
  date = "2020-04-09T12:01:00-04:00"
  expiryDate = "2020-04-09T13:00:00-04:00"
  title = "Structured cospans"
  speaker = " John Baez"
  speaker_institution = "UC Riverside"
  talk_site = "http://brendanfong.com/seminar.html"
  categories = ["CT"]

  publishDate = "2000-02-07T16:00:00-07:00"
+++

"Structured cospans" are a general way to study networks with inputs and outputs. Here we illustrate this using a type of network popular in theoretical computer science: Petri nets. An "open" Petri net is one with certain places designated as inputs and outputs. We can compose open Petri nets by gluing the outputs of one to the inputs of another. Using the formalism of structured cospans, open Petri nets can be treated as morphisms of a symmetric monoidal category - or better, a symmetric monoidal double category. We explain two forms of semantics for open Petri nets using symmetric monoidal double functors out of this double category. The first, an operational semantics, gives for each open Petri net a category whose morphisms are the processes that this net can carry out. The second, a "reachability" semantics, simply says which markings of the outputs can be reached from a given marking of the inputs. This is joint work with Kenny Courser and Jade Master.