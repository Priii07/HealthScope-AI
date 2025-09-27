import requests
import json

def test_fda_api():
    """Test if we can get drug info from FDA"""
    
    print("🧪 Testing FDA API...")
    
    # Simple FDA drug query - no API key needed!
    url = "https://api.fda.gov/drug/label.json"
    params = {
        'search': 'openfda.brand_name:Lipitor',
        'limit': 1
    }
    
    try:
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            print("✅ FDA API works!")
            print(f"📊 Found drug data")
            
            # Show what we got
            if data.get('results'):
                drug = data['results'][0]
                brand_name = drug.get('openfda', {}).get('brand_name', ['Unknown'])[0]
                generic_name = drug.get('openfda', {}).get('generic_name', ['Unknown'])[0]
                
                print(f"Brand: {brand_name}")
                print(f"Generic: {generic_name}")
                
            return True
        else:
            print(f"❌ Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_fda_api()
