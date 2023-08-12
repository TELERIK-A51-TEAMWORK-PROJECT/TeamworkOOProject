<img align="left" src="https://cdn.discordapp.com/attachments/1134577424538017793/1137411856751939594/image.png" alt="logo" width="180px"/>

# MBI EXPRESS SYSTEM GUIDE

Hello and welcome to every new employee in our company. Here you will find everything about our application. 
We specially created this `employee handbook` to help you understand how to work with our **commands** in the most easiest way. 

* **BE AWARE - FOLLOW THE COMMANDS ORDER**

* **BY DOING EVERYTHING IN ORDER/CORRECTLY YOU WILL BE ABLE TO SERVICE A SHIPMENT**

<br></br>
<br></br>


## EVERY COMMAND IN OUR SYSTEM:

<!-- TRUCKS -->

### 🚚 CreateTruck Commands:
> This command set's a truck by giving it a capacity and also maximum range.


**[CreateTruck Information](#1-create-specific-truck-🚚)**

*(You can click here to see how the command works)*
<!-- ROUTE -->

### 🛣 Route Command:

> This command maps a new route and appoints the trucks on it from the first command.

**[CreateRoute Information](#2-create-route-🛣)**

*(You can click here to see how the command works)*

<!-- CUSTOMER -->

### 👷‍♂ Customer Command:

>This command is used when a new customer comes in one of our offices (our employees gather his information and they enter it into the system)

**[CreateCustomer Information](#3-create-customer-👷‍♂)**

*(You can click here to see how the command works)*

<!-- PACKAGE -->

### 📦 Package Command:

>This command is used right after the customer command, it registers a new package in our system from the customers email.

**[CreatePackage Information](#4-create-package-📦)**

*(You can click here to see how the command works)*


<!-- ASSIGN PACKAGE -->

### 🚚📦 AssignPackage Command:

>This command is used to assign a package to an existing truck.

**[AssignPackage Information](#5-assign-package-🚚📦)**

*(You can click here to see how the command works)*

<!-- EMPLOYEE LOGIN -->

### 🔑 Employee Access Command:

>This command gives a restricted information to our employees about the current: packages, routes, trucks.

**[EmployeeLogin Information](#6-employee-login-🔑)**

*(You can click here to see how the command works)*

<!-- MANAGER LOGIN -->

### 🗝 Manager Access Command:

>This command gives a restricted information to our managers about the current customers information (Used only in case of errors and other problems).

**[ManagerLogin Information](#7-manager-login-🗝)**

*(You can click here to see how the command works)*
 

<img align="left" src="https://cdn.discordapp.com/attachments/1134577424538017793/1137411856751939594/image.png" alt="logo" width="180px"/>


# COMMANDS FUNCTIONALITY WITH GUIDE AND EXAMPLES:

**DESCRIPTION OF ALL COMMANDS AND HOW ARE THEY USED**
<br></br>
<br></br>
<br></br>

## 1. CREATE SPECIFIC TRUCK 🚚 
>**Before typing out every parameter you have to create the command - createtruck**

>1. (TRUCK ID) - You will have to set a new truck from our avaible ID's.
<br></br>
>2. (CAPACITY) - You will have to give it capacity (BE AWARE: the different trucks in our firm have different capacities).
<br></br>
>3. (MAX_RANGE) - You will have to set a maximum range (BE AWARE: for the safety of our trucks and our drivers we have limited the range to each truck).

| Truck | ID |Capacity | Max Range |
| :---  | :---:  |   :---:  |      :---: |
| Scania | 1003-1010  | 42,000kg | 8,000km     |
| Man | 1011-1025  | 37,000kg | 10,000km     |
| Actros | 1026-1040  | 26,000kg | 13,000km     |

#### COMMANDS:

`SCANIA - createtruck (ID: 1003 - 1010) (CAPACITY) (MAX_RANGE)`

`MAN - createtruck (ID: 1011 - 1025) (CAPACITY) (MAX_RANGE)`

`ACTROS - createtruck (ID: 1026 - 1040) (CAPACITY) (MAX_RANGE)`

### ALL TRUCK CASES (INCLUDING THE WRONG ONES):
#### INPUT:


```none
VALID INPUT:

createtruck 1003 42000 8000
createtruck 1011 37000 10000
createtruck 1026 26000 13000

INVALID INPUT:

createtruck 1003 42000 8000
createtruck 1003 42000 8000
createtruck 1011 37000 10000
createtruck 1011 37000 10000
createtruck 1026 26000 13000
createtruck 1026 26000 13000
createtruck 1050 42000 8000
createtruck 1004 42000 9000
```
#### EXPECTED OUTPUT:

```none
Truck Scania with id: [1003] already exists!
Invalid range for truck with model Scania
Truck Man with id: [1011] already exists!
Truck Actros with id: [1026] already exists!
The id you are trying to input is invalid(too low or too high)
------------------------------------------
Truck Scania with id: [1003] was created!
------------------------------------------
Truck Man with id: [1011] was created!
------------------------------------------
Truck Actros with id: [1026] was created!
------------------------------------------
```

## 2. CREATE ROUTE 🛣
### [Click to return to the top](#every-command-in-our-system)
>**Before typing out every parameter you have to create the command - createroute**

>1. (ROUTE ID) - You will have to set a new route by giving it a special ID.
<br></br>
>2. (TRUCK ID) - You will have to give the same ID of the truck you set in the first command.
<br></br>
>3. (MAPPING ROUTE) - You will have to set a route using (->) after every city.
<br></br>
>4. (DATE) - You will have to set the current date
#### COMMAND:

`createroute (ROUTE ID) (TRUCK ID) (MAPPING ROUTE) (DATE)`

### ALL ROUTE CASES (INCLUDING THE WRONG ONES):
#### INPUT:

```none
VALID INPUT:

createtruck 1003 42000 8000
createroute 1 1003 Sydney->Melbourne->AliceSprings 2023/8/7

INVALID INPUT:

createroute 1 1003 Sydney->Melbourne->AliceSprings 2023/8/7
createtruck 1003 42000 8000
createtruck 1004 42000 8000 
createroute 5 1003 Sydney->Melbourne->AliceSprings 2023/8/7
createroute 5 1004 Sydney->Melbourne->AliceSprings 2023/8/7
createroute 2 1003 Sydney->Melbourne->AliceSprings 2023/8/0
createroute 1 1004 Sydney->Melbourne->AliceSprings 2023/8/7
createroute 4 1003 Sydney->Melbourne->AliceSprings 202/8/7
```

#### EXPECTED OUTPUT:

```none
Truck: [1004] Scania does not exist!
day is out of range for month
Route with id: [1] is already taken by [1003]
Invalid year (must be between 2023-2025)
------------------------------------------------------------------------------
Truck Scania with id: [1003] was created!
------------------------------------------------------------------------------
Route with id: [1] has been created:
Route: [Sydney->Melbourne->AliceSprings]
Assigned to truck: [1003] Scania
------------------------------------------------------------------------------
```

## 3. CREATE CUSTOMER 👷‍♂
### [Click to return to the top](#every-command-in-our-system)
>**Before typing out every parameter you have to create the command - createcustomer**

>1. (CUSTOMER DESTINATION) - You will have to type the office in which you register the package.
<br></br>
>2. (FIRST NAME) - You will have to set the current customers first name.
<br></br>
>3. (LAST NAME) - You will have to set the current customers last name.
<br></br>
>4. (TELEPHONE) - You will have to set the current customers telephone number.
<br></br>
>5. (EMAIL) - You will have to set the current customers email.
#### COMMAND:

`createcustomer (CUSTOMER DESTINATION) (FIRST NAME) (LAST NAME) (TELEPHONE) (EMAIL)`

### ALL CUSTOMER CASES (INCLUDING THE WRONG ONES):
#### INPUT:

```none
VALID INPUT:
createcustomer Melbourne Borislav Bonev 0899999999 bobi@abv.bg

INVALID INPUT:
createcustomer LosSantos Borislav Bonev 0899999999 bobi@abv.bg
createcustomer Melbourne Borislav Bonev 089999999 bobi@abv.bg
```

#### EXPECTED OUTPUT:

```none
VALID OUTPUT:

------------------------------------------------------------------------------
Customer was created in (Melbourne):
Info: [Borislav Bonev] | Number: [0899999999] | Email: (bobi@abv.bg)
------------------------------------------------------------------------------

INVALID OUTPUT

There is no LosSantos in the Australian region
The telephone you are trying to input is not valid (for australia)
```

## 4. CREATE PACKAGE 📦
### [Click to return to the top](#every-command-in-our-system)
>**Before typing out every parameter you have to create the command - createpackage**

>1. (PACKAGE ID) - You will have set a new package by giving it ID.
<br></br>
>2. (PRODUCT NAME) - You will have to set the current package name.
<br></br>
>3. (PACKAGE KG) - You will have to set the current package kilograms.
<br></br>
>4. (CUSTOMER EMAIL) - You will have to type the same email as the customer you registered in the previous command.
<br></br>
>5. (DELIVERY LOCATION) - You will have to set the delivery location (the last location in your route map)

> * BE CAREFUL - When you create a package you must put а valid city (one of the cities from the route you created) That way you are setting the arrival location of the package. If you put anything else that is not in the route the system will throw you an ERROR.
> * BE CAREFUL (2) - We are only working with international shipping so we are not shipping in the same city. The system will throw you again ERROR.
#### COMMAND:

`createpackage (PACKAGE ID) (PRODUCT NAME) (PACKAGE KG) (CUSTOMER EMAIL) (DELIVERY LOCATION)`

### ALL PACKAGE CASES (INCLUDING THE WRONG ONES):
#### INPUT:

```none
VALID INPUT:
createcustomer Melbourne Borislav Bonev 0899999999 bobi@abv.bg
createpackage 1 Fridge 50 bobi@abv.bg AliceSprings

INVALID INPUT:
createpackage 1 Fridge 50 bobi@abv.bg AliceSprings
createcustomer Melbourne Borislav Bonev 0899999999 bobi@abv.bg
createpackage 1 Fridge 50 bobi@abv.bg AliceSprings
createpackage 1 Fridge 50 bobi@abv.bg AliceSprings
createpackage 2 Fridge 50 bobi@abv.bg LosSantos
createpackage 3 Fridge 120 bobi@abv.bg AliceSprings
createpackage 4 Fridge -50 bobi@abv.bg AliceSprings
```

#### EXPECTED OUTPUT:

```none
VALID OUTPUT:

------------------------------------------------------------------------------
Package has been created with id: [1] Status: [OPEN]
Info of package: Name: Fridge | Kilograms: 50 | Customer Email: (bobi@abv.bg) Delivery location: (AliceSprings)
Wating for truck to pick up..
------------------------------------------------------------------------------

INVALID OUTPUT:

Customer with this email does not exist!
Package with id: [1] alredy exists!
There is no LosSantos in the Australian region
Invalid package kilograms (too high or negative)
Invalid package kilograms (too high or negative)
```

## 5. ASSIGN PACKAGE 🚚📦
### [Click to return to the top](#every-command-in-our-system)
>**Before typing out every parameter you have to create the command - assignpackage**

>1. (TRUCK ID) - You will have to give the same ID of the truck you set in the first command.
<br></br>
>2. (ROUTE ID) - You will have to give the same ID of the route you set in the second command.
<br></br>
>3. (PACKAGE ID) - You will have to give the same ID of the route you set in the forth command.

`assignpackage (TRUCK ID) (ROUTE ID) (PACKAGE ID)`

### ALL PACKAGE CASES (INCLUDING THE WRONG ONES):
#### INPUT:

```none
VALID INPUT:

createtruck 1003 5000 8000
createcustomer Brisbane Mario Stanoychev 0849567999 mario@abv.bg
createpackage 1 Televizor 23 mario@abv.bg Adelaide
assignpackage 1003 1 1

INVALID INPUT:

assignpackage 1003 1 1
createtruck 1003 5000 8000
createroute 1 1003 Melbourne->Adelaide->AliceSprings 2023/8/7
assignpackage 1003 1 1
createpackage 1 Televizor 23 mario@abv.bg Adelaide
assignpackage 1003 1 1
```

#### EXPECTED OUTPUT:

```none
VALID OUTPUT:

Package has been created with id: [1] Status: [OPEN]
Info of package: Name: Televizor | Kilograms: 23 | Customer Email: (mario@abv.bg) Delivery location: (Adelaide)
Wating for truck to pick up..
------------------------------------------------------------------------------

INVALID OUTPUT:

Truck: [1003] Scania does not exist!
Package with id: [1] does not exist!
Customer with this email does not exist!
'Brisbane' is not in list
```

## 6. EMPLOYEE LOGIN 🔑
### [Click to return to the top](#every-command-in-our-system)
>**Before typing out every parameter you have to create the command - employeelogin**

>1. (VALID PASSWORD) - After all of the commands, you can type the employee password to check current information about the package.
#### COMMAND:

`employeelogin (VALID PASSWORD)`

### ALL EMPLOYEE LOGIN CASES (INCLUDING THE WRONG ONES):
#### INPUT:

```none
VALID INPUT:

employeelogin mbi10811
createtruck 1003 5000 8000
createroute 1 1003 Melbourne->Adelaide->AliceSprings 2023/8/7
createcustomer Melbourne Borislav Bonev 0899999999 bobi@abv.bg
createpackage 1 Televizor 23 bobi@abv.bg AliceSprings
assignpackage 1003 1 1 
employeelogin mbi10811

INVALID INPUT:

employeelogin test123
```

#### EXPECTED OUTPUT:

```none
VALID OUTPUT:

EMPLOYEE VIEW INFO:
Trucks: No information
Routes: No information
Packages: No information
------------------------------------------------------------------------------
EMPLOYEE VIEW INFO:
Trucks: 1003 - Scania
Routes: 1 - Melbourne->Adelaide->AliceSprings
Packages: 1 - Televizor - 23 - AliceSprings
------------------------------------------------------------------------------

INVALID OUTPUT:

Incorrect password!
```

## 7. MANAGER LOGIN 🗝
### [Click to return to the top](#every-command-in-our-system)
>**Before typing out every parameter you have to create the command - managerlogin**

>1. (VALID PASSWORD) - After all of the commands, you can type the manager password to check current information about the customer.
#### COMMAND:

`managerlogin (VALID PASSWORD)`

### ALL MANAGER LOGIN CASES (INCLUDING THE WRONG ONES):
#### INPUT:

```none
VALID INPUT:

managerlogin manager1000
createtruck 1003 5000 8000
createroute 1 1003 Melbourne->Adelaide->AliceSprings 2023/8/7
createcustomer Melbourne Borislav Bonev 0899999999 bobi@abv.bg
createpackage 1 Televizor 23 bobi@abv.bg AliceSprings
assignpackage 1003 1 1 
managerlogin manager1000

INVALID INPUT:

managerlogin test123
```

#### EXPECTED OUTPUT:

```none
VALID OUTPUT:

MANAGER VIEW INFO:
Customers: No information
------------------------------------------------------------------------------
MANAGER VIEW INFO:
Customers: Melbourne - Borislav - Bonev - 0899999999 - bobi@abv.bg
------------------------------------------------------------------------------

INVALID OUTPUT:

Incorrect password!
```

# VALID PROGRAM INPUT:

### This is example of how the system works:

> It shows 3 customers packages being transferred by different trucks on different routs. Our system will even show you the expected arrival time for every single destination. If you have done everything correctly, you will be ready to service a shipment.

#### INPUT:

```none
createtruck 1003 5000 8000
createtruck 1011 6000 10000
createtruck 1027 7000 13000
createroute 1 1003 Melbourne->Adelaide->AliceSprings 2023/8/7
createroute 2 1011 Sydney->Adelaide->AliceSprings->Perth 2023/8/7
createroute 3 1027 Brisbane->AliceSprings->Adelaide 2023/8/7
createcustomer Sydney Borislav Bonev 0899999999 bobi@abv.bg
createcustomer Melbourne Ivaylo Petrov 0899568999 ivaylo@abv.bg
createcustomer Brisbane Mario Stanoychev 0849567999 mario@abv.bg
createpackage 1 Televizor 23 mario@abv.bg Adelaide
createpackage 2 Fridge 50 ivaylo@abv.bg AliceSprings
createpackage 3 Chair 10 bobi@abv.bg Perth
assignpackage 1027  3 1
assignpackage 1003 1 2
assignpackage 1011  2 3
managerlogin manager1000
employeelogin mbi10811
end
```

#### EXPECTED OUTPUT:
```none
------------------------------------------------------------------------------
Truck Scania with id: [1003] was created!
------------------------------------------------------------------------------
Truck Scania with id: [1011] was created!
------------------------------------------------------------------------------
Truck Scania with id: [1027] was created!
Route with id: [1] has been created:
Route: [Melbourne->Adelaide->AliceSprings]
Assigned to truck: [1003] Scania
------------------------------------------------------------------------------
Route with id: [2] has been created:
Route: [Sydney->Adelaide->AliceSprings->Perth]
Assigned to truck: [1011] Scania
------------------------------------------------------------------------------
Route with id: [3] has been created:
Route: [Brisbane->AliceSprings->Adelaide]
Assigned to truck: [1027] Scania
------------------------------------------------------------------------------
Customer was created in (Sydney):
Info: [Borislav Bonev] | Number: [0899999999] | Email: (bobi@abv.bg)
------------------------------------------------------------------------------
Customer was created in (Melbourne):
Info: [Ivaylo Petrov] | Number: [0899568999] | Email: (ivaylo@abv.bg)
------------------------------------------------------------------------------
Customer was created in (Brisbane):
Info: [Mario Stanoychev] | Number: [0849567999] | Email: (mario@abv.bg)
------------------------------------------------------------------------------
Package has been created with id: [1] Status: [OPEN]
Info of package: Name: Televizor | Kilograms: 23 | Customer Email: (mario@abv.bg) Delivery location: (Adelaide)
Wating for truck to pick up..
------------------------------------------------------------------------------
Package has been created with id: [2] Status: [OPEN]
Info of package: Name: Fridge | Kilograms: 50 | Customer Email: (ivaylo@abv.bg) Delivery location: (AliceSprings)
Wating for truck to pick up..
------------------------------------------------------------------------------
Package has been created with id: [3] Status: [OPEN]
Info of package: Name: Chair | Kilograms: 10 | Customer Email: (bobi@abv.bg) Delivery location: (Perth)
Wating for truck to pick up..
------------------------------------------------------------------------------
Package [1] has been assigned to truck:
Truck Info: [1027] Scania
Current route: Brisbane -> AliceSprings -> Adelaide
Departure time - Expected delivery time in different locations: Brisbane->(08/07/2023, 10:00:00) | AliceSprings->(08/08/2023, 03:00:00) | Adelaide->(08/08/2023, 20:00:00)
Kilograms left on the truck: (6977)
Status: PROCESSING
------------------------------------------------------------------------------
Package [2] has been assigned to truck:
Truck Info: [1003] Scania
Current route: Melbourne -> Adelaide -> AliceSprings
Departure time - Expected delivery time in different locations: Melbourne->(08/07/2023, 10:00:00) | Adelaide->(08/07/2023, 19:00:00) | AliceSprings->(08/08/2023, 04:00:00)
Kilograms left on the truck: (4950)
Status: PROCESSING
------------------------------------------------------------------------------
Package [3] has been assigned to truck:
Truck Info: [1011] Scania
Current route: Sydney -> Adelaide -> AliceSprings -> Perth
Departure time - Expected delivery time in different locations: Sydney->(08/07/2023, 10:00:00) | Adelaide->(08/08/2023, 14:00:00) | AliceSprings->(08/09/2023, 18:00:00) | Perth->(08/10/2023, 22:00:00)
Kilograms left on the truck: (5990)
Status: PROCESSING
------------------------------------------------------------------------------
MANAGER VIEW INFO:
Customers: Sydney - Borislav - Bonev - 0899999999 - bobi@abv.bg / Melbourne - Ivaylo - Petrov - 0899568999 - ivaylo@abv.bg / Brisbane - Mario - Stanoychev - 0849567999 - mario@abv.bg
------------------------------------------------------------------------------

EMPLOYEE VIEW INFO:
Trucks: 1003 - Scania / 1011 - Scania / 1027 - Scania
Routes: 1 - Melbourne->Adelaide->AliceSprings / 2 - Sydney->Adelaide->AliceSprings->Perth / 3 - Brisbane->AliceSprings->Adelaide 
Packages: 1 - Televizor - 23 - Adelaide / 2 - Fridge - 50 - AliceSprings / 3 - Chair - 10 - Perth
------------------------------------------------------------------------------
```
