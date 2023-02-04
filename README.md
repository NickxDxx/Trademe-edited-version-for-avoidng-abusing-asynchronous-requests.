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
![ALL](https://user-images.githubusercontent.com/124453554/216780564-8cc5cbcd-a11a-4269-9f33-8550eff8e504.png)
![Asking price](https://user-images.githubusercontent.com/124453554/216780577-289206bc-5741-4525-a9dc-2cce6e231a85.png)
![Screenshot 2023-01-12 173701](https://user-images.githubusercontent.com/124453554/216780603-2658711b-052f-4997-b809-841fb02a7c65.png)
![Screenshot 2023-01-12 170420](https://user-images.githubusercontent.com/124453554/216780620-e70c4fcc-e51c-4944-98f3-67d5ca5e39f9.png)
