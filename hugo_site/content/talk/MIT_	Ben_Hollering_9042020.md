+++
  host= "MIT"
  date = "2020-04-09T10:00:00-04:00"
  expiryDate = "2020-04-09T11:00:00-04:00"
  title = "	Identifiability in Phylogenetics using Algebraic Matroids"
  speaker = "	Ben Hollering"
  speaker_institution = "North Carolina State University"
  talk_site = "https://dibernstein.github.io/VirtualSeminar.html"
  categories = ["CO"]

  publishDate = "2000-02-07T16:00:00-07:00"
+++

Identifiability is a crucial property for a statistical model since it implies that distributions in the model uniquely determine the parameters that produce them. In phylogenetics, the identifiability of the tree parameter is of particular interest since it means that phylogenetic models can be used to infer evolutionary histories from data. Typical strategies for proving identifiability results require Gröbner basis computations which become untenable as the size of the model grows. In this talk I'll give some background on phylogenetic algebraic geometry and then discuss a new computational strategy for proving the identifiability of discrete parameters in algebraic statistical models that uses algebraic matroids naturally associated to the models. This algorithm allows us to avoid computing Gröbner bases and is also parallelizable.