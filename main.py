def main():
    print("Hello from crewai-tutorial!")


if __name__ == "__main__":
     main()

"""
from crewai_tools import FileReadTool

try:
    # This initializes the tool to check if all dependencies (like lancedb) are working
    tool = FileReadTool()
    print("✅ Success! Your CrewAI Environment is perfectly set up.")
except Exception as e:
    # If there's a tiny version mismatch left, this will tell us exactly what it is
    print(f"❌ Almost there, but got this error: {e}")
"""