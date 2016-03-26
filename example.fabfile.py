# coding: utf-8
import os
from fabric.api import run, env, cd, roles, lcd, local, sudo

def gp():
    lcd('/media/roxy/Users/Администратор/Downloads/sites/dmg/')
    local('sudo git add .')
    local('sudo git commit -a')
    local('sudo git push origin master')