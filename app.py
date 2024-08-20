from flask import Flask, send_from_directory, request, jsonify

app = Flask(__name__)

# Define a dictionary for the chatbot's prompts and responses
chat_data = {
    "greeting": {
        "text": "Welcome to Finbot! How can I assist you today?",
        "options": {
            "Loan Information": "Loan Information",
            "Investment": "Investment Information"
        }
    },
    "Loan Information": {
        "text": "What exactly do you wish to know more about?",
        "options": {
            "Types of loans": "Types of loans",
            "Application Process": "Application Process",
            "Check Eligibility": "Verify Eligibility",
            "Other Informations": "Other Informations",
            "greeting":"Home"
        }
    },
    "Other Informations": {
        "text": "Please Choose what other information you are interested about here at Finclub",
        "options": {
            "Interest Rates": "Interest Rates",
            "Repayments":"Repayments",
            "Loan Duration":"Loan Duration",
            "Required Documentations": "Required Documentation",
            "Loan Information":"Back"
        }
    },
    "Interest Rates": {
        "text": "Interest rates start from 9.50% but vary based on the loan type and your credit profile.",
        "options": {
            "Interest Rate Personal Loan": "Interest Rate Personal Loan",
            "Interest Rate SME Loan": "Interest Rate SME Loan",
            "What is a Credit Profile": "What is a Credit Profile",
            "Other Informations":"Back"
        }
    },
    "Interest Rate Personal Loan": {
        "text": "Interest rates for Personal Loan starts from 9.50% but vary based on your credit profile.",
        "options": {
            "What is a Credit Profile": "What is a Credit Profile",
            "Interest Rates":"Back"
        }
    },
    "Interest Rate SME Loan": {
        "text": "Interest rates for SME Loan starts from 10% but vary based on your credit profile.",
        "options": {
            "What is a Credit Profile": "What is a Credit Profile",
            "Interest Rates":"Back"
        }
    },
    "What is a Credit Profile": {
        "text": "FinScore is our advanced credit scoring engine which identifies your credit profile. \n\nAnalyzing over 200 data points and integrated with the Bank of Mauritius's Credit Information Bureau (MCIB) to evaluate borrowers' creditworthiness based on their financial history.",
        "options": {
            "Interest Rates":"Back"
        }
    },
    "Repayments": {
        "text": "Please select what you want information on:",
        "options": {
            "When does Repayment begin": "When does Repayment begin",
            "Repayment Calculations":"Repayment Calculations",
            "Other Informations":"Back"
        }
    },
    "When does Repayment begin": {
        "text": "For loan funded and disbursed between the 1st and 15th of a month, the repayments start at the end of the month. For loans disbursed after the 15th of a month, the repayment starts at the end of the following month",
        "options": {
            "Repayments":"Back"
        }
    },
    "Repayment Calculations": {
        "text": "Monthly repayments are calculated using the reducing balance method. \nYour instalment per month will remain the same throughout the duration of your loan.",
        "options": {
            "Repayments":"Back"
        }
    },
    "Loan Duration": {
        "text": "The duration of the loan depends on the type of loan you're applying for\n\n• Kwik Cash: 1 - 6 Months\n• Consumer loan: 6 - 12 Months\n• Flexi Loan: 6 - 24 Months\n• Finpro Loan: 6 - 36 Months\n• SME Loan: 6 - 36 Months",
        "options": {
            "Other Informations":"Back"
        }
    },

    "Investment": {
        "text": "Welcome to FinClub! Start earning competitive returns while making a positive impact. \n\nJoin our secure Peer to Peer Lending platform and unlock the potential of your investments today.",
        "options": {
            "Why Finclub": "Why Finclub",
            "Register as Lender":"Register as Lender",
            "Investing Process":"Investing Process",
            "greeting":"Back"
        }
    },
    "Why Finclub": {
        "text": "Key Benefits of Lending with FinClub\n\n• Earn up to 14% p.a. in returns\n• 80% Tax Exemption on interest earned\n• 100% online, simple, and secure process\n• Flexible investment options starting from MUR 1,000\n• Monthly repayments for consistent income\n• No registration fees or hidden charges",
        "options": {
            "Investment":"Back"
        }
    },
    "Register as Lender": {
        "text": "Simply click on the “Register” button and register through by following the simple step-by-step process as instructed.\n\n• Once you have filled in the basic information and uploaded the documents required, FinClub will verify your details, approve your registration, and assign you a FinID together with your personalised Dashboard.",
        "options": {
            "Investment":"Back"
        }
    },
    "Investing Process": {
        "text": "To start, register as a Lender with FinClub:\n\n• Create your FinID with personal details and KYC documents.\n• Submit your investment application.\n• Undergo compliance checks (AML/CFT).\n• Get your application approved and FinID assigned.\n• Transfer funds to your FinClub account.\n• Choose your investment preferences.\n• Full loan amount raised; notifications sent to lenders and borrower.\n• Sign the Loan Agreement.\n• Funds disbursed to the borrower.\n• Receive monthly repayments.\n• Withdraw or reinvest to grow your wealth.",
        "options": {
            "Investment":"Back"
        }
    },
    "Types of loans": {
        "text": "At Finclub we offer 2 types of loans:\n\n1. Personal Loan\n2. SME Loan",
        "options": {
            "Personal Loans": "Personal Loans",
            "SME Loan Type": "SME Loan",
            "Check Eligibility": "Verify Eligibility",
            "Required Documentations": "Required Documentation",
            "Loan Information":"Back"
        }
    },
    "Application Process": {
        "text": "The application process logic will soon be implemented",
        "options": {
            "greeting": "Go Back"
        }
    },
    "SME Loan Type": {
        "text": "Finclub offers loans to small and medium businesses with amounts going up to MUR 1,000,000",
        "options": {
            "Personal Loans": "Personal Loans",
            "Check Eligibility": "Verify Eligibility",
            "Back":"Back"
        }
    },
    "Personal Loans": {
        "text": "There are 4 types of personal loans offered by Finclub \n\n1.Kwik Cash\n2.Consumer Loan\n3.Flexi Loan\n4.Finpro Loan",
        "options": {
            "Kwik Cash Loan Type": "Kwik Cash",
            "Consumer Loan Type": "Consumer Loan",
            "Flexi Loan Type": "Flexi Loan",
            "Finpro Loan Typ": "Finpro Loan",
            "Check Eligibility": "Verify Eligibility",
            "Back":"Back"       
        }
    },
    "Kwik Cash Loan Type": {
        "text": " Small, short-term loans ranging from MUR 10,000 to 25,000 with a duration of 1-6 months",
        "options": {
            "Personal Loans": "Back"
        }
    },
    "Consumer Loan Type": {
        "text": "For general consumer needs, available in amounts between MUR 20,000 to 50,000, with a duration of 6-12 months.",
        "options": {
            "Personal Loans": "Back"
        }
    },
    "Flexi Loan Type": {
        "text": "For more significant expenses like house renovations or weddings, ranging from MUR 50,000 to 200,000, with a duration of 6-24 months.",
        "options": {
            "Personal Loans": "Back"
        }
    },
    "Finpro Loan Type": {
        "text": " Unsecured personal loans for professionals, ranging from MUR 200,000 to 500,000, with a duration of 6-36 months.",
        "options": {
            "Personal Loans": "Back"
        }
    },
    "Check Eligibility": {
        "text": "In order to determine if you are eligible for the loan, click on verify and fill in the information.",
        "options": {
            "Verify": "Verify"
        }
    },
    "Verify": {
        "text": "Click here to verify",
        "url": "https://finclub.mu/public/sign-up/borrower/loan",
        "options": {
            "Need Help For Verification": "Need Help For Verification",
            "Other Informations": "Other Informations",
            "Loan Information":"Back"
        }
    },
    "Need Help For Verification": {
        "text": "Finbot will now guide you with the process of verifying your Eligibility",
        "options": {
            "Eligibility Help": "Start"
        }
    },
    "Eligibility Help": {
        "text": "Select if you are applying for either a single or joint loan",
        "options": {
            "Next step 1": "Next",
            "Single Loan": "What is single Loan",
            "Joint Loan": "What is joint Loan"
        }
    },
    "Single Loan": {
        "text": "A single loan, often referred to as an individual loan, is a type of loan where only one borrower is responsible for the loan.",
        "options": {
            "Eligibility Help": "Back"
        }
    },
    "Joint Loan": {
        "text": "A joint loan is a type of loan that is shared between two or more individuals. \nEach party involved in a joint loan shares the responsibility for repaying the loan",
        "options": {
            "Eligibility Help": "Back"
        }
    },
    "Next step 1": {
        "text": "Put your Email and Phone Number. Ensure both are valid email and phone number ",
        "options": {
            "Next step 2": "Next"
        }
    },
    "Next step 2": {
        "text": "Put your monthly salary and if you get other monthly income please input them as well",
        "options": {
            "Next step 3": "Next"
        }
    },
    "Next step 3": {
        "text": "Calculate the total amount of your monthly debt and input in the field",
        "options": {
            "Next step 4": "Next"
        }
    },
    "Next step 4": {
        "text": "If you have existing arrears please specify yes or no",
        "options": {
            "Next step 5": "Next"
        }
    },
    "Next step 5": {
        "text": "Moving on to the right handside of the eligibility form you will now put the loan details you wish to take",
        "options": {
            "Next step 6": "Next"
        }
    },
    "Next step 6": {
        "text": "Specify the loan type \nConsumer Loan\nFlexi Loan\nFinpro loan\nKwik Cash\nSME Loan",
        "options": {
            "Next step 8": "Next",
            "Kwik Cash":"Kwik Cash",
            "Consumer Loan":"Consumer Loan",
            "Flexi Loan":"Flexi Loan",
            "Finpro Loan":"Finpro Loan",
            "SME Loan":"SME Loan"
        }
    },
    "Kwik Cash": {
        "text": " Small, short-term loans ranging from MUR 10,000 to 25,000 with a duration of 1-6 months",
        "options": {
            "Next step 6": "Back"
        }
    },
    "Consumer Loan": {
        "text": "For general consumer needs, available in amounts between MUR 20,000 to 50,000, with a duration of 6-12 months.",
        "options": {
            "Next step 6": "Back"
        }
    },
    "Flexi Loan": {
        "text": "For more significant expenses like house renovations or weddings, ranging from MUR 50,000 to 200,000, with a duration of 6-24 months.",
        "options": {
            "Next step 6": "Back"
        }
    },
    "Finpro Loan": {
        "text": " Unsecured personal loans for professionals, ranging from MUR 200,000 to 500,000, with a duration of 6-36 months.",
        "options": {
            "Next step 6": "Back"
        }
    },
    "SME Loan": {
        "text": "For small and medium enterprises, offering MUR 50,000 to 1,000,000, with a duration of 6-36 months​​.",
        "options": {
            "Next step 6": "Back"
        }
    },
    "Next step 8": {
        "text": "Specify the purpose of the loan",
        "options": {
            "Next step 9": "Next"
        }
    },
    "Next step 9": {
        "text": "Specify the loan amount and duration of repayment",
        "options": {
            "Eligibility Completion": "Done"
        }
    },
    "Eligibility Completion": {
        "text": "Based on your provided informations the system will evaluate if you are eligible or not ",
        "options": {
            "Eligible": "I am Eligible",
            "Not Eligible": "I am not Eligible"
        }
    },
    "Not Eligible": {
        "text": "we are sorry to but in case you are dimmed as not eligible you will hence not be able to get a loan",
        "options": {
            "Other Informations": "Other Informations",
            "Back":"Back"
        }
    },
    "Eligible": {
        "text": "Congratulations you can now move on to the Application Process",
        "options": {
            "Application Process": "Aplication Process",
            "Required Documentation": "Required Documentation",
            "Back":"Back"
        }
    },
    "Application Process": {
        "text": "Awaiting the stream line of the application process to finsih the logic of this segment",
        "options": {
            "Other Informations": "Other Informations",
            "Required Documentations": "Required Documentation",
            "Loan Information":"Back"
        }
    },
    "Required Documentations": {
        "text": "You will require a set of documents to register and some other documents depending on your employment status. \n\nPlease specify your status and gather required documents",
        "options": {
            "Registration": "Registration",
            "Salaried Employee": "Salaried Employee",
            "Self-Employed": "Self-Employes",
            "Company": "Company",
            "Retired": "Retired",
            "Back":"Back"
        }
    },
    "Registration": {
        "text": "For Registration \n• Proof of Identity\n\nNIC - Front & Back (for Mauritians)\nPassport (for Foreigners)\n\n• Proof of Address (not older than 3 months)\n(only one required)\nCWA\nCEB\nMy.T\n\n• If you are a tenant\nLease Agreement or Rent Book or\nLetter from Landlord\nUtility Bill of Landlord\nNIC of Landlord\n\n• Birth Certificate",
        "options": {
            "Required Documentations": "Back"
        }
    },
    "Salaried Employee": {
        "text": "As an employee you will require these Documents \n\n• Salary Slips (Last 3 months) \n• Bank Statement (Last 6 months) \n• Proof of Additional Income (if applicable)",
        "options": {
            "Required Documentations": "Back"
        }
    },
    "Self-Employed": {
        "text": "As an Self-Employed you will require these Documents \n\n• Bank Statement (Last 12 months)\n• Latest Financial Statement – (if applicable)\n• Proof of Additional Income\n• Business Registration Certificate (BRN)\n• VAT Certificate – (if applicable)\n• Trade License (if applicable)",
        "options": {
            "Required Documentations": "Back"
        }
    },
    "Company": {
        "text": "As an Company you will require these Documents \n\n• Certificate of Incorporation\n• Bank Statement (Last 12 Months)\n• Financial Statement (Last 2 Years)\n• VAT Certificate (if applicable)\n• Trade License (if applicable)\n• Board Resolution (for taking loans through FinClub’s P2P Lending Platform)\n• Latest Financial Statement – (if applicable)\n• Proof of Additional Income (if applicable)",
        "options": {
            "Required Documentations": "Back"
        }
    },
    "Retired": {
        "text": "As an Retired Individual you will require these Documents \n\n• Bank Statement (Last 6 months)\n• Old Age Pension (if receiving fund through Post Office) - (if applicable)\n• Proof of Additional Income (if applicable)",
        "options": {
            "Required Documentations": "Back"
        }
    },
    "Back": {
        "text": "At Finclub we offer 2 types of loans:\n\n1. Personal Loan\n2. SME Loan",
        "options": {
            "Personal Loans": "Personal Loans",
            "SME Loan Type": "SME Loan",
            "Check Eligibility": "Verify Eligibility",
            "Required Documentations": "Required Documentation",
            "Loan Information":"Back"
        }
    },

}

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    response = chat_data.get(user_input, chat_data['greeting'])
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
