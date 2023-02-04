# Asynchronous-scraping-with-hard-data-comparison-
32K listings in 20 seconds.



1. Twaek API output 500 listings dictionaries instead default 20.
2. Data comparison:
   1. Inside each listing's dictionary, all possible keys' position don't have time wasted to capture.
      keys' number random, positions fixed.
   S: Capture all possible dic keys. Split into long list(kept) and low list(filtered), 
      Each input data go through low list, filtered out any keys not inside the low list, long list keys go through filtered keys, any keys not inside filtered keys insert "/".
   2. Milliseconds date time inside dictionary value's string.
   S: Use Regrex convert all to Human knowledged date time.
3. Add Asynchronous speed up process.


