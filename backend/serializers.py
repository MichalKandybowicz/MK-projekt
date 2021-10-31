from rest_framework import serializers

from backend.models import Attack, VillageDetailInformation


class AttackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attack
        fields = ['url', 'defender_cords', 'attacker_cords', 'distance',
                  'attack_type', 'entry_time', 'defender_name', 'attacker_name']


class VillageDetailInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillageDetailInformation
        fields = ['url', 'x', 'y', 'troops_type', 'lose_off', 'created', 'modified']


"""

const api_url = 
      "https://project4cv.herokuapp.com/api/attacks/";
  
// Defining async function
async function getapi(url) {
    
    // Storing response
    const response = await fetch(url);
    
    // Storing data in form of JSON
    var data = await response.json();
    console.log(data);
    if (response) {
        hideloader();
    }
    show(data);
}
// Calling that async function
getapi(api_url);
  

"""
