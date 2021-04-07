from rest_framework import serializers

from backend.models import Attack


class AttackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attack
        fields = ['url', 'defender_x', 'defender_y', 'attacker_x', 'attacker_y', 'attack_type',
                  'entry_time', 'send_time', 'defender_name', 'attacker_name'
                  ]
