# Hospital Database
## This project stores a hospital's staff and patients information using SQLite3 and TKinter written in Python

There are three tables in the database including Doctors, Appointments and Patients. Each entity owns several specific fields, for Doctors table fields are as follows: First Name, Last Name, Department Number, Room Number, Phone and OPD starting/ending period. Likewise, for Patients table, they are First Name, Last Name, Age, Ward Number, Disease Title and Phone number. Finally, Appointments table contains full name of patients and their appointed doctor, also Phone Number and appointment's Submit Time.

In the first page of the project you can open each of the tables by their buttons, and insert the data in the boxes regarding the label and hit the "Submit" button to add them into the database. In order to see the table records you can hit the "Veiw List" button. Also for deleting an entire row in any table, you should insert the record's ID and hit the "Delete Record by ID" button. 
Checkout the output figure here: ![Capture](https://github.com/ParnianSrb/Hospital-Database/assets/82469872/2527bcc0-2ef6-4c14-b586-349908ad0273)

Installation Instructions:
1. To use python I have tried coding with PyCharm which has been easy and straightforward. Here is the link to download and install: https://www.jetbrains.com/pycharm/download/?section=windows / https://www.jetbrains.com/help/pycharm/installation-guide.html#snap
2. To use SQLite DBMS, write this code at the top and go ahead... "import sqlite3"

The purpose of this project is to store some information about a hospital and people who commute there. The storing process works well, however the code partially has some issues, like repetitive or sloppy codes. Second problem is "Veiw List" button that shows the list with some overlaps while deleting rows and changing number of the records.
