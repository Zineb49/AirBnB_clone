#!/bin/bash

# File @generated by hack/generate-authors.sh. DO NOT EDIT.
# This file lists all contributors to the repository.
# See hack/generate-authors.sh to make modifications.

git log --format='%aN <%aE>' | sort -u > AUTHORS

