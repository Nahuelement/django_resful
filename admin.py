#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 20:18:19 2022

@author: nahuelperugi
"""

from django.contrib import admin

class DronesAdminSite(admin.AdminSite):
    title_header = 'Drones'
    site_header = 'Drones administration'
    index_title = 'Drones site admin'