# a legal data collection module using the python requests library

# import all the required libraries
import requests
from bs4 import BeautifulSoup
import re


# next step is to load the webpage in Python
# loading the Legal Terms Dictionary - State of Connecticut branch
web_page = requests.get("https://www.jud.ct.gov/legalterms.htm")


# getting all the contents
contents = web_page.content
soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify())


words_and_meanings = {}
all_paragraphs = soup.find_all('p', {'class': 'text'})
all_strong_words = []
# all_corr_meanings = []
for each_paragraph in all_paragraphs:
    strong_words = each_paragraph.find('strong')
    # words_meanings = each_paragraph.text.split(": ", 1)
    if strong_words is not None:
        all_strong_words.append(strong_words.text)
        # all_corr_meanings.append(words_meanings)
# print(len(all_strong_words))
# print(all_corr_meanings)
# print(all_strong_words)


# # match_pattern = re.compile(r'')
# # we're using raw string to match the words
# for word in all_strong_words:
#     text = word.text
#     if len(text) > 1:
#         pattern = re.compile(r'[^\|0]')
#         if re.match(pattern, text) is not None:
#             legal_terms.append(word.text)
# print(legal_terms, "\n", len(legal_terms))

# now it's time to clean up the data
# we'll have to remove the \r\n\t, and escape sequences as such
unclean_terms = all_strong_words
legal_terms = []
for each_term in unclean_terms:
    removal_terms = ["\n", "\t", "\r", ":"]
    for term in removal_terms:
        if term in each_term:
            each_term = each_term.replace(term, "")
    if each_term != "A":
        legal_terms.append(each_term.strip())
        # stripping for removing all the leading and trailing spaces
    
print(legal_terms, "\n", len(legal_terms))

# # add all the data into a csv file
import csv

with open("legal_terms.csv", mode='w') as legal_terms_file:
    legal_writer = csv.writer(legal_terms_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    legal_writer.writerow(['LEGAL_TERMS'])
    for each_term in legal_terms:
        legal_writer.writerow([each_term])

# for each_term, index in enumerate(legal_terms):
#     for each_set in all_corr_meanings:
#         if each_term in all_corr_meanings:
#             print(all_corr_meanings[index][1])
<<<<<<< HEAD


# we've got 303 legal terms from the legal terms dictionary successfully :)
# OUTPUT 

##
##
# ['AKA', 'Accelerated Rehabilitation', 'Acknowledgment', 'Action', 'Adjournment', 'Adjudicatory Hearing', 'Adult Court Transfer', 'Adult Probation', 
# 'Affirmation', 'Affidavit', 'Alcohol Education Program', 'Alford Doctrine', 'Alimony', 'Allegation', 'Alternate Juror', 'Alternative Detention Program', 
# 'Alternative Dispute Resolution', 'Alternative Incarceration Center', 'Alternative Sanctions', 'Amicus Curiae brief', 'Annulment', 'Answer', 'Appeal', 
# 'Appeal Bond', 'Appearance', 'Appellant', 'Appellee', 'Arbitration', 'Arraignment', 'Arrest', 'Arrearages', 'Assignment List', 'Assistant Attorney General', 
# 'Attachment', 'Attorney of Record', 'Automatic Orders', 'Bail', 'Bail Bondsperson', 'Bail Commissioner', 'Bar', 'Best Interest of the Child', 'Bench Warrant', 
# 'Bond', 'Bond Forfeiture (calling the Bond)', 'Bond Review', 'Bondsman', 'Brief', 'Broken Down Irretrievably', 'Calendar', 'Calendar Call', 'Capias Mittimus', 
# 'Capital Felony', 'Case', 'Case Conference', 'Case File', 'Case Flow Coordinator', 'Central Transportation Unit', 'Certify', 'CGS', 'Challenge', 'Charge', 
# 'Charge to Jury', 'Chattels', 'Child', 'Child Support', '"', 'CIP', 'Civil Action', 'Claim', 'Classification and Program Officer', 'Common Law', 'Community Service', 
# 'Community Services Coordinator', 'Community Service Labor Program', 'Complaint', 'Complex Litigation', 'Conditional Discharge', 'Contempt of Court', 'Continuance',
# 'Continuance Date', 'Contract', 'Conviction', 'Costs', 'Count', 'Counter Claim', 'Court-Appointed Attorney', 'Court Clerk', 'Court Interpreter', 'Court Monitor', 'Court Reporter', 'Court Services Officer', 'Court Trial', 'Crime Victim 
# Compensation Program', 'Cross-Examination', 'Custody', 'Custody Affidavit', 'Damages', 'Day Incarceration Center', 'Declaration', 'Default', 'Defendant',
#  'Delinquent', 'Deposition', 'Detention Hearing or Detention Release Hearing', 'Discovery', 'Dismissal', 'Dismissal Without Prejudice', 'Dispose', 'Disposition', 
# 'Dissolution', 'Diversionary Programs', 'Docket', 'Docket Number', 'Domicile', 'Drug Court', 'Education Program', 'Ejectment', 'Electronic Monitoring', 
# 'Emancipated Minor', 'Emancipation', 'Eminent Domain', 'Eviction', 'Evidence', 'Ex Parte', 'Execution Suspended', 'Failure to Appear', 'Family Relations Counselor', 
# 'Family Support Magistrate', 'Family Violence Education Program', 'Family Violence Victim Advocate', 'Family With Service Needs', 'Felony', 'Felony Murder', 
# 'Financial Affidavit Short | Long -', 'Finding', 'Foreclosure', 'Foreman', 'Garnishment', 'GA - Geographical Area', 'Grievance', 'Guardian', 'Guardian Ad Litem', 
# 'Habeas Corpus', 'Hearsay', 'Honor Court', 'Housing Specialist', 'Hung Jury', 'Incarceration', 'Income Withholding Order', 'Indigent', 'Information (the)', 
# 'Infraction', 'Injunction', 'Interpreter', 'Interrogatory', 'Investigatory Grand Jury', 'Judge', 'Judgment', 'Judgment File', 'Juris Number', 'Jurisdiction', 
# 'Juror', 'Jury Charge', 'Jury Instructions', 'Juvenile Court', 'Juvenile Delinquent', 'Juvenile Detention', 'Juvenile Detention Center', 'Juvenile Detention Officer', 'Juvenile 
# Matters', 'Juvenile Probation', 'Juvenile Transportation Officer', 'Law Librarian', 'Legal Aid or Legal Services', 'Legal Custody', 'Legal Separation', 'Lien',
#  'Lis Pendens', 'Litigant', 'Lockout', 'Magistrate', 'Mandamus', 'Marshal', 'Mediation', 'Minor', 'Misdemeanor', 'Mitigating Circumstances', 'Mittimus Judgment', 
# 'Modification', 'Motion', 'Movant', 'Moving Party', 'Murder with Special Circumstances', 'Ne Exeat', 'Neglected Minor', 'No Contact Order', 'No Fault Divorce',
#  'Nolle', 'Nolo Contendere', 'No Contest', 'Non-Suit', 'Notarize', 'Oath', 'Office of Adult Probation', 'Order', 'Order to Detain', 
# 'Order of Detention (Detention Order)', 'Orders of Temporary Custody', 'Parcel', 'Parenting Education Program', 'Parole', 'Parties', 'Party', 'Paternity', 
# 'Pendente lite order', 'Peremptory Challenge', 'Perjury', 'Petition', 'Petitioner', 'Plaintiff', 'Plea', 'Plea Bargain', 'Pleadings', 'Posting Bond', 'Post Judgment',
#  'Practice Book', 'Pre-Sentence Investigation', 'Pretrial', 'Pretrial Hearing', 'Probable Cause Hearing', 'Probate/Probate Court', 'Probation', 'Probation Absconder', 
# 'Promise to Appear', 'Pro Se', 'Pro se Divorce', 'Prosecute', 'Prosecutor', 'Protective Order', 'Public Defender', 'Ready', 'Record', 'Referee', 
# 'Regional Child Protection Docket', 'Regional Family Trial Docket', 'Residential Treatment Programs', 'Respondent', 'Rest', 'Restitution', 'Restraining Order', 
# 'Return Date', 'Revocation Hearing', 
# 'Rule to Show Cause', 'Seal', 'Senior Judge', 'Sentences', 'Sentencing', 'Sentence Modification', 'Sentence Review', 'Serious Juvenile Offender', 
# 'Serious Juvenile Offense', 'Service', 'Short Calendar', 'Slip Opinions', 'Small Claims', 'Special Sessions of the Superior Court', 'State Referee', 
# 'States Attorney', 'Statute', 'Statute of Limitations', 'Stay', 'Stipulation', 'Subpoena', 'Subpoena Duces Tecum', 'Substance Abuse Education', 'ubstitute Charge',
#  'Summary Process', 'Summons', 'Summons (Juvenile)', 'Testimony', 'Time Served', 'Title', 'Tort', 'Transcript', 'Transfer', 'Transfer Hearing', 'Trial De Novo', 
# 'Trial Referee', 'Uncared For', 'Unconditional Discharge', 'Vacate', 'Venue', 'Victim Services Advocate', 'Visitation', 'Violation', 'Violation of Probation', 
# 'Voir Dire', 'Wage Execution', 'Wage Withholding', 'Witness', 'Writ', 'Youth', 'Youthful Offender']
#  303

##
##
=======
>>>>>>> 9cc3375462c3199c6f7ee294e4148a4e1301570d
