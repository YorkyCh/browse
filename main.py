#!/usr/bin/env python3

import argparse
from start import start
from create import create
from list import list


def main():
    parser = argparse.ArgumentParser(
        description="CLI tool for handling browser sessions."
    )

    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # List command
    list_parser = subparsers.add_parser("ls", help="List all items")

    # Create command
    create_parser = subparsers.add_parser("create", help="Create a new item")
    create_parser.add_argument("name", help="Name of the item to create")

    # Start command
    create_parser = subparsers.add_parser("start", help="Start a session")
    create_parser.add_argument("name", help="Name of the session required")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete an item")
    delete_parser.add_argument("name", help="Name of the item to delete")

    args = parser.parse_args()

    # Handle commands
    if args.command == "ls":
        print("Listing all items...")
        list("./sessions")

    elif args.command == "create":
        print(f"Creating item: {args.name}")
        create(args.name)

    elif args.command == "delete":
        print(f"Deleting item: {args.name}")

    elif args.command == "start":
        print(f"Starting session: {args.name}")
        start(args.name)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
