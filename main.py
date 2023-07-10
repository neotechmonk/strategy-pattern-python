from support.app import CustomerSupport, fifo_strategy
from support.ticket import SupportTicket


class BlackHoleOrderingStrategy():
        """ New order strategy implemented at a later stage to scale the order approach"""
        def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
             return []

def main():
    # create the application
    app = CustomerSupport()

    # register a few tickets
    app.add_ticket(SupportTicket("John Smith", "My computer makes strange sounds!"))
    app.add_ticket(
        SupportTicket("Linus Sebastian", "I can't upload any videos, please help.")
    )
    app.add_ticket(
        SupportTicket("Arjan Codes", "VSCode doesn't automatically solve my bugs.")
    )

    # process the tickets
    app.process_tickets(processing_strategy=fifo_strategy)


if __name__ == "__main__":
    main()