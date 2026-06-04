seat_type = input('Enter seat type ( General / Sleeper / AC / Luxury): ').lower()


match seat_type:
    case 'general':
        print('General - Cheapest option, no reservation.')
    case 'sleeper':
        print('Sleeper - No AC, beds available.')
    case 'ac':
        print('AC - Air Conditioned, comfy ride.')
    case 'luxury':
        print('Luxury - Premium seats with meals.')
    case _:
        print('Invalid seat type.')