import random
from typing import Callable

from support.ticket import SupportTicket

TicketOrderingStrategy = Callable[[list[SupportTicket]], list [SupportTicket]]


class FIFOOrderingStrategy():
    def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return tickets.copy()
    
class LIFOOrderingStrategy():
    def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return list(reversed(tickets))
    
class RandomOrderingStrategy():
    def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return random.sample(tickets,len(tickets))
    
    


class CustomerSupport:
    def __init__(self):
        self.tickets: list[SupportTicket] = []

    def add_ticket(self, ticket: SupportTicket):
        self.tickets.append(ticket)

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):

        ticket_list = processing_strategy(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return
        
        for ticket in ticket_list:
            ticket.process()
