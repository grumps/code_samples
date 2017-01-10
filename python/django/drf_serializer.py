__author__ = 'Maxwell J. Resnick'

from authentication.serializers import AccountSerializer
from Customers.models import Customer, PartnerType

from rest_framework import serializers


class PartnerTypeSerializer(serializers.ModelSerializer):

    """
    Serializer for PartnerType model
    This is a read only class, and is "pre defined"
    """
    class Meta:
        model = PartnerType
        fields = ('id', 'title',)
        read_only_fields = ('id', 'title',)


class CustomerSerializer(serializers.ModelSerializer):

    """
    CustomerSerializer create and update a Customer object & relationships
    Attributes:
     * partner_1_title PrimaryKeyRelatedField to partnertype endpoint
     * partner_2_title PrimaryKeyRelatedField to partnertype endpoint
    """
    partner_1_title = serializers.PrimaryKeyRelatedField(
        write_only=True, required=True,
        queryset=PartnerType.objects.all())
    partner_2_title = serializers.PrimaryKeyRelatedField(
        write_only=True, required=True,
        queryset=PartnerType.objects.all())
    accounts = AccountSerializer

    class Meta:
        model = Customer
        fields = ('id', 'partner_1_type', 'partner_2_type',
                  'partner_1_name', 'partner_2_name',
                  'partner_1_party_size',
                  'partner_2_party_size', 'partner_1_title',
                  'partner_2_title',
                  )
        read_only_fields = ('id', 'created', 'modified')
        # follow relationship 1 level deep.
        depth = 1

    def create(self, validated_data):
        # our validated data, contains our relationships
        # however we need create w/ the relations excluded
        # from the wedding object
        _partner_1_type = validated_data.pop('partner_1_title')
        _partner_2_type = validated_data.pop('partner_2_title')
        return Customer.objects.create(partner_1_type=_partner_1_type,
                                      partner_2_type=_partner_2_type,
                                      **validated_data)
