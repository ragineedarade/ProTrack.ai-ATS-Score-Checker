 <h1>ProTrack.ai [ATS]</h1> 
Overview<br>
ProTrack.ai is an AI-driven Applicant Tracking System (ATS) designed to evaluate resumes against job descriptions efficiently. The system addresses common challenges faced during recruitment by providing automated and unbiased analysis of resumes, reducing manual effort, and enhancing decision-making.
<br>
Problem Statement<br><hr>
Employers struggle with efficiently screening resumes against job descriptions.<bbr></bbr>
Existing ATS solutions lack comprehensive analysis, missing context or specific skills.<br>
Manual evaluation is time-consuming and prone to bias.
Core Features
Resume Evaluation: Automatically evaluates resumes against job descriptions.
Professional Analysis: Highlights strengths, weaknesses, and missing keywords.
Match Percentage: Calculates and displays the match percentage between resumes and job descriptions.
Report Generation: Generates detailed evaluation reports.
Scope: <hr>
In Scope:
Accepts resumes in PDF format for evaluation.
Evaluates any job description provided by the user.
Provides insights such as keyword matching and strengths based on ATS criteria.
Out of Scope:
Resumes in formats other than PDF (e.g., DOCX, TXT).
Industry-specific in-depth analysis.
Manual feedback or customizations beyond ATS evaluations.
Functional Requirements
Resume Upload: Accepts PDF format resumes.
Job Description Input: Allows users to input job descriptions.
ATS Match Percentage: Calculates and displays the match percentage.
Evaluation Report: Highlights strengths, weaknesses, and missing keywords in resumes.
Non-Functional Requirements
Performance: Provides results within 10–15 seconds.
Usability: Simple interface requiring no technical expertise.
Scalability: Supports simultaneous uploads by multiple users.
Security: Ensures secure storage and handling of resumes to protect user privacy.
Tech Stack
Programming Language: Python
Libraries:
PIL
google.generativeai
Pdf2image
Streamlit
dotenv
Tools:
Virtual Environment
VS Code
AI Tools
External Tools: Peppler (external software)
API: Google Generative AI
Installation and Setup
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/ProTrack.ai-ATS.git  
cd ProTrack.ai-ATS  
Set Up Virtual Environment:

bash
Copy code
python -m venv venv  
source venv/bin/activate  # For Linux/Mac  
venv\Scripts\activate     # For Windows  
Install Dependencies:

bash
Copy code
pip install -r requirements.txt  
Environment Configuration:

Create a .env file in the root directory.
Add API keys and configurations.
Run the Application:

bash
Copy code
streamlit run app.py  
Contribution
Contributions are welcome! Follow these steps:

Fork the repository.
Create a feature branch:
bash
Copy code
git checkout -b feature-name  
Commit changes:
bash
Copy code
git commit -m "Add feature description"  
Push to the branch:
bash
Copy code
git push origin feature-name  
Open a pull request.
License
This project is licensed under the MIT License.

Contact
For questions or collaboration, reach out to:

Email: ragineedarade@gmail.com
LinkedIn: raginee_darade
This README includes all essential details about your project. Let me know if you’d like additional refinements or specific sections added!
