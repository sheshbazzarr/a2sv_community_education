import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    rename=['student_id','first_name','last_name','age_in_years']
    students.columns=rename
    return students