from rest_framework import serializers
from decoratorapi.models import Branch,Student
from django.core.validators import EmailValidator, MinLengthValidator


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = "__all__"



class StudentSerializer(serializers.ModelSerializer):
    student_branch=BranchSerializer(many=True)  #Accessing many to many fields also
    country_info=serializers.SerializerMethodField()



    class Meta:
        model = Student
        fields = "__all__"
        # depth=1        #Accessing many to many fields also


    def get_country_info(self,student):
        return "India"



    student_name = serializers.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(limit_value=2, message="Name should have at least 2 characters.")
        ]
    )

    # Adding validation for email field
    student_email = serializers.EmailField(
        validators=[
            EmailValidator(message="Enter a valid email address.")
        ]
    )

    # class Meta:
    #     model = Student
    #     fields = ['name', 'email']  # Note: Use a list for fields, not a set

    def validate_name(self, value):
        # Custom validation for the name field
        # You can add more complex validation logic here if needed
        if value == "InvalidName":
            raise serializers.ValidationError("Invalid name. Please provide a valid name.")
        return value

    def validate_email(self, value):
        # Custom validation for the email field
        # You can add more complex validation logic here if needed
        if "example.com" in value:
            raise serializers.ValidationError("Email domain 'example.com' is not allowed.")
        return value