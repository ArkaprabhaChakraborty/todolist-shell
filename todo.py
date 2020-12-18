import sys
import os.path
from datetime import datetime


def help():
	t="""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
	sys.stdout.buffer.write(t.encode('utf8'))		
	

def add(st):
	if os.path.isfile('todo.txt'):					
	    with open("todo.txt",'r') as t:
	    	data=t.read()
	    with open("todo.txt",'w') as d:
	    	d.write(st+'\n'+data)
	else:									
	    with open("todo.txt",'w') as f:
	    	f.write(st+'\n')
	print('Added todo: "{}"'.format(st))


def showlist():
	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as t:
	    	data=t.readlines()
	    c=len(data)
	    st=""
	    for line in data:
	    	st+='[{}] {}'.format(c,line)
	    	c-=1
	    sys.stdout.buffer.write(st.encode('utf8'))
	else:
	    print ("There are no pending todos!") 


def delete(num):
	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as t:
	    	data=t.readlines()
	    c=len(data)
	    if num>c or num<=0:
	    	print(f"Error: todo #{num} does not exist. Nothing deleted.")
	    else:
	    	with open("todo.txt",'w') as tm:
	    		for line in data:
	    			if c!=num:
	    				tm.write(line)
	    			c-=1
	    	print("Deleted todo #{}".format(num))
	else:
	    print("Error: todo #{} does not exist. Nothing deleted.".format(num))


def markdone(num):
	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as t:
	    	data=t.readlines()
	    c=len(data)
	    if num>c or num<=0:
	    	print("Error: todo #{} does not exist.".format(num))
	    else:
	    	with open("todo.txt",'w') as tmod:
	    		if os.path.isfile('done.txt'):
	    			with open("done.txt",'r') as dfile:
				    	done=dfile.read()
			    	with open("done.txt",'w') as dfilemod:
			    		for line in data:
			    			if c==num:
			    				dfilemod.write("x "+datetime.today().strftime('%Y-%m-%d')+" "+line)
			    			else:
			    				tmod.write(line)
			    			c-=1
			    		dfilemod.write(done)
		    	else:
		    		with open("done.txt",'w') as dfile:
			    		for line in data:
			    			if c==num:
			    				dfile.write("x "+datetime.today().strftime('%Y-%m-%d')+" "+line)
			    			else:
			    				tmod.write(line)
			    			c-=1
	    	print("Marked todo #{} as done.".format(num))
	else:
	    print("Error: todo #{} does not exist.".format(num))


def report():
	t_count = 0
	d_count = 0
	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as t:
	    	todos=t.readlines()
	    t_count=len(todos)
	if os.path.isfile('done.txt'):
	    with open("done.txt",'r') as d:
	    	done=d.readlines()
	    d_count=len(done)
	st=datetime.today().strftime('%Y-%m-%d') + " Pending : {} Completed : {}".format(t_count,d_count)
	sys.stdout.buffer.write(st.encode('utf8'))


def main(): 
	if len(sys.argv)==1:
		help()
	elif sys.argv[1]=='help':
		help()
	elif sys.argv[1]=='ls':
		showlist()
	elif sys.argv[1]=='add':
		if len(sys.argv)>2:
			add(sys.argv[2])
		else:
			print("Error: Missing todo string. Nothing added!")
	elif sys.argv[1]=='del':
		if len(sys.argv)>2:
			delete(int(sys.argv[2]))
		else:
			print("Error: Missing NUMBER for deleting todo.")
	elif sys.argv[1]=='done':
		if len(sys.argv)>2:
			markdone(int(sys.argv[2]))
		else:
			print("Error: Missing NUMBER for marking todo as done.")
	elif sys.argv[1]=='report':
		report()
	else:
		print('Option Not Available. Please use "./todo help" for Usage Information')

if __name__=="__main__": 
    main() 