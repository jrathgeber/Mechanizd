import pandas as pd
import win32com.client as win32
import os
import glob
from pathlib import Path

def get_company_csv_files(directory="."):
    """
    Find all CSV files that could be company user lists.
    Assumes naming convention like 'company_name_users.csv' or similar.
    """
    csv_files = glob.glob(os.path.join(directory, "*.csv"))
    return csv_files

def read_company_users(csv_file_path):
    """
    Read company user list from CSV file.
    Expected columns: Username, Company, Role, Email
    """
    try:
        df = pd.read_csv(csv_file_path)
        
        # Validate CSV structure
        expected_columns = ['Username', 'Company', 'Role', 'Email']
        if len(df.columns) >= 4:
            # Assume first 4 columns are Username, Company, Role, Email
            df.columns = expected_columns + list(df.columns[4:])
        else:
            print(f"Warning: {csv_file_path} doesn't have expected 4 columns")
            return None
        
        # Clean up data
        df = df.dropna(subset=['Email'])  # Remove rows without email
        df['Username'] = df['Username'].astype(str).str.strip()
        df['Company'] = df['Company'].astype(str).str.strip()
        df['Role'] = df['Role'].astype(str).str.strip()
        df['Email'] = df['Email'].astype(str).str.strip()
        
        return df
        
    except Exception as e:
        print(f"Error reading {csv_file_path}: {e}")
        return None

def create_company_wide_email(users_df, company_name, subject, message_body, attachment_path=None):
    """
    Create a single email to all users in a company.
    """
    try:
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)  # 0 = olMailItem
        
        # Get all email addresses
        email_list = users_df['Email'].tolist()
        
        # Set email properties
        mail.To = "; ".join(email_list)
        mail.Subject = f"{subject} - {company_name}"
        
        # Create personalized body
        user_count = len(users_df)
        full_body = f"Dear {company_name} Team,\n\n"
        full_body += message_body + "\n\n"
        full_body += f"This message is being sent to all {user_count} users in your organization.\n\n"
        full_body += "Best regards,\n[Your Name]"
        
        mail.Body = full_body
        
        # Add attachment if provided
        if attachment_path and os.path.exists(attachment_path):
            mail.Attachments.Add(os.path.abspath(attachment_path))
        
        # Save as draft
        mail.Save()
        
        print(f"✓ Created company-wide email draft for {company_name} ({user_count} recipients)")
        return True
        
    except Exception as e:
        print(f"✗ Error creating company-wide email for {company_name}: {e}")
        return False

def create_individual_user_emails(users_df, company_name, subject, message_body, attachment_path=None):
    """
    Create individual emails for each user in a company.
    """
    outlook = win32.Dispatch('outlook.application')
    success_count = 0
    error_count = 0
    
    for index, user in users_df.iterrows():
        try:
            mail = outlook.CreateItem(0)  # 0 = olMailItem
            
            username = user['Username']
            email = user['Email']
            role = user['Role']
            
            # Set email properties
            mail.To = email
            mail.Subject = f"{subject} - {company_name}"
            
            # Create personalized body
            full_body = f"Dear {username},\n\n"
            full_body += message_body + "\n\n"
            full_body += f"This message is specifically for you as a {role} at {company_name}.\n\n"
            full_body += "Best regards,\n[Your Name]"
            
            mail.Body = full_body
            
            # Add attachment if provided
            if attachment_path and os.path.exists(attachment_path):
                mail.Attachments.Add(os.path.abspath(attachment_path))
            
            # Save as draft
            mail.Save()
            
            print(f"✓ Created individual email draft for {username} ({role}) - {email}")
            success_count += 1
            
        except Exception as e:
            print(f"✗ Error creating email for {username}: {e}")
            error_count += 1
    
    return success_count, error_count

def process_single_company(csv_file_path, email_type, subject, message_body, attachment_path=None):
    """
    Process a single company CSV file.
    """
    print(f"\nProcessing: {os.path.basename(csv_file_path)}")
    print("-" * 50)
    
    # Read company users
    users_df = read_company_users(csv_file_path)
    if users_df is None or users_df.empty:
        print("No valid user data found in this file.")
        return
    
    # Get company name (assume it's consistent in the Company column)
    company_name = users_df['Company'].iloc[0]
    
    print(f"Company: {company_name}")
    print(f"Total users: {len(users_df)}")
    
    if email_type == "1":  # Company-wide email
        create_company_wide_email(users_df, company_name, subject, message_body, attachment_path)
    
    elif email_type == "2":  # Individual emails
        success, errors = create_individual_user_emails(users_df, company_name, subject, message_body, attachment_path)
        print(f"Individual emails created: {success}")
        print(f"Errors: {errors}")

def process_all_companies(directory, email_type, subject, message_body, attachment_path=None):
    """
    Process all company CSV files in a directory.
    """
    csv_files = get_company_csv_files(directory)
    
    print(f"Found {len(csv_files)} CSV files in directory: {directory}")
    
    for csv_file in csv_files:
        process_single_company(csv_file, email_type, subject, message_body, attachment_path)

def display_menu():
    """
    Display the main menu options.
    """
    print("\n" + "="*60)
    print("COMPANY USER EMAIL SYSTEM")
    print("="*60)
    print("1. Send company-wide email (one email to all users per company)")
    print("2. Send individual emails (separate email to each user)")
    print("3. Exit")
    print("-"*60)

def get_email_details():
    """
    Get email subject, body, and attachment from user.
    """
    print("\nEmail Details:")
    print("-" * 30)
    
    subject = input("Enter email subject: ").strip()
    if not subject:
        subject = "Important Notification"
    
    print("\nEnter email message body (press Enter twice to finish):")
    message_lines = []
    while True:
        line = input()
        if line == "":
            if message_lines and message_lines[-1] == "":
                break
        message_lines.append(line)
    
    message_body = "\n".join(message_lines).strip()
    if not message_body:
        message_body = "Please see the attached information."
    
    attachment_path = input("\nEnter attachment file path (optional, press Enter to skip): ").strip()
    if attachment_path and not os.path.exists(attachment_path):
        print(f"Warning: Attachment file '{attachment_path}' not found.")
        attachment_path = None
    
    return subject, message_body, attachment_path

def select_companies():
    """
    Let user select which companies to process.
    """
    directory = input("\nEnter directory containing company CSV files (or press Enter for current directory): ").strip()
    if not directory:
        directory = "."
    
    csv_files = get_company_csv_files(directory)
    
    if not csv_files:
        print(f"No CSV files found in directory: {directory}")
        return [], directory
    
    print(f"\nFound CSV files:")
    for i, file in enumerate(csv_files, 1):
        print(f"{i}. {os.path.basename(file)}")
    
    print(f"{len(csv_files) + 1}. Process ALL files")
    
    choice = input(f"\nSelect files to process (1-{len(csv_files) + 1}) or 'all': ").strip().lower()
    
    if choice == 'all' or choice == str(len(csv_files) + 1):
        return csv_files, directory
    
    try:
        selected_index = int(choice) - 1
        if 0 <= selected_index < len(csv_files):
            return [csv_files[selected_index]], directory
        else:
            print("Invalid selection. Processing all files.")
            return csv_files, directory
    except ValueError:
        print("Invalid input. Processing all files.")
        return csv_files, directory

def main():
    """
    Main function to run the company user email system.
    """
    while True:
        display_menu()
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "3":
            print("Goodbye!")
            break
        
        if choice not in ["1", "2"]:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue
        
        # Get email details
        subject, message_body, attachment_path = get_email_details()
        
        # Select companies to process
        selected_files, directory = select_companies()
        
        if not selected_files:
            continue
        
        # Confirm before processing
        print(f"\nSummary:")
        print(f"Email Type: {'Company-wide' if choice == '1' else 'Individual'}")
        print(f"Subject: {subject}")
        print(f"Files to process: {len(selected_files)}")
        print(f"Attachment: {attachment_path if attachment_path else 'None'}")
        
        confirm = input("\nProceed? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Operation cancelled.")
            continue
        
        # Process selected files
        print(f"\nProcessing emails...")
        print("="*60)
        
        for csv_file in selected_files:
            process_single_company(csv_file, choice, subject, message_body, attachment_path)
        
        print(f"\nCompleted! Check your Outlook Drafts folder.")
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
