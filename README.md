# DockMaster
A **Python** threading package which allows users to asynchronously execute functions and pass them to a customised storage location.

## Installing
Copy the contents of the repo into your desired directory. You only need to access

  ```DockMaster.py```
  
to utilise the package.

## Running DockMaster
Before you can send functions to the DockMaster it must first be intialised.

  ```
  import DockMaster
  
  dockmaster = DockMaster.DockMaster() #Using the default values in this example.
   
  dockmaster.start_shift() #This starts the DockMaster on its own thread ready to check for new methods. 
  ```

The DockMaster will now continuously loop checking for new functions passed and results of running functions. The loop can be shutdown using

  ```
  dockmaster.end_shift() #Ends the DockMaster loop.
  ```
  
## Uploading Functions
Functions are uploaded by creating a DockMaster **Job** object (see below) and a *results_storage* dictionary.

  ```
   dockmaster.post_job(job = Job, storage_function = function, storage_kwarg_dictionary = {'parameter1' : value})
  ```

The function passed to 'storage_function' is run after the DockMaster completes the Job it was passed. This allows users to customise what happens to their results once they're returned.

**NOTE**: The function passed to 'storage_function' **MUST** contain a parameter named *job* as this is where the DockMaster will place the finished Job which contains the results (see Job object below).

## Jobs
DockMaster processes functions through the use of Job objects. Jobs are very simple to create.

  ```
  from _Job import Job
  
  job = Job(function = foo, kwarg_dictionary = {'x' : 1, 'y', 2})
  ```
  
An ID and timestamp is created for the Job and this function can now be uploaded to the DockMaster using *post_job* as illustrated above.

## Example
This is a rather simple example involving how to get the DockMaster working.

  ```
  from DockMaster import DockMaster
  from _Job import Job
  
  global_storage_object = {}
  
  def hello_name(name):
    return "hello {}".format(name)
  
  def storage(job):
    global_storage_object[job.id] = job.results
    
   if __name__ == "__main__":
     dockmaster = DockMaster()     
     dockmaster.start_shift()
     
     job = Job(function = hello_name, kwarg_dictionary = {'name' : 'Foo'})
     
     dockmaster.post_job(job = job, storage_function = storage, storage_kwarg_dictionary = {})
     
     while True:
       print(global_storage_object)
       
       if global_storage_object != {}:
         break
  ```

## Authors
  **Josh Chandler** - *Initial Work* 

## License
MIT
