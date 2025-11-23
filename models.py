from django.db import models
from django.contrib.auth.models import User

# Model for missing children
class MissingChild(models.Model):
    person_name = models.CharField(max_length=60)
    child_name = models.CharField(max_length=60)
    contact_no = models.CharField(max_length=20)
    location = models.CharField(max_length=120)
    image = models.ImageField(upload_to='missing_children/')
    upload_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, default='Pending')

# Model for Parent Registration
class ParentSignup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=30)
    occupation = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    document = models.FileField(upload_to='parent_documents/')
    child_age = models.CharField(max_length=20)
    child_color = models.CharField(max_length=20)

# Adoption details
class Adoption(models.Model):
    parent = models.ForeignKey(ParentSignup, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=50)
    adoption_date = models.DateTimeField(auto_now_add=True)

# Model for found children (not yet identified)
class FoundChild(models.Model):
    found_location = models.CharField(max_length=120)
    image = models.ImageField(upload_to='found_children/')
    date_found = models.DateTimeField(auto_now_add=True)
    additional_info = models.TextField()
    status = models.CharField(max_length=50, default='Unidentified')

# Model for police reports
class PoliceReport(models.Model):
    officer_name = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20)
    missing_child = models.ForeignKey(MissingChild, on_delete=models.CASCADE)
    report_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')

# Model for user-submitted reports
class UserReport(models.Model):
    reporter_name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=20)
    child_description = models.TextField()
    location = models.CharField(max_length=120)
    image = models.ImageField(upload_to='user_reports/')
    report_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Under Review')

# Model for face recognition logs
class FaceRecognitionLog(models.Model):
    uploaded_image = models.ImageField(upload_to='face_logs/')
    matched_child = models.ForeignKey(MissingChild, on_delete=models.SET_NULL, null=True, blank=True)
    match_confidence = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
