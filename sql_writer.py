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
list_tables = ['Android_Challenges.table','Assembly_Challenge.table'] #add here all file names with strings...
