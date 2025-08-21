import pandas as pd

EMPLOYEE_DATA_PATH = "employee_data.csv"
employee_df = pd.read_csv(EMPLOYEE_DATA_PATH)

def lookup_employee(query: str) -> str:
    """Smarter employee dataset search & analytics."""
    q = query.lower()

    if "count" in q:
        for position in employee_df["Position"].unique():
            if position.lower() in q:
                count = len(employee_df[employee_df["Position"].str.lower() == position.lower()])
                return f"There are {count} employees with the job title '{position}'."
        return "Couldn't match a job title for the count query."

    if "average" in q and "salary" in q:
        for position in employee_df["Position"].unique():
            if position.lower() in q:
                avg_salary = employee_df.loc[
                    employee_df["Position"].str.lower() == position.lower(),
                    "Salary"
                ].mean()
                return f"The average salary for {position}s is {avg_salary:,.0f}."
        return "Couldn't match a job title for the average salary query."

    if "highest" in q or "max" in q:
        top = employee_df.loc[employee_df["Salary"].idxmax()]
        return f"The highest paid employee is a {top['Position']} with {top['Experience (Years)']} years experience earning {top['Salary']:,.0f}."

    if "lowest" in q or "min" in q:
        low = employee_df.loc[employee_df["Salary"].idxmin()]
        return f"The lowest paid employee is a {low['Position']} with {low['Experience (Years)']} years experience earning {low['Salary']:,.0f}."

    results = employee_df[
        employee_df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)
    ]
    if results.empty:
        return "No matching employee record found in the dataset."
    return results.to_string(index=False)
