#!/usr/bin/python3
from lib.main import main
from imports.common_import import exit, run, Console

if __name__ == '__main__':
    try:
        run(main())
    except KeyboardInterrupt:
        Console.print('\n[bold red1][!][/bold red1] Scan interrupted. Goodbye!', style="bold")
        exit(1)
