Practising different approaches to the Strategy Design Pattern based Arjan's YT tutorial

[Original source code](https://github.com/ArjanCodes/2021-pythonic-strategy)
[Youtube link](https://www.youtube.com/watch?app=desktop&v=n2b_Cxh20Fw)

## Learning outcomes
Allows to injection of behavior without the application know about the implementation
of the beahavior. 

This is achived by definition of an interface or a contract which is seperate from the implmentation details 

1. OO Strategy Implementation with Abstract Classes (Classic Approach)
1. OO Composition based approach
1. Protocol based approach
1. Functional approach

Use differnt branch names to explore different Strategy patterns


### 1. OO Strategy Implementation with Abstract Classes
abstract class `TicketOrderingStrategy` is implmented by `FIFOOrderingStrategy` , `LIFOOrderingStrategy`, `RandomOrderingStrategy`

This allows for `CustomerSuppport.process_tickets()` to be not aware of the ticket ordering logic. The approach allows the code to scale by implementing additional `TicketOrderingStrategy` implementations to be instroduced in the future. 

However, there is no need to change the code in the `CustomerSuppport` class