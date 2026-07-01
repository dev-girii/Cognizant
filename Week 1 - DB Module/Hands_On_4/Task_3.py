import time
import psycopg2 # type: ignore
import psycopg2.extras # type: ignore

DB_CONFIG = {
    "dbname": "college_db",
    "user": "postgres",
    "password": "dharan06#",
    "host": "localhost",
    "port": "5432"
}

def simulate_n_plus_one():
    """
    Step 56: Simulates the inefficient N+1 problem.
    Fetches N enrollments, then makes a separate database call for EVERY row.
    """
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    query_count = 0
    start_time = time.time()
    
    cur.execute("SELECT student_id, course_id, grade FROM enrollments;")
    enrollments = cur.fetchall()
    query_count += 1
    
    results = []
    for row in enrollments:
        cur.execute("SELECT first_name, last_name FROM student WHERE student_id = %s;", (row['student_id'],))
        student = cur.fetchone()
        query_count += 1
        
        results.append({
            "name": f"{student['first_name']} {student['last_name']}" if student else "Unknown",
            "grade": row['grade']
        })
        
    duration = time.time() - start_time
    cur.close()
    conn.close()
    return query_count, duration, len(results)

def execute_optimized_join():
    """
    Step 57: Resolves the N+1 problem using a single database round-trip.
    Retrieves enrollment items and student names in a single JOIN query.
    """
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    query_count = 0
    start_time = time.time()
    
    # Single optimized query fetching all columns in one trip
    optimized_query = """
        SELECT 
            CONCAT(s.first_name, ' ', s.last_name) AS full_name,
            e.grade
        FROM enrollments e
        JOIN student s ON e.student_id = s.student_id;
    """
    cur.execute(optimized_query)
    enrollments = cur.fetchall()
    query_count += 1
    
    results = []
    for row in enrollments:
        results.append({
            "name": row['full_name'],
            "grade": row['grade']
        })
        
    duration = time.time() - start_time
    cur.close()
    conn.close()
    return query_count, duration, len(results)

if __name__ == "__main__":
    print("--- Starting Database Performance Benchmark ---")
    try:
        # Run N+1 Simulation
        n1_queries, n1_time, n1_rows = simulate_n_plus_one()
        print(f"\n[Approach 1: N+1 Anti-Pattern]")
        print(f"Total DB Queries Executed: {n1_queries}")
        print(f"Total Rows Handled:       {n1_rows}")
        print(f"Total Execution Time:     {n1_time:.4f} seconds")
        
        # Run Optimized Join Method
        join_queries, join_time, join_rows = execute_optimized_join()
        print(f"\n[Approach 2: Single JOIN Query]")
        print(f"Total DB Queries Executed: {join_queries}")
        print(f"Total Rows Handled:       {join_rows}")
        print(f"Total Execution Time:     {join_time:.4f} seconds")
        
        # Performance Summary Log
        print(f"\n[Performance Verdict]")
        print(f"Saved {n1_queries - join_queries} network round-trips to the database.")
        print(f"Optimized approach was {n1_time / max(join_time, 0.0001):.1f}x faster.")
        
    except psycopg2.OperationalError:
        print("\nError: Could not connect to PostgreSQL server.")
        print("Please check your DB_CONFIG credentials and ensure the database is active.")
        
        
# Verdict:
# For 10000 records, the N+1 Pattern takes 10001 round trips
# Optimized JOIN Query takes only 1 round trip and 1 query is executed 