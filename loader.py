#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_wo_scan():
    wo_scan = input("Scan Workorder: ")
    return wo_scan


def main():
    wo_id = get_wo_scan()
    print(wo_id)

if __name__ == '__main__':
    main()

