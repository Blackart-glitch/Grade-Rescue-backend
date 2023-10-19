from config.dbconnect import mysql
from flask import Blueprint, request, jsonify

token = Blueprint('token', __name__)
