<img align="left" src="https://cdn.discordapp.com/attachments/1134577424538017793/1137411856751939594/image.png" alt="logo" width="180px"/>

# MBI EXPRESS SYSTEM GUIDE

Hello and welcome to every new employee in our company. Here you will find everything about our application. 
We specially created this `employee handbook` to help you understand how to work with our **commands** in the most easiest way. 
<br></br>
(BE AWARE - FOLLOW THE COMMANDS ORDER)
<br></br>
(BY DOING EVERYTHING IN ORDER/CORRECTLY YOU WILL BE ABLE TO SERVICE A SHIPMENT)

<br></br>
<br></br>


## EVERY COMMAND IN OUR SYSTEM:

<!-- TRUCKS -->

### 🚚 CreateTruck Commands:
> This command set's a truck by giving it a capacity and also maximum range.


**[CreateTruck](#1-create-specific-truck) - (TRUCK ID) (TRUCK CAPACITY) (TRUCK MAX RANGE)**

*(You can click here to see how the command works)*
<!-- ROUTE -->

### 🛣 Route Command:

> This command maps a new route and appoints the trucks on it from the first command.

**[CreateRoute](#2-create-route) - (ROUTE ID) | (TRUCK ID) | (MAPPING ROUTE) (DATE)**

*(You can click here to see how the command works)*

<!-- CUSTOMER -->

### 👷‍♂ Customer Command:

>This command is used when a new customer comes in one of our offices (our employees gather his information and they enter it into the system)

**[CreateCustomer](#3-create-customer) - (OFFICE-CITY) | (FIRST NAME) | (LAST NAME) | (TELEPHONE) (EMAIL)**

*(You can click here to see how the command works)*

<!-- PACKAGE -->

### 📦 Package Command:

>This command is used right after the customer command, it registers a new package in our system from the customers email.

**[CreatePackage](#4-create-package) - (PACKAGE ID) | (PACKAGE NAME) | (PACKAGE KG) | (CUSTOMER EMAIL) | (OFFICE-CITY)**

*(You can click here to see how the command works)*

<!-- EMPLOYEE LOGIN -->

### 🔑 Employee Access Command:

>This command gives a restricted information to our employees about the current: packages, routes, trucks 

**[EmployeeLogin](#5-employee-login) - (VALID PASSWORD)**

*(You can click here to see how the command works)*

<!-- MANAGER LOGIN -->

### 🗝 Manager Access Command:

>This command gives a restricted information to our managers about the current customers information (Used only in case of errors and other problems)

**[ManagerLogin](#6-manager-login)  - (VALID PASSWORD)**

*(You can click here to see how the command works)*
 

<img align="left" src="https://cdn.discordapp.com/attachments/1134577424538017793/1137411856751939594/image.png" alt="logo" width="180px"/>


# COMMANDS FUNCTIONALITY WITH GUIDE AND EXAMPLES:

**DESCRIPTION OF ALL COMMANDS AND HOW ARE THEY USED**
<br></br>
<br></br>
<br></br>

## 1. CREATE SPECIFIC TRUCK
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
createtruck 1003 42000 8000
createtruck 1003 42000 8000
createtruck 1003 6000 8000
createtruck 1003 42000 9000
createtruck 1011 37000 10000
createtruck 1011 37000 10000
createtruck 1026 26000 13000
createtruck 1026 26000 13000
createtruck 1050 42000 8000
```
#### EXPECTED OUTPUT:

```none
Truck Scania with id: [1003] already exists!
Invalid capacity for truck with model Scania
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

## 2. CREATE ROUTE
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
createroute 1 1003 Sydney->Melbourne->AliceSprings 2023/8/7
createtruck 1003 42000 8000
createroute 1 1003 Sydney->Melbourne->AliceSprings 2023/8/7
createroute 2 1003 Sydney->Melbourne->AliceSprings 2023/8/0
createroute 1 1004 Sydney->Melbourne->AliceSprings 2023/8/7
createroute 3 1004 Sydney->Melbourne->AliceSprings 202/8/7
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

## 3. CREATE CUSTOMER
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
createcustomer Melbourne Borislav Bonev 0899999999 bobi@abv.bg
createcustomer LosSantos Borislav Bonev 0899999999 bobi@abv.bg
createcustomer Melbourne Borislav Bonev 089999999 bobi@abv.bg
```

#### EXPECTED OUTPUT:

```none
There is no LosSantos in the Australian region
The telephone you are trying to input is not valid (for australia)
------------------------------------------------------------------------------
Customer was created in (Melbourne):
Info: [Borislav Bonev] | Number: [0899999999] | Email: (bobi@abv.bg)
------------------------------------------------------------------------------
```

## 4. CREATE PACKAGE
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
#### COMMAND:

`createpackage (PACKAGE ID) (PRODUCT NAME) (PACKAGE KG) (CUSTOMER EMAIL) (DELIVERY LOCATION)`

### ALL PACKAGE CASES (INCLUDING THE WRONG ONES):
#### INPUT:

```none
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
Customer with this email does not exist!
Package with id: [1] alredy exists!
There is no LosSantos in the Australian region
Invalid package kilograms (too high or negative)
Invalid package kilograms (too high or negative)
------------------------------------------------------------------------------
Package has been created with id: [1] Status: [OPEN]
Info of package: Name: Fridge | Kilograms: 50 | Customer Email: (bobi@abv.bg) Delivery location: (AliceSprings)
Wating for truck to pick up..
------------------------------------------------------------------------------
```

## 5. EMPLOYEE LOGIN
>**Before typing out every parameter you have to create the command - employeelogin**

>1. (VALID PASSWORD) - After all of the commands, you can type the employee password to check current information about the package.
#### COMMAND:

`employeelogin (VALID PASSWORD)`

### ALL EMPLOYEE LOGIN CASES (INCLUDING THE WRONG ONES):
#### INPUT:

```none
employeelogin test123
employeelogin mbi10811
Createtruck 1003 5000 8000
createroute 1 1003 Melbourne->Adelaide->AliceSprings 2023/8/7
CreateCustomer Melbourne Borislav Bonev 0899999999 bobi@abv.bg
createpackage 1 Televizor 23 bobi@abv.bg AliceSprings
assignpackage 1003 1 1 
managerlogin manager1000
employeelogin mbi10811
```

#### EXPECTED OUTPUT:

```none
Incorrect password!
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
```

## 6. MANAGER LOGIN
>**Before typing out every parameter you have to create the command - managerlogin**

>1. (VALID PASSWORD) - After all of the commands, you can type the manager password to check current information about the customer.
#### COMMAND:

`managerlogin (VALID PASSWORD)`

### ALL MANAGER LOGIN CASES (INCLUDING THE WRONG ONES):
#### INPUT:

```none
managerlogin test123
managerlogin manager1000
Createtruck 1003 5000 8000
createroute 1 1003 Melbourne->Adelaide->AliceSprings 2023/8/7
CreateCustomer Melbourne Borislav Bonev 0899999999 bobi@abv.bg
createpackage 1 Televizor 23 bobi@abv.bg AliceSprings
assignpackage 1003 1 1 
managerlogin manager1000
employeelogin mbi10811
```

#### EXPECTED OUTPUT:

```none
Incorrect password!
MANAGER VIEW INFO:
Customers: No information
------------------------------------------------------------------------------
MANAGER VIEW INFO:
Customers: Melbourne - Borislav - Bonev - 0899999999 - bobi@abv.bg
------------------------------------------------------------------------------
```
