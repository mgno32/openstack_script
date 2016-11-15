#!/bin/bash

source admin-openrc.sh

echo "------endpoint list------"
keystone endpoint-list
echo ""

echo "------service list------"
keystone service-list
echo ""

echo "-------user list------"
keystone role-list
echo ""

echo "------tenant list------"
keystone tenant-list
echo ""

echo "------role list------"
keystone role-list
echo ""