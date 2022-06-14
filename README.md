# Data contest
## Analyze the dataset Harry Portter and then answer the following questions:
1. Which movie has the most lines of dialog? Is it also the longest movie?
2. How have the characters with the most lines of dialogue varied across movies?
3. What is the most popular location in each film?
4. Which spells are used the most across the franchise? Do characters have a favorite spell?
## Find out more insight
# Note
- In the folder "docs", the html files that their filename containing uuid . The file contains the following information:
  - Chart
  - Its description
  - Its insight
- Each chart will have its own uuid declared in the script. Therefore, in order to find out the script used to generate the html, please do the following steps:
  1. Inspect the html and then find out the value of attribute "id" having format "chart_id_\<uuid\>"
  
        For example, if you find out the following value after inspecting the html
        > chart_id_c8842f18-45aa-4d0f-a596-a9be6de37705

  2. Determine the uuid which is right after "chart_id_"
    
        Continue to the above example, the equivalent uuid will be
        > c8842f18-45aa-4d0f-a596-a9be6de37705

  3. Search the file or the block of code containing this uuid
    
        Continue to the above example, the equivalent file is
        > q4.ipynb
- We also use the above uuid as the html filename
