<img src="https://cdn.discordapp.com/attachments/1134577424538017793/1137411856751939594/image.png" alt="logo" width="180px" style="margin-top: 20px; border-radius: 50%; display: block; margin-left: auto; margin-right: auto;"/>

# MBI EXPRESS SYSTEM GUIDE

Привет на всички работници в този `employee handbook` вие постоянно ще знаете как се работи със системата в случай, че забравите някоя **команда** или **функционалност** всичко е описано тук:



## ВСИЧКИ КОМАНДИ ЗА ВСЕКИ РАБОТНИК:

<br></br>
<!-- TRUCKS -->

### 🚚 CreateTruck Commands:
> Info about the command [BOBI]


**[CreateTruck](#1-create-specific-truck) - (TRUCK ID) (TRUCK CAPACITY) (TRUCK MAX RANGE)**

*! CLICK TO SEE HOW COMMAND WORKS !*
<!-- ROUTE -->

### 🛣 Route Command:

> Info about the command [BOBI]

**[CreateRoute](#2-create-route) - (ROUTE ID: 1 - ~) | (TRUCK ID) | (CURRENT ROUTE) (DATE)**

*! CLICK TO SEE HOW COMMAND WORKS !*

<!-- CUSTOMER -->

### 👷‍♂ Customer Command:

>Info about the command [BOBI]

**[CreateCustomer](#3-create-customer) - (CUSTOMER CITY) | (FIRST NAME) | (LAST NAME) | (TELEPHONE) (EMAIL)**

*! CLICK TO SEE HOW COMMAND WORKS !*

<!-- PACKAGE -->

### 📦 Package Command:

>Info about the command [BOBI]

**[CreatePackage](#4-create-package) - (PACKAGE ID) | (PACKAGE NAME) | (PACKAGE KG) | (CUSTOMER EMAIL) | (CUSTOMER CITY)**

*! CLICK TO SEE HOW COMMAND WORKS !*

<!-- EMPLOYEE LOGIN -->

### 🔑 Employee Access Command:

>Info about the command [BOBI] 

**[EmployeeLogin](#5-employee-login) - (VALID PASSWORD)**

*! CLICK TO SEE HOW COMMAND WORKS !*

<!-- MANAGER LOGIN -->

### 🗝 Manager Access Command:

>Info about the command [BOBI]

**[ManagerLogin](#6-manager-login)  - (VALID PASSWORD)**

*! CLICK TO SEE HOW COMMAND WORKS !*
 

<img src="https://cdn.discordapp.com/attachments/1134577424538017793/1137411856751939594/image.png" alt="logo" width="180px" style="margin-top: 20px; border-radius: 50%; display: block; margin-left: auto; margin-right: auto;"/>


# COMMANDS FUNCTUONALITY WITH GUIDE AND EXAMPLES:

**ОПИСАНИЕ НА ВСИЧКИ КОМАНДИ И КАК ТЕ СЕ ПОЛЗВАТ СЪС ПРИМЕРИ И ОБЯСНСНИЕЯ: [BOBI]**

## 1. CREATE SPECIFIC TRUCK

>Info about the command [BOBI]

| Truck | ID |Capacity | Max Range |
| :---  | :---:  |   :---:  |      :---: |
| Scania | 1003-1010  | 42,000kg | 8,000km     |
| Man | 1011-1025  | 37,000kg | 10,000km     |
| Actros | 1026-1040  | 26,000kg | 13,000km     |

#### COMMANDS:

`SCANIA - createtruck (ID: 1003 - 1010) (CAPACITY) (MAX_RANGE)`

`MAN - createtruck (ID: 1011 - 1025) (CAPACITY) (MAX_RANGE)`

`ACTROS - createtruck (ID: 1026 - 1040) (CAPACITY) (MAX_RANGE)`

### ALL TRUCK CASES:
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
>Info about the command [BOBI]
#### COMMAND:

`createroute (ROUTE ID: 1 - ~) (TRUCK ID) (CURRENT ROUTE) (DATE)`

### ALL ROUTE CASES:
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
>Info about the command [BOBI]
#### COMMAND:

`createcustomer (CUSTOMER DESTINATION) (FIRST NAME) (LAST NAME) (TELEPHONE) (EMAIL)`

### ALL CUSTOMER CASES:
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
>Info about the command [BOBI]
#### COMMAND:

`createpackage (PACKAGE ID) (PRODUCT NAME) (PACKAGE KG) (CUSTOMER EMAIL) (DELIVERY LOCATION)`

### ALL PACKAGE CASES:
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
>Info about the command [BOBI]
#### COMMAND:

`employeelogin - (VALID PASSWORD)`

### ALL EMPLOYEE LOGIN CASES:
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
>Info about the command [BOBI]
#### COMMAND:

`managerlogin - (VALID PASSWORD)`

### ALL MANAGER LOGIN CASES:
#### INPUT:

```none
managerlogin - test123
managerlogin - manager1000
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
