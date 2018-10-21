# DockMaster
A **Python** threading package which allows users to asynchronously execute functions and pass them to a customised storage location.

# Installing
Copy the contents of the repo into your desired directory. You only need to access

  `DockMaster.py`
  
to utilise the package.

# Running DockMaster
Before you can send functions to the DockMaster it must first be intialised.

  `import DockMaster
  
  dockmaster = DockMaster.DockMaster() #Using the default values in this example.
  
  dockmaster.start_shift() #This starts the DockMaster on its own thread ready to check for new methods. Can be ended with  dockmaster.end_shift()`
