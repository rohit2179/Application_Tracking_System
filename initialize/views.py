from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import re, time
import openai
from django.views import View
from PyPDF2 import PdfReader
from initialize.models import Discription
from django.templatetags.static import static
import yagmail

class PDFView(View):
    def get(self, request, *args, **kwargs):
        pdf_path = static('Resume--RohiniPrakash.pdf')  # Path to the static PDF file
        with open(pdf_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="example.pdf"'
            return response


message = "############"
message1 = "$$$$$$$$$$$"
counter = 0
disc_message = ""
d = "Description should be shown here..."
#================================================================-- pages --==================================================================

def index(request):
    print(HttpResponse("an i here"))
    return render(request, 'resume.html')

def screening(request):
    

    #=================================================================================================================

   

    

    

    return render(request, 'Screening.html')
#==================================================================================================================================================
candy_request=0 
def candidate(request):
    global candy_request, message, message1, counter          
    candy_request=request   

    
    context = {'disc_message': disc_message,'message': message, "message1": message1}
    print("============================\n",message, message1, "\n====================================================")
    # message = ""
    
    return render(request, 'candidate.html', context) 

#==================================================================================================================================================
#===============================================================--- working ---====================================================================

def upload_pdf(request):
    print("-----------------------------------------------------zsdnSfgnzfdhnsdfg ndgh---------------------------------------------")
    if request.method == 'POST' and request.FILES['pdf_file']: 
        uploaded_file = request.FILES['pdf_file']
        print("====================================\n",uploaded_file ,"\n=================================================")
        # Do something with the uploaded file, such as saving it to the server or processing it
        reader = PdfReader(uploaded_file)
        page = reader.pages[0]

        # # extracting text from page
        text = page.extract_text()

        openai.api_key = "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"

        prompt = f"you are a HR check if this resume {text} contains personnal details like name,contact,email then say 1 and if it dosent contain contains personnal details like name,contact,email then say 0 "
        model = "text-davinci-003"
        response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=100)
        generated_text1 = response.choices[0].text

        
        print("result is----  ",generated_text1,"  ------------")
         

        # time.sleep(3)
        candidate(candy_request)
        # message1 = ""

        prompt = f"you are a HR and you have to rate the candidate acording to this job discription{d} and his resume {text}only give me the rating out of 100 in integer format without \\n and spaces"
        model = "text-davinci-003"
        response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1000)
       
        generated_text = response.choices[0].text
        print("-rank------------",generated_text,"----------------")
    
        
        #initializing the server connection
        #============================================= email sending ==========================================================================

        yag = yagmail.SMTP(user='lms.aj.industries@gmail.com', password='wmwydlvblprhjtqj')
        #sending the email

        #company Details
        hiringPost      = "Software Developer"
        emailHR         = "hr14@ajindustries.com"
        contactHR       = "+91 0000000000"
        companyName     = "Aj Industries"
        companyContact  = "+91 1234567890"

        # Subject: Enhancing Your Resume for a Successful Application

        suggestion="""<div class="email" style="font-size: 14px;">Dear <b>Candidate</b>, 

        I hope this email finds you well. I wanted to take a moment to provide you with some insights that might help you enhance your resume for a more impactful job application. As we receive numerous applications for our roles, having a well-structured and readable resume can significantly improve your chances of standing out in the selection process.

        1. **Clear Formatting and Structure:**
        A well-organized resume is crucial for easy readability. Make sure to use consistent fonts, bullet points, and headings to create a visually appealing layout. This helps our hiring team quickly navigate through your achievements and experiences.

        2. **Tailoring to the Role:**
        Customize your resume for the specific role you're applying for. Highlight the skills, experiences, and achievements that align most closely with the job description. This helps us understand how your background fits the position's requirements.

        3. **Quantifiable Achievements:**
        Whenever possible, quantify your achievements. Use metrics, numbers, and percentages to demonstrate the impact you've had in previous roles. This provides a clearer picture of your contributions and capabilities.

        4. **Use of Action Verbs:**
        Start your bullet points with strong action verbs to describe your responsibilities and accomplishments. This makes your resume more dynamic and engaging to read.

        5. **Relevance of Information:**
        While including relevant experiences is essential, be mindful of the relevance of older experiences, especially if they aren't directly related to the position you're applying for. Focus on recent and applicable roles to keep your resume concise.

        6. **Avoid Overcrowding:**
        Ensure that your resume isn't overly crowded with information. A clutter-free layout makes it easier for us to absorb the key details about your qualifications.

        7. **Contact Information:**
        Double-check that your contact information, including email address and phone number, is accurate and up-to-date. This ensures that we can easily reach you with updates about your application.

        8. **Proofreading and Grammar:**
        A resume with grammatical errors and typos can leave a negative impression. Review your resume thoroughly and, if possible, have someone else proofread it as well.

        Please know that we highly value your interest in joining our team and we are committed to giving every application the careful consideration it deserves. We believe that by making these improvements, your resume will become an even more compelling representation of your qualifications.

        Thank you for your time and effort in applying to [Company Name]. We look forward to receiving your updated resume and continuing the application process. If you have any questions or need further assistance, please don't hesitate to reach out.

        Best regards,

        [Your Name]
        [Your Title]
        [Company Name]
        [Contact Information]

        <a href="http://www.google.com">Click here to get redirect to website.</a>
        </div>
        </div>
        """


        screeningQuestionInvitation = """<div class="email" style="font-size: 14px;">Dear [<b>Candidate's Name</b>],

        I trust this email finds you well. Thank you for expressing your interest in the [Position Title] at [Company Name]. We have thoroughly reviewed your application and are pleased to inform you that you have been selected to move forward to the next stage of our recruitment process.

        The next step is a Screening Question Round designed to help us better understand your qualifications, experiences, and suitability for the role. This round consists of a set of targeted questions that will assess your skills and alignment with our requirements.

        Please find below the details of the Screening Question Round:

        - Method: Online questionnaire
        - Expected Duration: Approximately [duration] minutes
        - Access: You will receive a separate email with a link to the questionnaire within the next [timeframe].
        - Deadline: Kindly complete the questionnaire by [deadline date].

        We understand the importance of your time, and we assure you that this round has been structured to be concise while still providing valuable insights into your qualifications.

        Your responses will be evaluated by our hiring team, and based on the outcomes, selected candidates will be invited for further rounds of interviews.

        Should you have any questions regarding the screening process or require any assistance, please do not hesitate to reach out to us at [HR Contact Email] or [HR Contact Phone Number].

        We appreciate your commitment to the application process and look forward to your timely participation in the Screening Question Round. We are excited about the opportunity to learn more about your background and potential fit for our team.

        Thank you for considering a career with [Company Name]. We wish you the best of luck in the upcoming round.

        Best regards,

        [Your Name]
        [Your Title]
        [Company Name]
        [Contact Information]


        <a href="http://www.google.com">Click here to get redirect to website.</a>
        </div>
        """

        finalInterviewEmail = """<div class="email" style="font-size: 16px;">Dear [<b>Candidate's Name</b>],

        I hope this email finds you well. We are pleased to inform you that after careful review of your application, we are impressed with your qualifications and experience that align perfectly with the requirements of the [Position Title] at [Company Name].

        We would like to invite you to the next stage of our selection process – a formal interview. This interview will provide us with an opportunity to learn more about your skills, experience, and how you can contribute to our team. It will also be a chance for you to gain a deeper understanding of our company culture, values, and the role you are being considered for.

        Here are the interview details:

        - Date: [Date]<br>
        - Time: [Time]<br>
        - Location: [Address or Virtual Meeting Link]<br>
        - Interviewers: [Names and Titles]<br>

        Please confirm your availability for the provided date and time. If you are unable to attend or need to reschedule, please let us know as soon as possible so that we can accommodate your request.

        In preparation for the interview, please bring any relevant documents or portfolio materials that you would like to share. Be prepared to discuss your experiences and how they relate to the position. We will also take this opportunity to answer any questions you may have about the role, our company, or the interview process.

        Please reply to this email or contact [HR Contact Name] at [HR Contact Email] or [HR Contact Phone Number] to confirm your attendance or request any further information you may require.

        We appreciate your interest in joining [Company Name] and look forward to meeting you in person. We are excited to explore your potential contributions to our team.

        Thank you once again for your interest and effort. We eagerly await your response.

        Best regards,

        [Your Name]
        [Your Title]
        [Company Name]
        [Contact Information]


        <a href="http://www.google.com">Click here to get redirect to website.</a>
        </div>
        """
        if (int(generated_text1[-1:])==0):
            yag.send(to='123rajaj@gmail.com', subject='Invitation for Interview – {Position Title} at {Company Name}', contents=suggestion)
        if (int(generated_text1[-1:])==1 and int(generated_text[-2:])<=70):
            yag.send(to='123rajaj@gmail.com', subject='Invitation for Interview – {Position Title} at {Company Name}', contents=screeningQuestionInvitation)
        print("process done")  
        #=========================================================================================================================================
        response_data = {'message': 'PDF file uploaded successfully.'} 
    else:
        response_data = {'message': 'Failed to upload PDF file.'}
   
    context = {'message': message, "message1": message1}
    print("============================\n",message, message1, "\n====================================================")
    # message = ""
    
    return render(request, 'candidate.html', context)
    #return JsonResponse(response_data)

#==================================================================================================================================================
#==================================================== hr discription========================================================================================= 

def hr(request):
    if request.method == "POST":
        desc = request.POST.get("discription")
        global disc_message , d
        disc_message = desc
        d = Discription(disc=desc) 
        d.save()
        print("-------------------whart sfff dsfwf-----------")
    return render(request, 'hr.html')

#=================================================================================================================================================
# Create your views here.
