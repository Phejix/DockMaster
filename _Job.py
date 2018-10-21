import uuid
import datetime

class Job(object):
    
    def __init__(self, function, kwarg_dictionary, origin = None, results = None):
        self.id = uuid.uuid4().hex
        self.function = function
        self.kwarg_dictionary = kwarg_dictionary
        self.results = results
        self.origin = origin
        self.creation_date = datetime.datetime.now().timestamp()

    def process_job(self):
        return self.function(**self.kwarg_dictionary)

    def get_job_dictionary(self, serializable = False):
        job_dictionary = {
            "id" : self.id,
            "origin" : self.origin,
            "kwarg_dictionary" : self.kwarg_dictionary,
            "results" : self.results,
            "creation_date" : self.creation_date
            "function" : self.function
        }

        if serializable:
            job_dictionary["function"] = self.function.__name__
        
        return job_dictionary