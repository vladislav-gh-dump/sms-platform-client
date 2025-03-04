import argparse
import sys
from .send_sms import send_sms
from .logger import logger


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sender", help="Sender's phone number")
    parser.add_argument("recipient", help="Recipient's phone number")
    parser.add_argument("message", help="Message text")
    
    if len(sys.argv) != 4:
        logger.error("Not enough arguments provided")
        print("Argument Error: Not enough arguments provided")
        sys.exit(1)
    
    args = parser.parse_args()
    logger.info(f"Args:\nSender: {args.sender}\nRecipient: {args.recipient}\nMessage: {args.message}")
    
    send_sms(args.sender, args.recipient, args.message)


if __name__ == "__main__":
    main()
