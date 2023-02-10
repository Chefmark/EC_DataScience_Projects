# CHECK-OUT CART (shop)

## OBS! brainstorm document.  

## Description

An app that works as a "check-out" for a shop. the database will contain: 
- orders: 
    - id (PRIMARY KEY)
    - date (YYYY-MM-DD)
    - products in cart
    - employee(code) making sale
    - a subtotal
    - tax total
    - total
    - member_customer (id) 
        - option (add guest for non-members) 
<br> </br>
- products: 
    - id
    - name
    - description
    - stock 
    - price
    - tax
<br> </br>
- employees: 
    - id 
    - employe_code
    - name
    - role_id:
        - owner 
        - shiftleader 
        - employee
    - Start date
    - Active (Yes/No)
    
<br> </br>
- member_customer:
    - social_security_nr (Person_nr) (Primary Key)
    - name
    - phone number
    - email


App ska börja med att ta en inlogg kod. kod ska ge 3 olika menyer (3 classes) 

### Class 1 - Employee
Kan göra följande val:

1. Lägga en ny order
1. Lägga till en ny medlem
1. Logga ut

### Class 2 - Shiftleader
Kan göra följande val:

1. Lägga en ny order
1. Lägga till en ny medlem
1. Lägga till nya anställda (av klass employee)
1. Lager
    1. Updatera lager (fylla på)
    1. Lägga till nya produkter
    1. skriva ut lager
1. logga ut

### Class 3 - Owner

1. Lägga en ny order 
1. Lägga till en ny medlem 
1. Lägga till nya anställda (av klass employee och shiftleader) 
1. Inventory
    1. Updatera lager (fylla på stock, ändra pris)
    1. Lägga till nya produkter
    1. Ta bort produkt
1. Skriva ut statistik 
1. Logga ut


### LAYOUT

1) Inmatning av Användar ID eller stänga av programmet med ("exit")

2) Meny Display
    1. Orders (C1,C2,C3)
    2. Members (C1, C2, C3)
    3. Employees (C2,C3)
    4. Inventory (C2,C3)
    5. Statistics (C3)
    6. Log Out (C1,C2,C3)

3) Meny Val

4) Visa ny meny (Ge error om ID inte är behörig, "Error you do not have permission for this option) 

- Orders
    1. place new order
        - for member_id search Personnr. 
        - if not found (ask to add member) if yes create new member. if no leave blank and add guest.
        - leave blank to add guest.
    1. return to main menu

- Members
    1. Add new member
    2. Search members
    3. Update members
    4. Delete members
    5. return to main menu

- Employees (C2, C3)
    1. Add new Employee
    2. Search Employees
    3. Update Employees
    4. Delete Empoyees
    5. return to main menu

- Inventory (C2, C3)
    1. Add Product
    2. Update Product
    3. Print Inventory
    4. Remove product (C3)
    5. return to main menu

- Statistics (C3)
    1. Print Order statistics
    2. Return to main
<br></br>

-----




