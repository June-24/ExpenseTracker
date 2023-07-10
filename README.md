# ExpenseTracker

This repository contains a Django Personal Expense Tracker website that you can run locally. Follow the instructions below to get started.

## Prerequisites

Make sure you have the following software installed on your system:

- Python (version 3.7 or higher)
- pip (Python package manager)

## Installation

1. Clone this repository to your local machine or download and extract the ZIP file.

2. Open a terminal or command prompt and navigate to the project's root directory.

3. Create a virtual environment by running the following command:

   ```bash
   python3 -m venv myenv
   ```
4. Activate the Virual environment:
   - on macOS and linux:
   ```bash
   source myenv/bin/activate
   ```
    - on windows:
   ```bash
   myenv\Scripts\activate
   ```
4. Install the project dependencies from the requirements.txt file:
  ```bash
pip install -r requirements.txt
```

## Running the Website
To run the Django website, execute the following command in the project's root directory:
```bash
python manage.py runserver
```
After running the command, the website will be accessible at http://localhost:8000 in your web browser.

# Description
1. This is my personal Django project that helps you to track your expenses.
- I used Tailwind CSS in designing the website \
  ![image](https://github.com/June-24/ExpenseTracker/assets/123622678/1ee50cfa-28b3-4df0-9084-9fd8ade3d248)
- To plot the charts I used the Chart.js library, Chart.js renders chart elements on an HTML5 canvas. \
  ![image](https://github.com/June-24/ExpenseTracker/assets/123622678/a755226a-e82c-48ad-a4b2-5d5b0a660346)
- The data of the expenses and all the features are stored in the SQLite database. \
  ![image](https://github.com/June-24/ExpenseTracker/assets/123622678/66475033-ad05-4d5f-a459-f1d8d14cba72)

# Images below show the Working of the Expense Tracking application
## 1. Add Expense
 ![image](https://github.com/June-24/ExpenseTracker/assets/123622678/d30c442b-aa1c-4efd-83e1-2fd665c2fcfc)
 >after adding the Keyboard expense
 ![image](https://github.com/June-24/ExpenseTracker/assets/123622678/b10a4526-5f59-4057-ab98-241a11898c01)
## 2. Expenses list
 ![image](https://github.com/June-24/ExpenseTracker/assets/123622678/9171500c-14a4-45b5-b576-980e07961df1)
 ![image](https://github.com/June-24/ExpenseTracker/assets/123622678/36a5c9b4-cd1b-4fdc-a522-87d71225a7be)
## 3. we can edit the expenses and delete them as well
### 3.1 edit
![image](https://github.com/June-24/ExpenseTracker/assets/123622678/e808455e-4701-4de6-bf32-4012694cd73b)
after edit
![image](https://github.com/June-24/ExpenseTracker/assets/123622678/491c4ffb-05e9-4671-afb5-4d98b2208f89)

### 3.2 delete
#### let us delete that updated Ipad by clickig on the delete button
![image](https://github.com/June-24/ExpenseTracker/assets/123622678/5a80370f-1aef-4d69-ac6e-594f48f66b47)
#### Ipad is gone
![image](https://github.com/June-24/ExpenseTracker/assets/123622678/e1d843b9-5e2f-491a-be87-9288d499a612)
## 4. categorical Sum and the expenses in the past 30-days
![image](https://github.com/June-24/ExpenseTracker/assets/123622678/aff950be-f5ea-4d0c-951b-4f44475b348f)
## 5. pie chart of the categorical expenses and the line chart of the daily expense sum
![image](https://github.com/June-24/ExpenseTracker/assets/123622678/1db643d4-e758-4871-80b0-19d8fe815119)




   






  



   


 
