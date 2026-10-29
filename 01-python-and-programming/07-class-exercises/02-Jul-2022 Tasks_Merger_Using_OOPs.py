import logging
logging.basicConfig(filename="test1.log",level=logging.INFO)


class List_Dict_Tuple_Set_Task:

    try:
        def __init__(self,l):
            self.l=l
        
        """Try to extract all the list entity"""
        def extract_list_entity(self):
            for i in self.l:
                if type(i)==list:
                    logging.info(i)
        
        """Try to extract all the dict entities"""
        def extract_dict_entity(self):
            for i in self.l:
                if type(i)==dict:
                    logging.info(i)    
        
        """Try to extract all the tuples entities"""
        def extract_tuple_entity(self):
            for i in self.l:
                if type(i)==tuple:
                    logging.info(i)    
        
        """Try to extract all the numerical data it may be a part of dict key and values"""
        def extract_numerical_data(self):
            for i in self.l:
                if type(i)==tuple or type(i)==list or type(i)==set:
                    for j in i:
                        if type(j)==int:
                            logging.info(j)
                if type(i)==dict:
                    for k,v in i.items():
                        if type(k)==int or type(v)==int:
                            logging.info(k,v)
        
        """Try to give summation of all the numeric data"""
        def sum_numeric(self):
            sum_num=0
            for i in self.l:
                if type(i)==tuple or type(i)==list or type(i)==set:
                    for j in i:
                        if type(j)==int:
                            sum_num=sum_num+j
                if type(i)==dict:
                    for k,v in i.items():
                        if type(k)==int or type(v)==int:
                            sum_num=sum_num+k+v
            logging.info("Summation of all the numeric data : %s",sum_num)
        
        """ Try to filter out all the odd values out all numeric data which is a part of a list"""
        def odd_numeric_value(self):
            odd_number_list=[]
            for i in self.l:
                if type(i)==list:
                    for j in i:
                        if type(j)==int:
                            if j%2 != 0 :
                                odd_number_list.append(j)
            logging.info("Odd numbers presenet in the list are %s",odd_number_list)
        
        """Try to extract "ineuron" out of this data"""
        def extract_ineuron(self):
            text_list=[]
            for i in self.l:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                        if j=="ineuron":
                            text_list.append(j)
                if type(i)==dict:
                    for k,v in i.items():
                        if k=="ineuron":
                            text_list.append(k)
                        if v=="ineuron":
                            text_list.append(v)
                            
            logging.info(text_list)
        
        """Try to find out a number of occurances of all the data"""
        def occurence_number(self):
            occur=[]
            for i in self.l:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                            occur.append(j)
                if type(i)==dict:
                    for k,v in i.items():
                        occur.append(k)
                        occur.append(v)
            for m in occur:
                logging.info("%s:%s",m,occur.count(m))
            
        """Try to find out number of keys in dict element"""
        def number_keys_dict(self):
            count_key=0
            for i in self.l:
                if type(i)==dict:
                    for k in i.keys():
                        count_key=count_key+1 
            logging.info(count_key)
        
        """Try to filter out all the string data"""
        def filter_string(self):
            str_list=[]
            for i in self.l:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                        if type(j)==str:
                            str_list.append(j)
                if type(i)==dict:
                    for k,v in i.items():
                        if type(k)==str:
                            str_list.append(k)
                        if type(v)==str:
                            str_list.append(v)
            logging.info(str_list)

        """Try to find out all the alphanum in date"""
        def filter_alphanum(self):
            alphanum_list=[]
            for i in self.l:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                        if type(j)==str:
                            if j.isalnum()==True:
                                alphanum_list.append(j)
                if type(i)==dict:
                    for k,v in i.items():
                        if type(k)==str:
                            if k.isalnum()==True:
                                alphanum_list.append(k)
                        if type(v)==str:
                            if v.isalnum()==True:
                                alphanum_list.append(v)
            logging.info(alphanum_list)

        """Try to find out multiplication of all numeric value in the individual collection inside dataset"""
        def multiply_numeric(self):
            mul_num_tuple=1
            mul_num_set=1
            mul_num_list=1
            mul_num_dict=1
            j=0
            for i in self.l:
                if type(i)==tuple:
                    for j in i:
                        if type(j)==int:
                            mul_num_tuple=mul_num_tuple*j
                if type(j)==list:
                    for j in i:
                        if type(j)==int:
                            mul_num_list=mul_num_list*j
                if type(j)==set:
                    for j in i:
                        if type(j)==int:
                            mul_num_set=mul_num_set*j
                if type(i)==dict:
                    for k,v in i.items():
                        if type(k)==int or type(v)==int:
                            mul_num_dict=mul_num_dict*k*v
                            
            logging.info("Multiplication of all the numeric data inside the tuple: %s",mul_num_tuple)
            logging.info("Multiplication of all the numeric data inside the list: %s",mul_num_list)
            logging.info("Multiplication of all the numeric data inside the set: %s",mul_num_set)
            logging.info("Multiplication of all the numeric data inside the dict: %s",mul_num_dict)
        
        """Try to unwrape all the collections inside collection and create a flat list"""
        def unwrap_in_flat_list(self):
            flat_list=[]
            for i in self.l:
                if type(i)==tuple or type(i)==list or type(i)==set:
                    for j in i:
                        flat_list.append(j)
            
                if type(i)==dict:
                    for k,v in i.items():
                        flat_list.append(k)
                        flat_list.append(v)

            logging.info("Unwrape elements: %s",flat_list)
    except:
        logging.exception("Error occured")
    else:
        logging.info("Code ran successfully.")


l=[[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{'k1':"sudh","k2":"ineuron","k3":"kumar",
3:6,7:8},["ineuron","data science"]]
obj_list_task=List_Dict_Tuple_Set_Task(l)
obj_list_task.extract_list_entity()
obj_list_task.extract_dict_entity()
obj_list_task.extract_tuple_entity()
obj_list_task.extract_numerical_data()
obj_list_task.sum_numeric()
obj_list_task.odd_numeric_value()
obj_list_task.extract_ineuron()
obj_list_task.occurence_number()
obj_list_task.number_keys_dict()
obj_list_task.filter_string()
obj_list_task.filter_alphanum()
obj_list_task.multiply_numeric()
obj_list_task.unwrap_in_flat_list()

class Str_Task:
    
    def __init__(self,s,s1,s2,s3):
        self.s=s
        self.s1=s1
        self.s2=s2
        self.s3=s3

    try:
        """Try to extract data from index one to index 300 with a jump of 3."""
        def extract_data(self):
            logging.info(self.s[1:300:3])
        
        """Try to reverse a string without using reverse function"""
        def reverse_string(self):
            logging.info(self.s[::-1])
        
        """Try to split a string after conversion of entire string in uppercase"""
        def split_string(self):
            logging.info(self.s.upper().split(' '))
        
        """Try to convert the whole string into lower case"""
        def to_lower_string(self):
            logging.info(self.s.lower())
        
        """Try to capitalize the whole string"""
        def capitalize_string(self):
            logging.info(self.s.capitalize())
        
        """Try to give an example of expand tab"""
        def expand_tab_string(self):
            logging.info(self.s1.expandtabs())
        
        """Give an example of strip , lstrip and rstrip"""
        def strip_lstrip_rstrip_string(self):
            logging.info(self.s2.strip())
            logging.info(self.s2.lstrip())
            logging.info(self.s2.rstrip())

        """Replace a string character by another character by taking your own example """
        def replace_string(self):
            logging.info(self.s3.replace('u','W'))

        """Try to give a definition of string center function with an example"""
        def center_string(self):
            logging.info(self.s3.center(30,'#'))
        
    except:
        logging.exception("Some error occured.")

s = "this is My First Python programming class and i am learNING python string and its function"
s1="Subhash\tDixit\tNIT\tDUrgapur"
s2=" Subhash Dixit  "
s3="Subhash Dixit"
obj_extract_data=Str_Task(s,s1,s2,s3)
obj_extract_data.extract_data()
obj_extract_data.reverse_string()
obj_extract_data.split_string()
obj_extract_data.to_lower_string()
obj_extract_data.capitalize_string()
obj_extract_data.expand_tab_string()
obj_extract_data.strip_lstrip_rstrip_string()
obj_extract_data.replace_string()
obj_extract_data.center_string()
