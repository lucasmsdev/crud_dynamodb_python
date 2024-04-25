from decimal import Decimal 
from pprint import pprint
from botocre.exceptions import ClientError
import boto3

def update_movie(title,year):
    region=boto3.session.Session().region_name
    dynamodb = boto3.resource('dynamodb', region_name=region) # low-level client
    
    table = dynamodb.Table('movies'):
        
        try:
            resp