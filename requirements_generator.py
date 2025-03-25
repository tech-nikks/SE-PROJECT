import subprocess
import sys

def generate_requirements():
    """
    Generate requirements.txt using pip list command
    """
    try:
        # Run pip list command and capture output
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'list'], 
            capture_output=True, 
            text=True
        )
        
        # Process the output
        lines = result.stdout.strip().split('\n')[2:]  # Skip header lines
        
        # Extract package names and versions
        requirements = [
            f"{line.split()[0]}=={line.split()[1]}" 
            for line in lines 
            if line.strip()  # Ensure line is not empty
        ]
        
        # Write to requirements.txt
        with open('requirements.txt', 'w') as f:
            f.write('\n'.join(requirements))
        
        print(f"Generated requirements.txt with {len(requirements)} packages.")
    
    except Exception as e:
        print(f"Error generating requirements: {e}")

if __name__ == "__main__":
    generate_requirements()