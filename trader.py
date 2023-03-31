import sys
import json
import random

def update_state(state):
    with open('state.json', 'w') as f:
        json.dump(state, f)

def get_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def get_state():
    with open('state.json', 'r') as f:
        return json.load(f)

def get_rate(state):
    print(round(state['usd_rate'], 2))

def get_available(state):
    print(f"USD {round(state['usd_balance'], 2)} UAH {round(state['uah_balance'], 2)}")


def buy_usd(amount, state):
    if amount == 'ALL':
        amount = state['uah_balance'] / state['usd_rate']
    else:
        amount = float(amount)

    required_uah = amount * state['usd_rate']
    if state['uah_balance'] >= required_uah:
        state['usd_balance'] += amount
        state['uah_balance'] -= required_uah
        update_state(state)
    else:
        print(f"UNAVAILABLE, REQUIRED BALANCE UAH {round(required_uah, 2)}, AVAILABLE {round(state['uah_balance'], 2)}")

def sell_usd(amount, state):
    if amount == 'ALL':
        amount = state['usd_balance']

    amount = float(amount)
    required_usd = amount

    if state['usd_balance'] >= required_usd:
        state['uah_balance'] += amount * state['usd_rate']
        state['usd_balance'] -= required_usd
        update_state(state)
    else:
        print(f"UNAVAILABLE, REQUIRED BALANCE USD {round(required_usd, 2)}, AVAILABLE {round(state['usd_balance'], 2)}")


def next_rate(state, config):
    new_rate = random.uniform(state['usd_rate'] - config['delta'], state['usd_rate'] + config['delta'])
    state['usd_rate'] = new_rate
    update_state(state)

def restart(config):
    initial_state = {
        "usd_rate": config['initial_usd_rate'],
        "uah_balance": config['initial_uah_balance'],
        "usd_balance": config['initial_usd_balance']
    }
    update_state(initial_state)

def main():
    if len(sys.argv) < 2:
        print("Usage: python trader.py <command>")
        print("Commands: RATE, AVAILABLE, BUY <amount>, SELL <amount>, NEXT, RESTART")
        return

    config = get_config()
    state = get_state()
    command = sys.argv[1]

    if command == 'RATE':
        get_rate(state)
    elif command == 'AVAILABLE':
        get_available(state)
    elif command.startswith('BUY'):
        if len(sys.argv) > 2:
            amount = sys.argv[2]
            buy_usd(amount, state)
        else:
            print("Error: Please provide an amount to buy (e.g., BUY 100)")
    elif command.startswith('SELL'):
        if len(sys.argv) > 2:
            amount = sys.argv[2]
            sell_usd(amount, state)
        else:
            print("Error: Please provide an amount to sell (e.g., SELL 100)")
    elif command == 'NEXT':
        next_rate(state, config)
    elif command == 'RESTART':
        restart(config)
    else:
        print('Unknown command')

if __name__ == "__main__":
    main()



