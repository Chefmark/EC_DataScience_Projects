# Things that should be added to the store program

## Permissions
The different employee types should have different permissions. The main menu in store.py has been marked with Everyone, C2 or C3 referencing C2 - shiftleaders and C3 - owner indicating who should be allowed to do what.

## Carry the logged in user value through the program
in order to A) check for permission. B) during checkout, automatically attach the employee id.

## Error handeling
Better Error handeling so that the program does not shut down during wrong input.

## Better Statistics 
Right now there are only simple descriptors (Totals and count)
To be added:
    - Total Sales by employee

## Clean the model portion of the program
currently there are multiple model files which could be combined into one to reduce the number of files in the program. 