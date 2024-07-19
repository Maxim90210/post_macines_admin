from django.db import models

class Locker(models.Model):
    locker_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20)  # Наприклад, 'active', 'inactive'

    def __str__(self):
        return f"{self.location} - {self.status}"

class Compartment(models.Model):
    compartment_id = models.AutoField(primary_key=True)
    locker = models.ForeignKey(Locker, on_delete=models.CASCADE, related_name='compartments')
    size = models.CharField(max_length=20)  # Наприклад, 'small', 'medium', 'large'
    status = models.CharField(max_length=20)  # Наприклад, 'available', 'occupied'

    def __str__(self):
        return f"Locker {self.locker.locker_id} - Compartment {self.compartment_id} ({self.size})"
