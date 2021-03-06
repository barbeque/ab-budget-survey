# AB budget survey
In 2015, the Alberta government issued a survey for how it should adapt the budget to deal with the low price of oil.

Later they released the raw (but trimmed of comments) [results from the survey](http://data.alberta.ca/data/budget-2015-survey) on their open data portal.

The original document is a large (13MB) Excel document. Some friends were interested in using common data analysis tools, but the format of the data as presented was unsuitable for a relational database. As such, I wrote these utilities to help extract some of the data to facilitate a much easier translation process for them.

This repository is a work in progress and should not be taken as a finished product by any means.

## Key terminology
This document appears quickly translated from the results and as such has a lot of governmentese and TLAs.

Here's a partial list of what I think they stand for:
 * PIT = Provincial income tax
  * Graduated PIT probably means "progressive income tax."
 * PST = Provincial sales tax 