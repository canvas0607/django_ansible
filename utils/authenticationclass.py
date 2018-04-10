# _*_ coding: utf-8 _*_
# email: canvas0607@gamil.com
__author__ = 'canvas'
__date__ = '2017/12/19 10:17'

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

#auth_pattern = (JSONWebTokenAuthentication, SessionAuthentication)
auth_pattern = (JSONWebTokenAuthentication,)
