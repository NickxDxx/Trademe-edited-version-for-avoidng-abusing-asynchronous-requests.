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


![Screenshot 2023-01-02 163936](https://user-images.githubusercontent.com/124453554/216780865-9addbefe-0b6a-4475-9972-d08ea4b5a9a1.png)
![ALL](https://user-images.githubusercontent.com/124453554/216780871-f947eb60-06d7-466a-96e1-e0d41ba2a77c.png)
![Asking price offical ](https://user-images.githubusercontent.com/124453554/216780885-88274428-3859-4911-a258-704d21fe7c46.png)
