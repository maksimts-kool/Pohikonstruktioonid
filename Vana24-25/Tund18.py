from re import sub
import smtplib
from email.message import EmailMessage
import ssl
from tkinter import filedialog

def saadakiri():
    message = EmailMessage()
    message['Subject'] = input("Teema: ")
    message['To'] = input("Kellele saata: ")
    message['From'] = "maksimtsitkool@gmail.com"
    # message.set_content(input("Sisu: "))
    message.set_content(
"""<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
        }
        .timetable {
            width: 80%;
            margin: 50px auto;
            border-collapse: collapse;
            box-shadow: 0 2px 5px #ccc;
        }
        .timetable th, .timetable td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: center;
        }
        .timetable th {
            background-color: #4CAF50;
            color: white;
        }
        .day-column {
            background-color: #f2f2f2;
            font-weight: bold;
        }
        .timetable tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .timetable tr:hover {
            background-color: #f1f1f1;
        }
    </style>
</head>
<body>
    <h1 style="text-align: center;">School Timetable</h1>
    <table class="timetable">
        <tr>
            <th>Day</th>
            <th>8:00 - 9:00</th>
            <th>9:00 - 10:00</th>
            <th>10:00 - 11:00</th>
            <th>11:00 - 12:00</th>
            <th>1:00 - 2:00</th>
            <th>2:00 - 3:00</th>
        </tr>
        <tr>
            <td class="day-column">Monday</td>
            <td>Math</td>
            <td>English</td>
            <td>History</td>
            <td>Science</td>
            <td>Art</td>
            <td>Physical Education</td>
        </tr>
        <tr>
            <td class="day-column">Tuesday</td>
            <td>Biology</td>
            <td>Math</td>
            <td>Computer Science</td>
            <td>Geography</td>
            <td>Music</td>
            <td>English</td>
        </tr>
        <tr>
            <td class="day-column">Wednesday</td>
            <td>Chemistry</td>
            <td>History</td>
            <td>Math</td>
            <td>Physical Education</td>
            <td>English</td>
            <td>Art</td>
        </tr>
        <tr>
            <td class="day-column">Thursday</td>
            <td>Physics</td>
            <td>Math</td>
            <td>History</td>
            <td>Music</td>
            <td>Computer Science</td>
            <td>Science</td>
        </tr>
        <tr>
            <td class="day-column">Friday</td>
            <td>Math</td>
            <td>English</td>
            <td>Geography</td>
            <td>Biology</td>
            <td>Art</td>
            <td>Physical Education</td>
        </tr>
    </table>
</body>
</html>""", subtype="html")

    salasona = input("Salasona: ").replace(" ", "")  # aaaa aaaa aaaa aaaa

    fail = filedialog.askopenfilename(title="Vali fail", filetypes=[("All files", "*.*")])
    with open(fail, "rb") as f:
        failisisu = f.read()
        failinimi = fail.split("/")[-1]
        message.add_attachment(failisisu, maintype="image", subtype="octet-stream", filename=failinimi)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls(context=ssl.create_default_context())
        server.login("maksimtsitkool@gmail.com", salasona)
        server.send_message(message)

if __name__ == "__main__":
    saadakiri()
    print("E-mail saadetud!")