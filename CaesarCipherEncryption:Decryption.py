print(f"Welcome to the Encryption/Decryption App.")




alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
activeProgram1=True
activeProgram2=True

while(activeProgram1==True):
    
    while(activeProgram2==True):
        
        user_choice=input(f"Press E to encrypt, D to decrypt your message: ")
        message=input(f"Please input your message: ")
        shift_value=input(f"Please input your shift value: ")
        message_splitted=[]
        message_position_list=[]
        shifted_position_list=[]
        shifted_message_list=[]
        shifted_position=""
        encrypted_message=""
        decrypted_message=""

        if(user_choice=="E" or user_choice=="e"):
            for single_message in message:
                message_splitted.append(single_message)
            
            
            for position in message_splitted:
                message_position=alphabet.index(position)
                message_position_list.append(message_position)
            
            
            for notShifted_position in message_position_list:
                shift_value_modulus=int(shift_value)%53
                y=52-int(notShifted_position)

                #variable "y" represents the number of alphabets left from its current position to the last character on the list.
                
                if((int(shift_value)>=52) and (int(shift_value_modulus)<=int(y))):
                    notShifted_position=int(notShifted_position)+int(shift_value_modulus)
                elif((int(shift_value)>=52) and (int(shift_value_modulus)>int(y))):
                    notShifted_position=int(notShifted_position)+int(shift_value_modulus)-53
                elif(int(shift_value)<52 and int(shift_value)>int(y)):
                    notShifted_position=int(shift_value)-53+int(notShifted_position)
                elif(int(shift_value)<52 and int(shift_value)<=int(y)):
                    notShifted_position=int(notShifted_position)+int(shift_value)
                

                    
                
                shifted_position_list.append(notShifted_position)
            
            
            for notShifted_message in shifted_position_list:
                shifted_message=alphabet[notShifted_message]
                encrypted_message=encrypted_message+shifted_message

            print(encrypted_message)


        if(user_choice=="d" or user_choice=="D"):
            for single_message in message:
                message_splitted.append(single_message)
            
            
            for position in message_splitted:
                
                message_position=alphabet.index(position)
                message_position_list.append(message_position)
            
            
            for notShifted_position in message_position_list:
                shift_value_modulus=int(shift_value)%53
                y=int(notShifted_position) 
                
                if((int(shift_value)>=52)) and (int(shift_value_modulus)<=int(y)):
                    notShifted_position=int(notShifted_position)-int(shift_value_modulus)
                elif((int(shift_value)>=52)) and (int(shift_value_modulus)>int(y)):
                    notShifted_position=int(notShifted_position)-int(shift_value_modulus)+53
                elif(int(shift_value)<52 and int(shift_value)>int(y)):
                    notShifted_position=int(notShifted_position)-int(shift_value)+53
                elif(int(shift_value)<52 and int(shift_value)<=int(y)):
                    notShifted_position=int(notShifted_position)-int(shift_value)
                

                    
                
                shifted_position_list.append(notShifted_position)
            
            
            for notShifted_message in shifted_position_list:
                shifted_message=alphabet[notShifted_message]
                decrypted_message=decrypted_message+shifted_message

            print(decrypted_message)
        
        activeProgram2=False


    conti=input(f"Do you want to continue? Y/N: ")
    if(conti=="Y" or conti=="y"):
        activeProgram2=True

        print("Restarting the program...")
    elif(conti=="N" or conti=="n"):
        activeProgram1=False
        print(f"Exiting the program...")
    else:
        print("Invalid_Input. Please try again.")

