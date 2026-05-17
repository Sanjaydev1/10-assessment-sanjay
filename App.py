import argparse

parser = argparse.ArgumentParser(
    description="Welcome utility for Agentic AI Enablement"
)

parser.add_argument(
    "--name",
    required=True,
    help="Name of the user"
)

parser.add_argument(
    "--role",
    required=True,
    help="Role of the user"
)

args = parser.parse_args()

print(
    f"Hello {args.name}, welcome to Agentic AI Enablement as a {args.role}."
)