# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: TeamPulse
import argparse

def main():
    parser = argparse.ArgumentParser(description="TeamPulse CLI")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status").help("show status")
    sub.add_parser("checkin").help("checkin")
    sub.add_parser("blocker").help("add blocker")
    sub.add_parser("summary").help("weekly summary")
    args = parser.parse_args()
    if args.command == "status":
        print("TeamPulse running")
    elif args.command == "checkin":
        mood = input("Mood (good/neutral/bad): ")
        print(f"Checked in: {mood}")
    elif args.command == "blocker":
        desc = input("Blocker: ")
        print(f"Added blocker: {desc}")
    elif args.command == "summary":
        print("Weekly summary ready")

if __name__ == "__main__":
    main()
