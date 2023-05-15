from tkinter import *
import sqlite3


root = Tk()
root.title('Hospital Database')
root.iconbitmap('E:/Lessons/Python/GUI/Pics/icons/ico/database.ico')
root.geometry('400x400')

# DataBases

# Create DB (or connect)
conn = sqlite3.connect('hospital.db')

# Cursor
c = conn.cursor()

# Create Tables
# Doctor
c.execute('''CREATE TABLE IF NOT EXISTS doctors (
            first_name text,
            last_name text,
            department_number integer,
            room_number integer,
            phone_number integer,
            opd_start integer,
            opd_end integer
)
''')
# Appointments
c.execute('''CREATE TABLE IF NOT EXISTS appointments (
            p_first_name text,
            p_last_name text,
            dr_first_name text,
            dr_last_name text,
            p_phone_number integer,
            submit_time integer
)
''')
# Patients
c.execute('''CREATE TABLE IF NOT EXISTS patients (
            first_name text,
            last_name text,
            age integer,
            ward_number integer,
            disease text,
            phone_number integer
)
''')

# Commit Changes
conn.commit()

# Close Connection
conn.close()


# Create Functions

def doctor():
    global dr_window
    dr_window = Tk()
    dr_window.title('Doctors Information')
    dr_window.iconbitmap('E:/Lessons/Python/GUI/Pics/icons/ico/database.ico')
    dr_window.geometry('660x560')

    # Create Labels
    title_label = Label(dr_window, text='Doctors Information List', font=('Helvetica', 12, 'bold'))
    title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

    first_name_label = Label(dr_window, text='First Name')
    first_name_label.grid(row=1, column=0, padx=20, pady=5)
    last_name_label = Label(dr_window, text='Last Name')
    last_name_label.grid(row=2, column=0, padx=20, pady=5)
    department_number_label = Label(dr_window, text='Department Number')
    department_number_label.grid(row=3, column=0, padx=20, pady=5)
    room_number_label = Label(dr_window, text='Room Number')
    room_number_label.grid(row=4, column=0, padx=20, pady=5)
    phone_number_label = Label(dr_window, text='Phone Number')
    phone_number_label.grid(row=5, column=0, padx=20, pady=5)
    opd_starting_label = Label(dr_window, text='OPD Starting')
    opd_starting_label.grid(row=6, column=0, padx=20, pady=5)
    opd_ending_label = Label(dr_window, text='OPD Ending')
    opd_ending_label.grid(row=7, column=0, padx=20, pady=5)

    global first_name_entry_dr
    global last_name_entry_dr
    global department_number_dr_entry
    global room_number_entry_dr
    global phone_number_entry_dr
    global opd_starting_entry_dr
    global opd_ending_entry_dr
    global del_button_entry_dr

    # Create Entry boxes
    first_name_entry_dr = Entry(dr_window, width=40)
    first_name_entry_dr.grid(row=1, column=1, padx=20, pady=5)
    last_name_entry_dr = Entry(dr_window, width=40)
    last_name_entry_dr.grid(row=2, column=1, padx=20, pady=5)
    department_number_dr_entry = Entry(dr_window, width=40)
    department_number_dr_entry.grid(row=3, column=1, padx=20, pady=5)
    room_number_entry_dr = Entry(dr_window, width=40)
    room_number_entry_dr.grid(row=4, column=1, padx=20, pady=5)
    phone_number_entry_dr = Entry(dr_window, width=40)
    phone_number_entry_dr.grid(row=5, column=1, padx=20, pady=5)
    opd_starting_entry_dr = Entry(dr_window, width=40)
    opd_starting_entry_dr.grid(row=6, column=1, padx=20, pady=5)
    opd_ending_entry_dr = Entry(dr_window, width=40)
    opd_ending_entry_dr.grid(row=7, column=1, padx=20, pady=5)

    # Create Buttons
    add_button_label_dr = Label(dr_window, text='Add Record To Database', width=40)
    add_button_label_dr.grid(row=8, column=0, padx=20, pady=(20, 5))
    add_button_dr = Button(dr_window, text='Submit', width=35, command=dr_add_record)
    add_button_dr.grid(row=8, column=1, padx=20, pady=(20, 5))

    del_button_dr = Button(dr_window, text='Delete Record by ID', bg='yellow', width=25, command=dr_del_record)
    del_button_dr.grid(row=9, column=0, padx=20, pady=(15, 5))
    del_button_entry_dr = Entry(dr_window, width=40)
    del_button_entry_dr.grid(row=9, column=1, padx=20, pady=(15, 5))

    view_button_dr = Button(dr_window, text='View List', width=25, bg='light green', command=dr_view_all)
    view_button_dr.grid(row=10, column=0, padx=20, pady=(10, 5))


# Create Doctors Functions - add_record - del_record - view_all
def dr_add_record():
    # Create DB (or connect)
    conn = sqlite3.connect('hospital.db')
    # Cursor
    c = conn.cursor()

    # INSERT INTO TABLE
    c.execute('INSERT INTO doctors VALUES (:first_name, :last_name, :department_number, :room_number, :phone_number,:opd_start, :opd_end)',
              {
                'first_name': first_name_entry_dr.get(),
                'last_name': last_name_entry_dr.get(),
                'department_number': department_number_dr_entry.get(),
                'room_number': room_number_entry_dr.get(),
                'phone_number': phone_number_entry_dr.get(),
                'opd_start': opd_starting_entry_dr.get(),
                'opd_end': opd_ending_entry_dr.get(),
              })

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    # Clear Entry Boxes
    first_name_entry_dr.delete(0, END)
    last_name_entry_dr.delete(0, END)
    department_number_dr_entry.delete(0, END)
    room_number_entry_dr.delete(0, END)
    phone_number_entry_dr.delete(0, END)
    opd_starting_entry_dr.delete(0, END)
    opd_ending_entry_dr.delete(0, END)


def dr_del_record():
    # Create DB (or connect)
    conn = sqlite3.connect('hospital.db')
    # Cursor
    c = conn.cursor()

    # DELETE a Record by oid
    c.execute("DELETE from doctors WHERE oid=" + del_button_entry_dr.get())

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    del_button_entry_dr.delete(0, END)


def dr_view_all():
    # Create DB (or connect)
    conn = sqlite3.connect('hospital.db')
    # Cursor
    c = conn.cursor()

    # Show List
    c.execute('SELECT oid, * FROM doctors')
    records = c.fetchall()
    # print(records)

    print_records = ''
    for record in records:
        # print_records += str(record) + '\n'
        print_records += str(record[0]) + '  ' + str(record[1]) + ' ' + str(record[2]) + '\n'

    # print(print_records)
    view_label_dr = Label(dr_window, text=print_records, width=25, bg='light green', bd=4, relief='sunken', justify='left')
    view_label_dr.grid(row=11, column=0, pady=15, ipady=5)

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()


def appointment():
    global app_window
    app_window = Tk()
    app_window.title('Appointment Documentations')
    app_window.iconbitmap('E:/Lessons/Python/GUI/Pics/icons/ico/database.ico')
    app_window.geometry('660x560')

    # Create Labels
    title_label = Label(app_window, text='Appointment Information', font=('Helvetica', 12, 'bold'))
    title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

    p_first_name_label = Label(app_window, text='Patient First Name')
    p_first_name_label.grid(row=1, column=0, padx=20, pady=5)
    p_last_name_label = Label(app_window, text='Patient Last Name')
    p_last_name_label.grid(row=2, column=0, padx=20, pady=5)

    dr_first_name_label = Label(app_window, text='Dr. First Name')
    dr_first_name_label.grid(row=3, column=0, padx=20, pady=5)
    dr_last_name_label = Label(app_window, text='Dr. Last Name')
    dr_last_name_label.grid(row=4, column=0, padx=20, pady=5)

    p_phone_number_label = Label(app_window, text='Patient Phone Number')
    p_phone_number_label.grid(row=5, column=0, padx=20, pady=5)

    submit_time_label = Label(app_window, text='Submission Time')
    submit_time_label.grid(row=6, column=0, padx=20, pady=5)

    global p_first_name_entry
    global p_last_name_entry
    global dr_first_name_entry
    global dr_last_name_entry
    global p_phone_number_entry
    global submit_time_entry
    global del_button_entry_app

    # Create Entry Boxes
    p_first_name_entry = Entry(app_window, width=40)
    p_first_name_entry.grid(row=1, column=1, padx=20, pady=5)
    p_last_name_entry = Entry(app_window, width=40)
    p_last_name_entry.grid(row=2, column=1, padx=20, pady=5)

    dr_first_name_entry = Entry(app_window, width=40)
    dr_first_name_entry.grid(row=3, column=1, padx=20, pady=5)
    dr_last_name_entry = Entry(app_window, width=40)
    dr_last_name_entry.grid(row=4, column=1, padx=20, pady=5)

    p_phone_number_entry = Entry(app_window, width=40)
    p_phone_number_entry.grid(row=5, column=1, padx=20, pady=5)

    submit_time_entry = Entry(app_window, width=40)
    submit_time_entry.grid(row=6, column=1, padx=20, pady=5)

    # Create Buttons
    add_button_label_app = Label(app_window, text='Add Record To Database', width=40)
    add_button_label_app.grid(row=8, column=0, padx=20, pady=(20, 5))
    add_button_app = Button(app_window, text='Submit', width=35, command=app_add_record)
    add_button_app.grid(row=8, column=1, padx=20, pady=(20, 5))

    del_button_app = Button(app_window, text='Delete Record by ID', bg='yellow', width=25, command=app_del_record)
    del_button_app.grid(row=9, column=0, padx=20, pady=(15, 5))
    del_button_entry_app = Entry(app_window, width=40)
    del_button_entry_app.grid(row=9, column=1, padx=20, pady=(15, 5))

    view_button_app = Button(app_window, text='View List', width=25, bg='light blue', command=app_view_all)
    view_button_app.grid(row=10, column=0, padx=20, pady=(10, 5))


# Create Appointment Functions - add_record - del_record - view_all
def app_add_record():
    # Create DB (or connect)
    conn = sqlite3.connect('hospital.db')
    # Cursor
    c = conn.cursor()

    # INSERT INTO TABLE
    c.execute(
        'INSERT INTO appointments VALUES (:p_first_name, :p_last_name, :dr_first_name, :dr_last_name, :p_phone_number,:submit_time)',
        {
            'p_first_name': p_first_name_entry.get(),
            'p_last_name': p_last_name_entry.get(),
            'dr_first_name': dr_first_name_entry.get(),
            'dr_last_name': dr_last_name_entry.get(),
            'p_phone_number': p_phone_number_entry.get(),
            'submit_time': submit_time_entry.get(),
        })

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    # Clear Entry Boxes
    p_first_name_entry.delete(0, END)
    p_last_name_entry.delete(0, END)
    dr_first_name_entry.delete(0, END)
    dr_last_name_entry.delete(0, END)
    p_phone_number_entry.delete(0, END)
    submit_time_entry.delete(0, END)


def app_del_record():
    # Create DB (or connect)
    conn = sqlite3.connect('hospital.db')
    # Cursor
    c = conn.cursor()

    # DELETE a Record by oid
    c.execute("DELETE from appointments WHERE oid=" + del_button_entry_app.get())

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    del_button_entry_app.delete(0, END)


def app_view_all():
    # Create DB (or connect)
    conn = sqlite3.connect('hospital.db')
    # Cursor
    c = conn.cursor()

    # Show List
    c.execute('SELECT oid, * FROM appointments')
    records = c.fetchall()
    # print(records)

    print_records = ''
    for record in records:
        # print_records += str(record) + '\n'
        print_records += str(record[0]) + '  ' + str(record[1]) + ' ' + str(record[2]) + '\n'

    view_label_app = Label(app_window, text=print_records, width=25, bg='light blue', bd=4, relief='sunken', justify='left')
    view_label_app.grid(row=11, column=0, pady=15, ipady=5)

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()


def patient():
    global pat_window
    pat_window = Tk()
    pat_window.title('Patients Information')
    pat_window.iconbitmap('E:/Lessons/Python/GUI/Pics/icons/ico/database.ico')
    pat_window.geometry('660x560')

    # Create Labels
    title_label = Label(pat_window, text='Patients Information', font=('Helvetica', 12, 'bold'))
    title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

    first_name_label = Label(pat_window, text='First Name')
    first_name_label.grid(row=1, column=0, padx=20, pady=5)
    last_name_label = Label(pat_window, text='Last Name')
    last_name_label.grid(row=2, column=0, padx=20, pady=5)
    age_label = Label(pat_window, text='Age')
    age_label.grid(row=3, column=0, padx=20, pady=5)
    disease_label = Label(pat_window, text='Disease')
    disease_label.grid(row=4, column=0, padx=20, pady=5)
    ward_number_label = Label(pat_window, text='Ward Number')
    ward_number_label.grid(row=5, column=0, padx=20, pady=5)
    phone_number_label = Label(pat_window, text='Phone Number')
    phone_number_label.grid(row=6, column=0, padx=20, pady=5)

    global first_name_entry_pat
    global last_name_entry_pat
    global age_entry_pat
    global disease_entry_pat
    global ward_number_entry_pat
    global phone_number_entry_pat
    global del_button_entry_pat

    # Create Entry Boxes
    first_name_entry_pat = Entry(pat_window, width=40)
    first_name_entry_pat.grid(row=1, column=1, padx=20, pady=5)
    last_name_entry_pat = Entry(pat_window, width=40)
    last_name_entry_pat.grid(row=2, column=1, padx=20, pady=5)
    age_entry_pat = Entry(pat_window, width=40)
    age_entry_pat.grid(row=3, column=1, padx=20, pady=5)
    disease_entry_pat = Entry(pat_window, width=40)
    disease_entry_pat.grid(row=4, column=1, padx=20, pady=5)
    ward_number_entry_pat = Entry(pat_window, width=40)
    ward_number_entry_pat.grid(row=5, column=1, padx=20, pady=5)
    phone_number_entry_pat = Entry(pat_window, width=40)
    phone_number_entry_pat.grid(row=6, column=1, padx=20, pady=5)

    # Create Buttons
    add_button_label_pat = Label(pat_window, text='Add Record To Database', width=40)
    add_button_label_pat.grid(row=7, column=0, padx=20, pady=(20, 5))
    add_button_pat = Button(pat_window, text='Submit', width=35, command=pat_add_record)
    add_button_pat.grid(row=7, column=1, padx=20, pady=(20, 5))

    del_button_pat = Button(pat_window, text='Delete Record by ID', bg='yellow', width=25, command=pat_del_record)
    del_button_pat.grid(row=8, column=0, padx=20, pady=(15, 5))
    del_button_entry_pat = Entry(pat_window, width=40)
    del_button_entry_pat.grid(row=8, column=1, padx=20, pady=(15, 5))

    view_button_pat = Button(pat_window, text='View List', width=25, bg='light gray', command=pat_view_all)
    view_button_pat.grid(row=9, column=0, padx=20, pady=(10, 5))


# Create Patients Functions - add_record - del_record - view_all
def pat_add_record():
    # Create DB (or connect)
    conn = sqlite3.connect('hospital.db')
    # Cursor
    c = conn.cursor()

    # INSERT INTO TABLE
    c.execute(
        'INSERT INTO patients VALUES (:first_name, :last_name, :age, :ward_number, :disease,:phone_number)',
        {
            'first_name': first_name_entry_pat.get(),
            'last_name': last_name_entry_pat.get(),
            'age': age_entry_pat.get(),
            'ward_number': ward_number_entry_pat.get(),
            'disease': disease_entry_pat.get(),
            'phone_number': phone_number_entry_pat.get(),
        })

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    first_name_entry_pat.delete(0, END)
    last_name_entry_pat.delete(0, END)
    age_entry_pat.delete(0, END)
    disease_entry_pat.delete(0, END)
    ward_number_entry_pat.delete(0, END)
    phone_number_entry_pat.delete(0, END)


def pat_del_record():
    # Create DB (or connect)
    conn = sqlite3.connect('hospital.db')
    # Cursor
    c = conn.cursor()

    # DELETE a Record by oid
    c.execute("DELETE from patients WHERE oid=" + del_button_entry_pat.get())

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    del_button_entry_pat.delete(0, END)


def pat_view_all():
    # Create DB (or connect)
    conn = sqlite3.connect('hospital.db')
    # Cursor
    c = conn.cursor()

    # Show List
    c.execute('SELECT oid, * FROM patients')
    records = c.fetchall()
    # print(records)

    print_records = ''
    for record in records:
        # print_records += str(record) + '\n'
        print_records += str(record[0]) + '  ' + str(record[1]) + ' ' + str(record[2]) + '\n'

    view_label_pat = Label(pat_window, text=print_records, width=25, bg='light gray', bd=4, relief='sunken', justify='left')
    view_label_pat.grid(row=10, column=0, pady=15, ipady=5)

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()


# Root Labels
root_label = Label(root, text="Hospital's Database", font=('Helvetica', 12, 'bold'))
root_label.grid(row=0, column=0, padx=20, pady=20, )

# Create Main Buttons
dr_button = Button(root, text='Doctors Information', command=doctor, width=50, bg='light green')
dr_button.grid(row=1, column=0, padx=20, pady=15, ipady=15)

app_button = Button(root, text='Appointment Documentations', command=appointment, width=50, bg='light blue')
app_button.grid(row=2, column=0, padx=20, pady=15, ipady=15)

pat_button = Button(root, text='Patients Information', command=patient, width=50, bg='light gray')
pat_button.grid(row=3, column=0, padx=20, pady=15, ipady=15)


root.mainloop()