#reading of CSV File
import pandas as pd
from fpdf import FPDF
data=pd.read_csv("student_habits_performance.csv")
#Analysis of CSV File
no_of_students=len(data)
average_exam_score=data["exam_score"].mean()
participation = data["extracurricular_participation"].value_counts().get("Yes", 0)
average_study_hours_per_day=data["study_hours_per_day"].mean()
average_social_media_hours=data["social_media_hours"].mean()
max_attendance_percentage=data["attendance_percentage"].max()
# PDF Report
pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)


pdf.cell(200,10,"Student Habits Performance Report",ln=True,align="C")   
pdf.ln(10)
#analysis print
pdf.set_font("Arial", size=15)
pdf.cell(200, 10, f"Total number of students: {no_of_students}", ln=True, border=1)
pdf.cell(200, 10, f"Average exam score: {average_exam_score:.2f}", ln=True, border=1)
pdf.cell(200, 10, f"Number of students in extracurriculars: {participation}", ln=True, border=1)
pdf.cell(200, 10, f"Average study hours per day: {average_study_hours_per_day:.2f}", ln=True, border=1)
pdf.cell(200, 10, f"Average social media hours: {average_social_media_hours:.2f}", ln=True, border=1)
pdf.cell(200, 10, f"Max attendance percentage: {max_attendance_percentage:.2f}%", ln=True, border=1)

# Output PDF
pdf.output("student_habits_report.pdf")