
from subprocess import call

print("hello")

#the_call = "ls"
#result = subprocess.Popen(the_call.strip().split(" "), stdout=subprocess.PIPE).communicate()[0]
#result = result.decode("utf-8")
#print(result)

#from subprocess import call
#call(["git", "clone", "https://hartloff@bitbucket.org/need-for-speed/unityrepository.git"])
#call(["git", "-C", "/home/csefaculty/hartloff/CourseWebsite/repos", "clone", "https://hartloff@bitbucket.org/need-for-speed/unityrepository.git"])

from subprocess import call

#call(["git", "clone", "https://hartloff@bitbucket.org/need-for-speed/unityrepository.git"])
result = subprocess.Popen(["git", "clone", "https://hartloff@bitbucket.org/need-for-speed/unityrepository.git"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
print(str(result[0].decode("utf-8")))

#from subprocess import call
#call(["ls", "-l"])

print("goodbye")
