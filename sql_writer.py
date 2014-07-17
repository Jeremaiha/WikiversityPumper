#functions which will write the queries

def text_writer(file_name ,txt):
	file_obj = open(file_name, 'w')
	file_obj.write(txt)
	file_obj.close()
# End of text_writer

def inject_c_challenges():
  print "Starting c challenge query"
  
  insert_query = ""
  
  
  
#end of inject c challenges

def inject_cpp_challenges():
  print "Starting c++ challenge query"  
  
#end of inject c++ challenges


#main 
list_tables = ['Android_Challenges.table','Assembly_Challenges.table','Blender_3D_Challenges.table','C_Challenges.table','CPP_Challenges.table','Encryption_Challenges.table','HTML_Challenges.table','Linux_Challenges.table','Math_Challenges.table','PHP_Challenges.table','Python_Challenges.table','Resources_Challenges.table','Reversing_Challenges.table','Security_Challenges.table','Thinking_Challenges.table'] #add here all file names with strings...
