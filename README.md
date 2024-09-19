# Ultimate-NSE-Fetcher-v2
This gives you historical prices of an NSE share. It is different from Ultimate-NSE-Fetcher-v1 because:
- More functionalities
   - Log In
   - Sign Up
   - Try as a guest
   - Has a database of MySQL to store the store credentials of Sign Up and use them for Log In

- Is not on **Streamlit Community Cloud**
   - This is because I wasn't able to upload on **Streamlit Community Cloud** :disappointed:

The working: 
1. Opens the landing page

2. When you press `Sign Up`:
   - Opens `pages/page_2.py`

   - In `pages/page_2.py`:
     1. Has input fields for username, email, password
   
     2. When you press `Sign Up`
        - Opens `ultimate-nse-fetcher` table from database `accounts` on engine `engine`
        - Checks if there is `` ` `` in username
        - Checks if username exists
        - Checks if password exists
        - If any check is false it shows error of its own
        - When all checks are done successfully, credentials are added to the SQL table and we are redirected to `pages/page_3.py`

4. When you press `Log In`:
   - Opens `pages/page_1.py`

   - In `pages/page_1.py`:
      1. Has input fields for username or email, password
   
      2. When you press `Log In`: 
         - Opens `ultimate-nse-fetcher` table from database `accounts` on engine `engine`
         - Checks if username or email exists
         - Checks if the password of the corresponding username or email is correct
         - If any check is false it shows error of its own
         - If all checks are done successfully, it will redirect to `pages/page_3.py`

6. In `pages/page_3.py`:
   - Has select box for index name or NSE Share, input fields for start date, start month, start year, end date, end month, end year, checkboxes for the values to plot
     - If you press NSE Share, another text input for share name will come

   - When you press `Get Graph`:
     1. Takes data of the share/index
     2. Removing some columns to not plot
     3. Using streamlits `st.line_chart` to plot the dataframe

   - When you press `Download Prices`:
     1. Takes the data
     2. Make another buttons `Download as CSV` and `Download as Excel will come` after doing all the fetching
     3. Clicking that button downloads the data

7. When you click `Try As A Guest`:
   - Redirects to the guest version of the `pages/page_3.py` which is `pages/page_4.py`

8. In `pages/page_4.py`:
   - Has select box for index name or NSE Share, input fields for start date, start month, start year, end date, end month, end year, checkboxes for the values to plot
     - If you press NSE Share, another text input for share name will come

   - When you press `Get Graph`:
     1. Takes data of the share/index
     2. Removing some columns to not plot
     3. Using streamlits `st.line_chart` to plot the dataframe

   - When you press `Download Prices`:
     1. Takes the data
     2. Make another buttons `Download as CSV` and `Download as Excel will come` after doing all the fetching
     3. Clicking that button downloads the data

   - You can use the functionalities total 20 times after thet it throws an error

**Note:** Please fill the details of the engine with a MySQL server which is remotely accessible
**SQL code for ultimate-nse-fetcher table:**
````sql
CREATE TABLE `ultimate-nse-fetcher` (
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
````

