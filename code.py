from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#import os
try:
    os.remove("db.sqlite3")
    print("Old database removed. Training new database")
except:
    print('No database found. Creating new database.')
    english_bot = ChatBot('Bot')
    trainer=ListTrainer(english_bot)
    trainer.train(conv)
    trainer.train(conv1)
    trainer.train(conv2)
    trainer.train(conv3)

    from chatterbot import ChatBot
    from tkinter import *
    i=0
    def ptr():
        global i
        f=e.get()
        w=Label(r,text="You: "+e.get(),bg='lightgreen').grid(row=i,column=2)
        i+=1
        t=english_bot.get_response(f)
        ans=str(t)
        w=Label(r,text="Bot: "+ans,bg='white').grid(row=i,column=0)
        e.delete(0,END)
        i+=1
        r=Tk()
        r.title('chatbot')
        r.geometry("480x550")
        e=Entry(r)
        e.grid(row=20,column=1)
        b=Button(r,text="Send",width=10,command=ptr)
        b.grid(row=20,column=2)
        i=i+1
        mainloop()
        conv=["hi","Hello,Welcome to CollegeDekho","How are you","I’m fine,what about you sir?","I am Alright”,”How can I help you sir?"]
        conv1=["I am in search of colleges or University for admission purpose","Ok sir, Kindly tell me your preference and for which degree?","My preference is basically government colleges and for B.Tech","Ok sir, We have following government colleges for B.Tech and B.E. - 1. IIT Madras, Chennai 2. IIT Delhi, New Delhi 3. IIT Bombay, Mumbai 4. IIT Kharagpur 5. IIT Kanpur 6. IIT Roorkee 7. IIT Guwahati 8. IIT Hyderabad 9. Anna University, Chennai 10. NIT Tiruchirappalli 11. IIT BHU Varanasi 12. ICT Mumbai 13. IIT Indore 14. Jadavpur University, Kolkata 15. IIT ISM Dhanbad 16. NIT Rourkela 17. IIT Bhubaneswar 18. IIEST Shibpur 19. IIT Mandi 20. NIT Karnataka, Surathkal 21. IIT Patna 22. IIT Gandhinagar 23. NIT Warangal 24. Jamia Millia Islamia, New Delhi 25. NIT Calicut 26. IIT Ropar 27. IIST Thiruvananthapuram  28. VNIT Nagpur 29. Delhi Technological University, New Delhi 30. Aligarh Muslim University, Aligarh 31. NIT Kurukshetra 32. MNNIT Allahabad 33. Jawaharlal Nehru Technological University, Hyderabad 34. NIT Durgapur 35. College of Engineering, Pune 36. IIT Jodhpur","Ok tell me about IITs","Ok sir, IITs generally give admission to JeeMains Cleared students "]
        conv2=["Tell me about medical colleges in india","Ok sir, I am listing you medical colleges name -1) AIIMS New Delhi 2) CMC Vellore 3) Maulana Azad Medical College New Delhi 4) Armed Forces Medical College Pune 5) Grant Medical College Mumbai 6) JIPMER Pondichérry 7) St.John's Medical College Bangalore 8) Kasturba Medical College Manipal 9) University College of Medical Science & G.T.B. Hospital New Delhi 10) Institute of Medical Sciences, BHU Varanasi 11) King George's Medical University, Chowk, Lucknow U.P 12) CMC Ludhiana 13) Sri Ramachandra University Chennai 14) Madras Medical College Chennai 15) Seth G.S. Medical College Mumbai 16) Osmania Medical College Hyderabad 17) BJ Medical College Ahmedabad 18) BJ Medical College - Pune 19) Bangalore Medical College and Research Institute 20) Kolkata Medical College 21) Jawaharlal Nehru Medical College, Aligarh 22) Stanley Medical College23) Kasturba Medical College Mangalore24) Baroda Medical College25) MS Ramaiah Medical College bangalore26) Government Medical College Surat27) Amrita Institute of Medical Sciences and Research Centre Kochi28) College of Medicine SRM University Chennai29) Mahatma Gandhi Memorial Medical College Indore31) Sawai Man Singh Medical (SMS) College Jaipur32) Gandhi Medical College & Hospital Hyderabad33) Lokmanya Tilak Municipal Medical College Sion Mumbai34) Patna Medical College35) Government Medical College and Hospital Chandigarh36) Vardhman Mahavir Medical College New Delhi37) Sardar Patel Medical College, Bikaner36) Army College of Medical Sciences Delhi Cantt38) Govt Medical College Nagpur39) R. G. Kar Medical College and Hospital Kolkata40) Topiwala National Medical College and Nair Hospital Mumbai41) Calcutta National Medical College Kolkata42) Andhra Medical College Visakhapatnam43) Era's Lucknow Medical College and Hospital44) S.C.B. Medical College Cuttack45) Padmashree Dr. D.Y.Patil Medical College Navi Mumbai46) JSS Medical College, Mysore47) Mysore Medical College 48) DR.B.R. Ambedkar Medical College Bangalore 49) D Y Patil Medical College Kolhapur 50) A.J. Institute of Medical Sciences and Research Centre Mangalore1.", "What is the process of getting admission in medical colleges","You need to qualify neet examination for getting admission","Thank you","You’re Welcome sir."]
        conv3=["Can you tell me what is cut off of JeeMains?","Sir, it varies yearly, this year the jee cutoff is for General category was 81, 49 for OBC-NCL, 32 for SC, 27 for ST, and 1 for PWD ","What about neet to qualify"," NEET cutoff 2020 for General category candidates is 50th, while qualifying percentile for SC/ST/OBC aspirants will be 40th.","My Jee cutoff is 85 which are the colleges I can get?","You will get NITs and some state government colleges.","Suggest any private college","Sure sir, I have a very good college in my sight which is a private college but placement is fantastic.Lovely Professional University is India’s best private Engineering college.","Tell me about LPU","LPU is India’s best private engineering college with more than 90% placement record","how to take admission in LPU?","LPU takes admission on the basis of LPU NEST examination. Before Admission you have to appear in LPU NEST exam. Once you clear the Exam you are elligible for taking admission.You can visit to www.lpu.co.in","Thanks for your suggestion","You welcome Sir"]
