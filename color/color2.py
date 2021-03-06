#!/usr/bin/python3
import crayons

def main ():
    print(crayons.red('red string'))
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    crayons.disable()
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    crayons.DISABLE_COLOR = False

    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    print(crayons.red('red string', bold=True))

    print(crayons.yellow('yellow string', bold=True))

    print(crayons.magenta('magenta string', bold=True))

    print(crayons.white('white string', bold=True))

main()
