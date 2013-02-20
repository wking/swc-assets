# What Would You Teach If You Had a Week?

Assume people know:

* Basic Unix shell: ls, cd, grep, find, for, environment variables
* Basic Python: lists, loops, file I/O, import, dictionaries, functions
  * But *not* how to write classes
* Basic SQL: where, join, NULL, group by, sum()
* Basic regular expressions
* Version control
* Unit testing

Budget is 30 hr (5 days * 6 hr/day)
Content is:

* Major data problems (1 hr)
  * Dealing with data that is very large
  * Dealing with data that changes quickly
  * Missing data
  * Misaligned discretizations (binning ticks, mixed units, ...)
* Basic data formats and trade offs (7 hr)
  * CSV + gzip (human readable but redundancy and errors make it difficult to use)
  * XML / JSON (structured and well supported, but god forgive you if there is a stray '>')
  * HDF5 (best of many worlds)
  * Custom Binary (faster and smaller at the cost of flexibility and portability)
* Exploring and learning from data (8 hr)
  * Basic regression analysis
  * classification
  * Ranking
  * PCA
* Databases (8 hr)
  * When do we go beyond files and require services
  * Database design
  * What is NoSQL
  * Examples of when and where
* Scaling (6 hr)
  * Hadoop and MapReduce
  * Other similar technologies
