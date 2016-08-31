#!/bin/python

import os, sys

def softlinks():
    folders = ['Documents', 'Downloads', 'Music','Pictures', 'Programming', 'Videos', 'Writing']
    for folder in folders:
        if folder in os.listdir('/media/D/'):
            os.system('ln -s /media/D/{} ~/{}'.format(folder, folder))
        else:
            print("folder not found: {}".format(folder))

           
if __name__ == '__main__':
    try:
        function = eval(input('function?: '))
    except Exception as ex:
        print("[-] function not found: {}".format(function))
        print(ex.message)
    function()
