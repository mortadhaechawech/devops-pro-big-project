# tests/test_app.py
import json
import sys
import os

# Add src to path so we can import app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from app import lambda_handler

def test_lambda_handler_returns_200():
    """Test that the Lambda handler returns a 200 status code."""
    event = {}
    context = {}
    
    response = lambda_handler(event, context)
    
    assert response['statusCode'] == 200
    print("✅ Test passed: Status code is 200")

def test_lambda_handler_returns_json():
    """Test that the Lambda handler returns valid JSON."""
    event = {}
    context = {}
    
    response = lambda_handler(event, context)
    body = json.loads(response['body'])
    
    assert 'message' in body
    assert 'environment' in body
    assert 'timestamp' in body
    print("✅ Test passed: Response contains required fields")

if __name__ == '__main__':
    test_lambda_handler_returns_200()
    test_lambda_handler_returns_json()
    print("🎉 All tests passed!")