from utils import *
from detector import detect_threat
from analyzer import ai_analysis
from report import save_report

create_folders()

while True:

    banner()

    print("1. Analyze Message")
    print("2. Exit")

    choice = input("\nChoice : ")

    if choice == "1":

        text = input("\nPaste Email / Message / URL\n\n> ")

        result = detect_threat(text)

        ai = ai_analysis(text)

        print("\n========== RESULT ==========\n")

        print("Threat :", result["type"])
        print("Risk :", result["risk"], "%")
        print("Reason :", result["reason"])

        print("\nAI Recommendation\n")
        print(ai)

        save_report(text, result, ai)

        success("Report Saved Inside reports Folder")

        input("\nPress Enter...")

    elif choice == "2":
        break

    else:
        warning("Invalid Choice")