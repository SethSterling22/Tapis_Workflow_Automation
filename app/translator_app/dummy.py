# Simple dummy script to simulate NL processing
import sys

def main():
    print("--- Tapis Dummy Scientific Task Starting ---")
    
    # Simulate reading the input argument defined in app-definition.json
    input_file = sys.argv[1] if len(sys.argv) > 1 else "no_input.txt"
    print(f"Reading input from: {input_file}")
    
    print("Processing Natural Language... [DONE]")
    print("Translating to Scientific Language... [DONE]")
    
    # Feedback simulation
    print("Result: {'status': 'success', 'code': 200, 'msg': 'Hello from TACC HPC'}")
    print("--- Task Completed ---")

if __name__ == "__main__":
    main()