import pexpect
import getpass

def get_wallet_address(seed_phrase, index):
    # command to derive the address using solana-keygen
    cmd = f'solana-keygen pubkey \"prompt:?key={index}/0\"'
    # spawn the child process
    child = pexpect.spawn(cmd, encoding='utf-8')

    # wait exactly for the seed-phrase prompt
    child.expect_exact('[pubkey recovery] seed phrase:')
    child.sendline(seed_phrase)

    # wait for bip39 passphrase prompt (if none, just press enter)
    child.expect(r'If this seed phrase has an associated passphrase.*continue:')
    child.sendline('')

    # wait for the command to fully finish
    child.expect(pexpect.EOF)

    # parse the final output line for the derived address
    output_lines = child.before.strip().split('\\n')
    address = output_lines[-1].strip()
    return address

def main():
    # quietly get the seed phrase (like a password)
    seed_phrase = getpass.getpass('Enter your phantom seed phrase: ')
    # how many addresses to generate
    num_addresses = int(input('Enter the number of addresses to derive: '))
    print("\n")
    # store addresses in addresses.txt
    with open('addresses.txt', 'w') as file:
        for i in range(num_addresses):
            address = get_wallet_address(seed_phrase, i)
            print(f'{address}')
            file.write(f'{address}\n')

    print('\nAll addresses have been saved to addresses.txt\n')

if __name__ == '__main__':
    main()
