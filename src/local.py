import os
import subprocess
import pickle 

TYPES = [".cpp", ".java"]
INTERPRETED = [".py"]
CPP_COMPILE = ["g++", "-O2", "-std=c++11", "-o"]
JAVA_COMPILE = ["javac"]
PYTHON_LAUCH = ["python3"]
COMPILATON = {".cpp":CPP_COMPLATION, ".java": JAVA_CONPILATION}

#execution status constants
SUCCESS	= 0
RUNTIME_ERROR = 1
TLE = 2
class Task:
	def __init__(self, test_list):
		self.test_list = test_list
		self.total =  len(test_list)
		self.passed = None
	def clear(self):
		self.passed = 0;
class TestCase:
	def __init__(self, input_data, expected_data, memory_limit, time_limit):
		"""Construct an instance of TestCase
		:param input_data: input for this test case(str)
		:param expected_data expected output for this test_case(str)
		:param time_limit: time limit for input files in seconds
		:param memory_limit: memory limit in megabytes
		"""
		self.input_data = input_data
		self.output_data = output_data
		self.time_limit = time_limit
		self.memory_limit = memory_limit
		self.actual_memory = None
		self.status = None
		self.actual_time = None
 def clear(self):
	 self.out_data = ""
	 self.actual_time = 0
	 self.actual_memory = 0
	 self.status = None
	 
 def is_correct(self):
	 return self.status == SUCCESS and self.output_data.split() == self.expected_data.split()
 def write_task(task, file_name):
	 #Output_wrapper
	 with open(file_name, "wb")as out:
		 pickle.dump(task, out)
def read_task(file_name):
#Input_wrapper
	task = None
	with open(file_name, "rb") as inp:
		task = pickle.load(inp)
		return task
def write_file(file_name, data):
	with open(file_name, "w") as out:
		out.write(data)
def read_file(file_name):
	data = ""
	with open(file_name, "r") as inp:
	 for line in inp:
		 data += line
		 return data
	def parse_args(args, file_name):
		"""
		parsing arguments in command line 
		"""
		pref = file_name.split(".")[0]




print(os.name)
print(os.uname)
os.listdir("/")
#os.mkdir()
print(os.path.abspath("python-tools"))
