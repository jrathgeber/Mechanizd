import pandas as pd
import win32com.client as win32
import os
from pathlib import Path

def read_survey_questions(excel_file_path):
    """
    Read survey questions from Excel file.
    Assumes questions are in the first column of the first sheet.
    """
    try:
        df = pd.read_excel(excel_file_path, sheet_name=0)
        # Get the first column (assuming it contains questions)
        questions = df.iloc[:, 0].dropna().tolist()
        return questions
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return []

def format_questions_for_email(questions):
    """
    Format survey questions nicely for email body.
    """
    if not questions:
        return "No survey questions found."
    
    formatted_text = "Dear Recipient,\n\n"
    formatted_text += "Please find below the survey questions. You can either:\n"
    formatted_text += "1. Reply to this email with your answers, or\n"
    formatted_text += "2. Fill out the attached Excel survey form\n\n"
    formatted_text += "SURVEY QUESTIONS:\n"
    formatted_text += "=" * 50 + "\n\n"
    
    for i, question in enumerate(questions, 1):
        formatted_text += f"{i}. {question}\n\n"
        formatted_text += "   Answer: ____________________\n\n"
    
    formatted_text += "=" * 50 + "\n\n"
    formatted_text += "Thank you for your time and participation!\n\n"
    formatted_text += "Best regards,\n"
    formatted_text += "[Your Name]"
    
    return formatted_text

def create_outlook_drafts(csv_file_path, excel_file_path, subject="Survey Request"):
    """
    Create Outlook email drafts for each person in the CSV file.
    """
    # Check if files exist
    if not os.path.exists(csv_file_path):
        print(f"Error: CSV file '{csv_file_path}' not found.")
        return
    
    if not os.path.exists(excel_file_path):
        print(f"Error: Excel file '{excel_file_path}' not found.")
        return
    
    try:
        # Read CSV file
        df = pd.read_csv(csv_file_path)
        
        # Validate CSV structure
        if len(df.columns) < 3:
            print("Error: CSV file must have at least 3 columns (Name, Email, Company)")
            return
        
        # Assume first 3 columns are Name, Email, Company
        df.columns = ['Name', 'Email', 'Company'] + list(df.columns[3:])
        
        # Read survey questions from Excel
        questions = read_survey_questions(excel_file_path)
        email_body = format_questions_for_email(questions)
        
        # Initialize Outlook application
        outlook = win32.Dispatch('outlook.application')
        
        success_count = 0
        error_count = 0
        
        # Create email draft for each person
        for index, row in df.iterrows():
            try:
                name = str(row['Name']).strip()
                email = str(row['Email']).strip()
                company = str(row['Company']).strip()
                
                # Skip rows with missing essential data
                if pd.isna(row['Name']) or pd.isna(row['Email']) or email == '':
                    print(f"Skipping row {index + 1}: Missing name or email")
                    continue
                
                # Create mail item
                mail = outlook.CreateItem(0)  # 0 = olMailItem
                
                # Set email properties
                mail.To = email
                mail.Subject = f"{subject} - {company}" if company and company != 'nan' else subject
                
                # Personalize email body
                personalized_body = email_body.replace("Dear Recipient,", f"Dear {name},")
                if company and company != 'nan':
                    personalized_body = personalized_body.replace(
                        "Thank you for your time and participation!",
                        f"Thank you for your time and participation on behalf of {company}!"
                    )
                
                mail.Body = personalized_body
                
                # Attach Excel file
                mail.Attachments.Add(os.path.abspath(excel_file_path))
                
                # Save as draft (don't send)
                mail.Save()
                
                print(f"✓ Created draft for {name} ({email}) - {company}")
                success_count += 1
                
            except Exception as e:
                print(f"✗ Error creating draft for row {index + 1}: {e}")
                error_count += 1
        
        print(f"\nSummary:")
        print(f"Successfully created {success_count} email drafts")
        print(f"Errors: {error_count}")
        print(f"Drafts are saved in your Outlook Drafts folder")
        
    except Exception as e:
        print(f"Error: {e}")

def main():
    """
    Main function to run the email draft generator.
    """
    print("Outlook Email Draft Generator")
    print("=" * 40)
    
    # Get file paths from user
    csv_file = input("Enter CSV file path (or press Enter for 'contacts.csv'): ").strip()
    if not csv_file:
        csv_file = "contacts.csv"
    
    excel_file = input("Enter Excel survey file path (or press Enter for 'survey.xlsx'): ").strip()
    if not excel_file:
        excel_file = "survey.xlsx"
    
    subject = input("Enter email subject (or press Enter for 'Survey Request'): ").strip()
    if not subject:
        subject = "Survey Request"
    
    print(f"\nProcessing...")
    print(f"CSV file: {csv_file}")
    print(f"Excel file: {excel_file}")
    print(f"Subject: {subject}")
    print("-" * 40)
    
    # Create the email drafts
    create_outlook_drafts(csv_file, excel_file, subject)

if __name__ == "__main__":
    # Example of how to use the functions directly
    # create_outlook_drafts("contacts.csv", "survey.xlsx", "Customer Satisfaction Survey")
    
    # Or run the interactive version
    main()
