#!/usr/bin/env python3
# ---------------------------------------------------------
# File:        common.py
# Author:      Mathias Hellsten (hathaum@disroot.org)
# Created:     <2025-11-16>
#
# Description:
#   Common utulities for the BitGym suite of scripts.
#
# License:
#   MIT License <https://mit-license.org/>
# ---------------------------------------------------------


# Base conversions
def dec_to_bin(n: int) -> str:
    return format(n, "08b")

def bin_to_dec(b: str) -> int:
    return int(b, 2)

def dec_to_hex(n: int) -> str:
    return format(n, "02X")

def hex_to_dec(h: str) -> int:
    return int(h, 16)

def bin_to_hex(b: str) -> str:
    return format(int(b, 2), "02X")

def hex_to_bin(h: str) -> str:
    return format(int(h, 16), "08b")


# Continuation request
def ask_continue() -> bool:
    answer = input("Another? (y/n): ").strip().lower()
    return answer == "y"








def main():
    """
    Main entry point of the script.
    """
    pass  # Replace with your code


if __name__ == "__main__":
    main()