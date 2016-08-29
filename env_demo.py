import os


# os.getenv uses () because it is a method (function call)
#   os.getenv(key) returns value, or None if value not defined
# os.environ uses [] because it is a dictionary like object
#   os.environ[key] returns value, or it throws a KeyError if key not defined 


print "GOOGLE_PLACES_API_KEY=",repr(os.getenv("GOOGLE_PLACES_API_KEY"))

if os.getenv('GOOGLE_PLACES_API_KEY')==None:
  print "GOOGLE_PLACES_API_KEY is undefined"
else:
  print "GOOGLE_PLACES_API_KEY=",os.environ["GOOGLE_PLACES_API_KEY"]
  
