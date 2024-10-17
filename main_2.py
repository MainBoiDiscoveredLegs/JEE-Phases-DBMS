# before runnnig, go to cmd >>python -m pip install -U prettytable
# and run create_db_stuff()
# and change the mycntr for you db specs

import tkinter as tk
from tkinter import messagebox, simpledialog, Text, Scrollbar, Frame
import mysql.connector as sql
from prettytable import PrettyTable

# this guy for your db
mycntr = sql.connect(
    host="localhost",
    user="root",
    password="mysql@123123",
    database="JEE_DB"
) 
mycur = mycntr.cursor()

def create_db_stuff():
    #PHASE 1 MATH
    mycur.execute('create table PHASE_1_MATH(Sno integer primary key,chapter char(20),status_ char(20) default "❌");')
    mycur.execute('insert into PHASE_1_MATH values(1,"Quadratic Equations","❌");')
    mycur.execute('insert into PHASE_1_MATH values(2,"Logarithm","❌");)')
    mycur.execute('insert into PHASE_1_MATH values(3,"Trigonometry","❌");')
    mycur.execute('insert into PHASE_1_MATH values(4,"Basic Calculus","❌");')
    mycur.execute('insert into PHASE_1_MATH values(5,"Sets, Relations, Functions","❌");')
    mycur.execute('insert into PHASE_1_MATH values(6,"Linear Inequalities","❌");')

    #PHASE 1 PHY
    mycur.execute("CREATE TABLE PHASE_1_PHY (Sno INTEGER PRIMARY KEY,chapter CHAR(20),status_ CHAR(20) DEFAULT '❌');")
    mycur.execute('insert into PHASE_1_PHY values(1,"Vectors","❌");')
    mycur.execute('insert into PHASE_1_PHY values(2,"Kinematics","❌");')
    mycur.execute('insert into PHASE_1_PHY values(3,"Laws and Motion","❌");')
    mycur.execute('insert into PHASE_1_PHY values(4,"Units and Dimensions","❌");')
    
    #PHASE 1 CHEM
    mycur.execute('create table PHASE_1_CHEM(Sno integer primary key,chapter char(20),status_ char(20) default "❌");')
    mycur.execute('insert into PHASE_1_CHEM values(1,"Atomic Structure","❌");')
    mycur.execute('insert into PHASE_1_CHEM values(2,"BCC","❌");')
    mycur.execute('insert into PHASE_1_CHEM values(3,"Periodic Properties","❌");')
    mycur.execute('insert into PHASE_1_CHEM values(4,"Stoichiometry","❌");')

    #PHASE 2 MATH
    mycur.execute('create table PHASE_2_MATH(Sno integer primary key,chapter char(30),status_ char(20) default "❌");')
    mycur.execute('insert into PHASE_2_MATH values(1,"Complex Numbers","❌");')
    mycur.execute('insert into PHASE_2_MATH values(2,"Progression and Series","❌");')
    mycur.execute('insert into PHASE_2_MATH values(3,"Straight Lines","❌");')
    mycur.execute('insert into PHASE_2_MATH values(4,"Circle","❌");')

    #PHASE 2 PHY
    mycur.execute('create table PHASE_2_PHY(Sno integer primary key,chapter char(30),status_ char(20) default "❌");')
    mycur.execute('insert into PHASE_2_PHY values(1,"Work Energy Power","❌");')
    mycur.execute('insert into PHASE_2_PHY values(2,"Conservation of Momentum","❌");')
    mycur.execute('insert into PHASE_2_PHY values(3,"Rotational Motion","❌");')

    #PHASE 2 CHEM
    mycur.execute('create table PHASE_2_CHEM(Sno integer primary key,chapter char(50),status_ char(20) default "❌");')
    mycur.execute('insert into PHASE_2_CHEM values(1,"Chemical Bonding","❌");')
    mycur.execute('insert into PHASE_2_CHEM values(2,"Group 1 and Group 2","❌");')
    mycur.execute('insert into PHASE_2_CHEM values(3,"Hydrogen and it\'s Compounds","❌");')
    mycur.execute('insert into PHASE_2_CHEM values(4,"Gaseous State","❌");')
    mycur.execute('insert into PHASE_2_CHEM values(5,"Thermodynamics","❌");')

    #PHASE 3 MATH
    mycur.execute('create table PHASE_3_MATH(Sno integer primary key,chapter char(20),status_ char(20) default "❌");')
    mycur.execute('insert into PHASE_3_MATH values(1,"Limits","❌");')
    mycur.execute('insert into PHASE_3_MATH values(2,"Parabola","❌");')
    mycur.execute('insert into PHASE_3_MATH values(3,"Hyperbola","❌");')
    mycur.execute('insert into PHASE_3_MATH values(4,"Elipse","❌");')

    #PHASE 3 PHY
    mycur.execute('create table PHASE_3_PHY(Sno integer primary key,chapter char(20),status_ char(20) default "❌");')
    mycur.execute('insert into PHASE_3_PHY values(1,"Gravitation","❌");')
    mycur.execute('insert into PHASE_3_PHY values(2,"FLuids","❌");')

    #PHASE 3 CHEM
    mycur.execute('create table PHASE_3_CHEM(Sno integer primary key,chapter char(40),status_ char(20) default "❌");')
    mycur.execute('insert into PHASE_3_CHEM values(1,"Chemical Equilibrium","❌");')
    mycur.execute('insert into PHASE_3_CHEM values(2,"Inoic Equilibrium","❌");')
    mycur.execute('insert into PHASE_3_CHEM values(3,"Group 13","❌");')
    mycur.execute('insert into PHASE_3_CHEM values(4,"Group 14","❌");')
    mycur.execute('insert into PHASE_3_CHEM values(5,"Group 15","❌");')
    mycur.execute('insert into PHASE_3_CHEM values(6,"Group 18","❌");')

    #NOTES
    mycur.execute('create table notes(file_name char(50));')

    mycon.commit()

class JEEApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JEE Phases 1-3")
        self.root.geometry("500x550")
        self.root.configure(bg="#fcfbfb")

        self.main_frame = tk.Frame(root, bg="#fcfbfb", bd=1, relief=tk.SOLID, padx=20, pady=20)
        self.main_frame.pack(pady=50)

        self.create_home_screen()

    def create_home_screen(self):
        self.clear_frame()

        ascii_art = (
            "+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+\n"
            "|\t                        \t  |\n"
            "|\t  |￣￣￣￣￣￣￣￣￣￣￣￣|\t  |\n"
            "|\t  |   JEE PHASES 1-3    |\t  |\n"
            "|\t  |＿＿＿＿＿＿＿＿＿＿＿＿|\t  |\n"
            "|\t      (\__/) ||         \t  |\n"
            "|\t      (•ㅅ•) ||          \t  |\n"
            "|\t      / づ               \t  |\n"
            "+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+"
        )

        label = tk.Label(self.main_frame, text=ascii_art, font=("Courier", 10), bg="#fcfbfb", justify='left')
        label.pack(pady=10)

        self.phase_var = tk.IntVar()

        tk.Label(self.main_frame, text="HOME SCREEN\n", font=("Courier", 14), bg="#fcfbfb").pack(pady=5)
        tk.Radiobutton(self.main_frame, text="View Phase 1", variable=self.phase_var, value=1, bg="#fcfbfb", font=("Courier", 9)).pack(anchor='w')
        tk.Radiobutton(self.main_frame, text="View Phase 2", variable=self.phase_var, value=2, bg="#fcfbfb", font=("Courier", 9)).pack(anchor='w')
        tk.Radiobutton(self.main_frame, text="View Phase 3", variable=self.phase_var, value=3, bg="#fcfbfb", font=("Courier", 9)).pack(anchor='w')
        tk.Label(self.main_frame, text="\n", font=("Helvetica", 5), bg="#fcfbfb").pack(pady=5)

        tk.Button(self.main_frame, text="NEXT", command=self.choose_subject,relief=tk.GROOVE, bg="#aace93", fg="white", font=("Courier", 9), width=5, height=1).pack(side=tk.LEFT, padx=70, pady=5)
        tk.Button(self.main_frame, text="EXIT", command=self.root.quit,relief=tk.GROOVE, bg="#db4588", fg="white", font=("Courier", 9), width=5, height=1).pack(side=tk.LEFT, padx=70, pady=5)

    def choose_subject(self):
        phase = self.phase_var.get()
        if phase == 0:
            messagebox.showwarning("Select Phase", "Please select a phase.")
            return

        self.clear_frame()

        self.subject_var = tk.StringVar()

        tk.Label(self.main_frame, text=f"CHOOSE SUBJECT FOR PHASE {phase}", font=("Courier", 14), bg="#fcfbfb").pack(pady=10)
        tk.Radiobutton(self.main_frame, text="Physics", variable=self.subject_var, value="phy", bg="#fcfbfb", font=("Courier", 9)).pack(anchor='w')
        tk.Radiobutton(self.main_frame, text="Chemistry", variable=self.subject_var, value="chem", bg="#fcfbfb", font=("Courier", 9)).pack(anchor='w')
        tk.Radiobutton(self.main_frame, text="Mathematics", variable=self.subject_var, value="math", bg="#fcfbfb", font=("Courier", 9)).pack(anchor='w')

        tk.Button(self.main_frame, text="SELECT SUBJECT", command=lambda: self.show_table(phase, self.subject_var.get()),relief=tk.GROOVE, bg="#aace93", fg="white", font=("Courier", 9), width=20, height=1).pack(pady=10)
        tk.Button(self.main_frame, text="BACK TO HOME", command=self.create_home_screen, bg="#db4588",relief=tk.GROOVE, fg="white", font=("Courier", 9), width=20, height=1).pack(pady=5)

    def show_table(self, phase, subject):
        query = f"SELECT * FROM PHASE_{phase}_{subject.upper()}"
        mycur.execute(query)
        records = mycur.fetchall()
        rec1=records.copy()

        self.clear_frame()

        tk.Label(self.main_frame, text=f"PHASE {phase} {subject.upper()}", font=("Courier", 14), bg="#fcfbfb").pack(pady=10)

        table = PrettyTable()
        table.field_names = ["Sno.", "Chapter", "Status"]
        for record in records:
            table.add_row(record)

        table_text = Text(self.main_frame, wrap='word', height=10)
        table_text.insert('1.0', str(table))
        table_text.config(state='disabled')

        scroll = Scrollbar(self.main_frame, command=table_text.yview)
        table_text['yscrollcommand'] = scroll.set

        table_text.pack(padx=50,pady=10)
        scroll.pack(side='right', fill='y')


        tk.Button(self.main_frame, text="Update Status", command=lambda: self.update_status(phase, subject),relief=tk.GROOVE, bg="#876bab", fg="white", font=("Courier", 9), width=20, height=1).pack(pady=5)
        tk.Button(self.main_frame, text="Make Notes", command=lambda: self.create_note(phase, subject), relief=tk.GROOVE,bg="#53b2bb", fg="white", font=("Courier", 9), width=20, height=1).pack(pady=5)
        tk.Button(self.main_frame, text="View Notes", command=lambda: self.view_note(phase, subject), relief=tk.GROOVE,bg="#53b2bb", fg="white", font=("Courier", 9), width=20, height=1).pack(pady=5)
        tk.Button(self.main_frame, text="BACK", command=lambda: self.choose_subject(), bg="#db4588",relief=tk.GROOVE, fg="white", font=("Courier", 9), width=20, height=1).pack(pady=5)

    def update_status(self, phase, subject):
        chapter = simpledialog.askstring("Update Status", "Enter Chapter Sno:")
        new_status = simpledialog.askstring("Update Status", "Enter New Status:")

        if chapter and new_status:
            query = f"UPDATE PHASE_{phase}_{subject.upper()} SET status_='{new_status}' WHERE Sno={chapter}"
            mycur.execute(query)
            mycntr.commit()
            messagebox.showinfo("Success", "Status updated successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter both Chapter Sno and Status.")


    def create_note(self, phase, subject):
        chapter = simpledialog.askstring("Create Notes", "Enter Chapter Sno:")

        if chapter:
            query = f"SELECT chapter FROM PHASE_{phase}_{subject.upper()} WHERE Sno = {chapter}"
            mycur.execute(query)
            result = mycur.fetchone()

            if result:
                chapter_name = result[0]
                note_window = tk.Toplevel(self.root)
                note_window.title("Enter Notes")
                note_window.geometry("400x300")
                note_window.configure(bd=1, relief=tk.SOLID)


                tk.Label(note_window, text=f"Enter your notes for\n{chapter_name}", font=("Courier", 12)).pack(pady=10)

                note_text = Text(note_window, wrap='word', height=10)
                note_text.pack(pady=10, padx=10, fill='both', expand=True)

                def save_notes():
                    note_content = note_text.get("1.0", tk.END).strip()
                    if note_content:
                        filename = f"PHASE_{phase}_{subject}_{chapter_name}.txt"
                        with open(filename, 'w') as note_file:
                            note_file.write(note_content)
                        messagebox.showinfo("Success", "Notes created successfully!")
                        note_window.destroy()
                    else:
                        messagebox.showwarning("Input Error", "Please enter some notes.")

                tk.Button(note_window, text="SAVE NOTES", command=save_notes, relief=tk.GROOVE, bg="#aace93", fg="white", font=("Courier", 9), width=20, height=1).pack(pady=10)

            else:
                messagebox.showwarning("Input Error", "Invalid Chapter Sno.")
        else:
            messagebox.showwarning("Input Error", "Please enter Chapter Sno.")




    def view_note(self, phase, subject):
        chapter = simpledialog.askstring("View Notes", "Enter Chapter Sno:")

        if chapter:
            query = f"SELECT chapter FROM PHASE_{phase}_{subject.upper()} WHERE Sno = {chapter}"
            mycur.execute(query)
            result = mycur.fetchone()

            if result:
                chapter_name = result[0]  
                filename = f"PHASE_{phase}_{subject}_{chapter_name}.txt"

                try:
                    with open(filename, 'r') as note_file:
                        notes = note_file.read()

                    self.clear_frame()

                    tk.Label(self.main_frame, text=f"Notes for {chapter_name}", font=("Courier", 12),bg="#fcfbfb").pack(pady=10)

                    notes_text = Text(self.main_frame, wrap='word', height=10)
                    notes_text.insert('1.0', notes)
                    notes_text.config(state='disabled')
                    notes_text.pack(pady=10, padx=50)

                    tk.Button(self.main_frame, relief=tk.GROOVE, text="BACK", command=lambda: self.show_table(phase, subject), bg="#db4588", fg="white", width=20, height=1).pack(pady=10)

                except FileNotFoundError:
                    messagebox.showwarning("File Not Found", "No notes found for this chapter.")
            else:
                messagebox.showwarning("Input Error", "Invalid Chapter Sno.")
        else:
            messagebox.showwarning("Input Error", "Please enter Chapter Sno.")

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = JEEApp(root)
    root.mainloop()
