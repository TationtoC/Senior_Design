import time

#Def create_account:
    #part 1 prompt for name    

    #Prompt user for name
    #call record function from class obj
    #call use_model() and set = to variable Pred_name
    #Clear transcription box
    #INPUT new text into box with OUTPUT from use_model
    #Prompt for correctness 
    #Put time buffer here
    #Call record for verification -  SAVE TO IF_YES
    #If IF_YES = yes
        #continue 
        #Part 2 prompt for email

        #If output = yes
        #clear transcribe label
        #Input text to box and prompt for email
        #Call record


        #part 3 prompt for for password
    #else 
        #print("Please try again")
def format_email(string):
    punc_list = '''!()-[]{};*:'"\,<>./?_~'''
    for i in string:
        if i in punc_list:
            string = string.replace(i,"")
    
    string = string.replace(" ", "")
    print(string)

def exp_contact_list():
    with open("source/contact_list.txt", "w") as f:
        f.write("Tyler Cohen tcohenwest gobblety154\n" + "Devin Chen Dchen1 furryornah\n" + "Zach Ray zray1 beastmode\n")
        f.close()
    with open("source/contact_list.txt", "r") as f:
        contacts = f.readlines()
        for line in contacts:
            print(line)

#exp_contact_list()
#format_email("T. Cohen West")
def pull_contact(string):
    with open("source/my_account.txt", "r") as f:
         contacts = f.readlines()

         for line in contacts:
            extr = line.partition(" ")
            first_name = extr[0]
            extr_2 = extr[2].partition(" ")
            last_name = extr_2[0]
            extr_3 = extr_2[2].partition(" ")
            email = extr_3[0]
            domain = extr_3[2]
            if (first_name + " " + last_name == string):
                contact = {
                    'name' : first_name + " " + last_name,
                    'email' : email , 
                    'domain' : domain
                }
            
            #copy string until second " " is found 
            #compare with user input
            #If same pull the info from the line and save as dict
    return contact.get('name'), contact.get('email'), contact.get('domain')
    
    
    #return output
name, email, domain = pull_contact("Chris Perlowin")
print(name, email, domain)

def account_info_in():
    with open("source/my_account.txt", "r") as f:
         contacts = f.readlines()
         for line in contacts:
            extr = line.partition(" ")
            first_name = extr[0]
            extr_2 = extr[2].partition(" ")
            last_name = extr_2[0]
            extr_3 = extr_2[2].partition(" ")
            email = extr_3[0]
            domain = extr_3[2]
            contact = {
                    'name' : first_name + " " + last_name,
                    'email' : email , 
                    'domain' : domain
                }
    return contact.get('name'), contact.get('email'), contact.get('domain')