# Converts .cnf files into lists and expressions for py to process


def convert_file(one_file):
    # Skip lines starting with c
    # Read lines starting with p and extrack num_var and num_clauses
        # Return a object (num_var , clauses)
        with open(one_file,'r') as file:
            clauses = []
            for line in file:
                if not line.strip():
                    # If empty lines skip it
                    continue
                if line.startswith('c'):
                    # if the line starts with c skip it
                    continue 
                if line.startswith('p'):
                    # if the line stats with p get the vars and clauses
                    parts = line.split()
                    num_vars = int(parts[2])
                    num_clauses = int(parts[3])

                if line.strip().endswith('0'):
                    # Split the clauses line
                    clauses_parts = line.split()
                    # Remove the trailing 0 
                    clauses_parts = clauses_parts[:-1]
                    clause = [int(x) for x in clauses_parts]
                    clauses.append(clause)
            # Return the num of vars and clauses
            return num_vars,clauses 



